import type { ReactiveController, ReactiveControllerHost } from 'lit';
import { isValidISODate, today } from './dates.js';
import { ACTIVITY, GOALS } from './macros.js';
import type { ActivityLevel, Entry, Goal, Macros, Profile, Sex, State, Units } from './types.js';

const STORAGE_KEY = 'macro2eos.state.v1';

export const DEFAULT_PROFILE: Profile = {
  sex: 'female',
  age: 30,
  weightKg: 68,
  heightCm: 170,
  activity: 'moderate',
  goal: 'maintain',
  units: 'metric',
};

function defaultState(): State {
  return { profile: { ...DEFAULT_PROFILE }, days: {}, selectedDate: today() };
}

function isMacros(value: unknown): value is Macros {
  if (typeof value !== 'object' || value === null) return false;
  const macros = value as Record<string, unknown>;
  return (
    typeof macros.protein === 'number' &&
    typeof macros.carbs === 'number' &&
    typeof macros.fat === 'number'
  );
}

function isEntry(value: unknown): value is Entry {
  if (typeof value !== 'object' || value === null) return false;
  const entry = value as Record<string, unknown>;
  return (
    typeof entry.id === 'string' &&
    typeof entry.name === 'string' &&
    typeof entry.servings === 'number' &&
    isMacros(entry.perServing)
  );
}

function isOneOf<T extends string>(value: unknown, options: readonly T[]): value is T {
  return typeof value === 'string' && (options as readonly string[]).includes(value);
}

function isPositiveNumber(value: unknown): value is number {
  return typeof value === 'number' && Number.isFinite(value) && value > 0;
}

function reviveProfile(raw: unknown): Profile {
  const profile = { ...DEFAULT_PROFILE };
  if (typeof raw !== 'object' || raw === null) return profile;
  const saved = raw as Partial<Record<keyof Profile, unknown>>;

  if (isOneOf<Sex>(saved.sex, ['male', 'female'])) profile.sex = saved.sex;
  if (isOneOf<Units>(saved.units, ['metric', 'imperial'])) profile.units = saved.units;
  if (isOneOf(saved.activity, Object.keys(ACTIVITY) as ActivityLevel[])) {
    profile.activity = saved.activity;
  }
  if (isOneOf(saved.goal, Object.keys(GOALS) as Goal[])) profile.goal = saved.goal;
  if (isPositiveNumber(saved.age)) profile.age = saved.age;
  if (isPositiveNumber(saved.weightKg)) profile.weightKg = saved.weightKg;
  if (isPositiveNumber(saved.heightCm)) profile.heightCm = saved.heightCm;

  return profile;
}

/**
 * Rebuilds state from whatever is in storage, keeping only the parts that still
 * look right. A partially corrupt blob degrades to defaults instead of throwing.
 */
export function reviveState(raw: unknown): State {
  const state = defaultState();
  if (typeof raw !== 'object' || raw === null) return state;
  const parsed = raw as Partial<Record<keyof State, unknown>>;

  state.profile = reviveProfile(parsed.profile);

  if (typeof parsed.days === 'object' && parsed.days !== null) {
    for (const [date, entries] of Object.entries(parsed.days)) {
      if (!isValidISODate(date) || !Array.isArray(entries)) continue;
      const valid = entries.filter(isEntry);
      if (valid.length) state.days[date] = valid;
    }
  }

  if (isValidISODate(parsed.selectedDate)) state.selectedDate = parsed.selectedDate;
  return state;
}

function load(): State {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? reviveState(JSON.parse(raw)) : defaultState();
  } catch {
    return defaultState();
  }
}

function newId(): string {
  return globalThis.crypto?.randomUUID?.() ?? `e${Date.now()}${Math.random().toString(36).slice(2, 8)}`;
}

/**
 * The whole app's state, in one place. Components read `store.state` and
 * re-render when `notify` fires; nothing mutates state in place.
 */
export class Store {
  #state: State;
  #listeners = new Set<() => void>();

  constructor(initial: State = load()) {
    this.#state = initial;
  }

  get state(): State {
    return this.#state;
  }

  get entries(): readonly Entry[] {
    return this.#state.days[this.#state.selectedDate] ?? [];
  }

  subscribe(listener: () => void): () => void {
    this.#listeners.add(listener);
    return () => this.#listeners.delete(listener);
  }

  #commit(next: State): void {
    this.#state = next;
    this.#persist();
    for (const listener of this.#listeners) listener();
  }

  #persist(): void {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(this.#state));
    } catch {
      // Storage full or blocked: the session still works, it just won't survive a reload.
    }
  }

  #setEntries(entries: Entry[]): void {
    this.#commit({
      ...this.#state,
      days: { ...this.#state.days, [this.#state.selectedDate]: entries },
    });
  }

  updateProfile(patch: Partial<Profile>): void {
    this.#commit({ ...this.#state, profile: { ...this.#state.profile, ...patch } });
  }

  selectDate(date: string): void {
    if (!isValidISODate(date)) return;
    this.#commit({ ...this.#state, selectedDate: date });
  }

  addEntry(entry: Omit<Entry, 'id'>): void {
    this.#setEntries([...this.entries, { ...entry, id: newId() }]);
  }

  setServings(id: string, servings: number): void {
    const clamped = Math.max(0.25, Math.round(servings * 4) / 4);
    this.#setEntries(
      this.entries.map((entry) => (entry.id === id ? { ...entry, servings: clamped } : entry)),
    );
  }

  removeEntry(id: string): void {
    this.#setEntries(this.entries.filter((entry) => entry.id !== id));
  }

  clearDay(): void {
    const days = { ...this.#state.days };
    delete days[this.#state.selectedDate];
    this.#commit({ ...this.#state, days });
  }

  /** Swaps in a whole state, e.g. a restored backup. */
  replaceState(next: State): void {
    this.#commit(next);
  }

  /** Wipes everything back to a fresh install. */
  reset(): void {
    this.#commit(defaultState());
  }
}

export const store = new Store();

/** Re-renders its host whenever the store changes. */
export class StoreController implements ReactiveController {
  #unsubscribe?: () => void;

  constructor(
    private host: ReactiveControllerHost,
    private target: Store = store,
  ) {
    host.addController(this);
  }

  get state(): State {
    return this.target.state;
  }

  hostConnected(): void {
    this.#unsubscribe = this.target.subscribe(() => this.host.requestUpdate());
  }

  hostDisconnected(): void {
    this.#unsubscribe?.();
    this.#unsubscribe = undefined;
  }
}
