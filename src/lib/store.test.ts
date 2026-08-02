import { beforeEach, describe, expect, it } from 'vitest';
import { DEFAULT_PROFILE, Store, reviveState } from './store.js';
import type { State } from './types.js';

const initial = (): State => ({
  profile: { ...DEFAULT_PROFILE },
  days: {},
  selectedDate: '2026-08-02',
});

describe('Store', () => {
  let store: Store;

  beforeEach(() => {
    // Constructed with explicit state, so nothing is read from storage; writes
    // fail silently in Node, which is the same path as a browser blocking them.
    store = new Store(initial());
  });

  it('starts with an empty day', () => {
    expect(store.entries).toEqual([]);
  });

  it('adds entries with generated ids', () => {
    store.addEntry({ name: 'Oats', servings: 1, perServing: { protein: 8, carbs: 40, fat: 4 } });
    store.addEntry({ name: 'Milk', servings: 1, perServing: { protein: 8, carbs: 12, fat: 8 } });
    const ids = store.entries.map((entry) => entry.id);
    expect(store.entries).toHaveLength(2);
    expect(new Set(ids).size).toBe(2);
  });

  it('keeps each day separate', () => {
    store.addEntry({ name: 'Oats', servings: 1, perServing: { protein: 8, carbs: 40, fat: 4 } });
    store.selectDate('2026-08-03');
    expect(store.entries).toEqual([]);
    store.selectDate('2026-08-02');
    expect(store.entries).toHaveLength(1);
  });

  it('ignores a malformed date', () => {
    store.selectDate('not-a-date');
    expect(store.state.selectedDate).toBe('2026-08-02');
  });

  it('rounds servings to a quarter and never goes below one', () => {
    store.addEntry({ name: 'Rice', servings: 1, perServing: { protein: 5, carbs: 56, fat: 1 } });
    const id = store.entries[0].id;

    store.setServings(id, 1.3);
    expect(store.entries[0].servings).toBe(1.25);

    store.setServings(id, 0);
    expect(store.entries[0].servings).toBe(0.25);
  });

  it('removes a single entry and clears the whole day', () => {
    store.addEntry({ name: 'Rice', servings: 1, perServing: { protein: 5, carbs: 56, fat: 1 } });
    store.addEntry({ name: 'Tofu', servings: 1, perServing: { protein: 17, carbs: 4, fat: 10 } });

    store.removeEntry(store.entries[0].id);
    expect(store.entries.map((entry) => entry.name)).toEqual(['Tofu']);

    store.clearDay();
    expect(store.entries).toEqual([]);
    expect(store.state.days['2026-08-02']).toBeUndefined();
  });

  it('patches the profile without dropping other fields', () => {
    store.updateProfile({ weightKg: 90 });
    expect(store.state.profile.weightKg).toBe(90);
    expect(store.state.profile.age).toBe(DEFAULT_PROFILE.age);
  });

  it('replaces state rather than mutating it', () => {
    const before = store.state;
    store.updateProfile({ age: 41 });
    expect(store.state).not.toBe(before);
    expect(before.profile.age).toBe(DEFAULT_PROFILE.age);
  });

  it('notifies subscribers until they unsubscribe', () => {
    let calls = 0;
    const unsubscribe = store.subscribe(() => calls++);

    store.updateProfile({ age: 33 });
    expect(calls).toBe(1);

    unsubscribe();
    store.updateProfile({ age: 34 });
    expect(calls).toBe(1);
  });
});

describe('reviveState', () => {
  it('falls back to defaults for junk', () => {
    expect(reviveState(null).profile).toEqual(DEFAULT_PROFILE);
    expect(reviveState('nope').days).toEqual({});
    expect(reviveState(42).selectedDate).toMatch(/^\d{4}-\d{2}-\d{2}$/);
  });

  it('keeps valid profile fields and drops invalid ones', () => {
    const revived = reviveState({
      profile: { weightKg: 91, age: -4, goal: 'cut', activity: 'space-travel', sex: 'other' },
    });
    expect(revived.profile.weightKg).toBe(91);
    expect(revived.profile.goal).toBe('cut');
    expect(revived.profile.age).toBe(DEFAULT_PROFILE.age);
    expect(revived.profile.activity).toBe(DEFAULT_PROFILE.activity);
    expect(revived.profile.sex).toBe(DEFAULT_PROFILE.sex);
  });

  it('keeps only well-formed days and entries', () => {
    const good = { id: 'a', name: 'Oats', servings: 1, perServing: { protein: 8, carbs: 40, fat: 4 } };
    const revived = reviveState({
      days: {
        '2026-08-02': [good, { id: 'b', name: 'Broken' }],
        'last tuesday': [good],
        '2026-08-03': 'not an array',
      },
      selectedDate: '2026-08-02',
    });

    expect(Object.keys(revived.days)).toEqual(['2026-08-02']);
    expect(revived.days['2026-08-02']).toEqual([good]);
    expect(revived.selectedDate).toBe('2026-08-02');
  });
});
