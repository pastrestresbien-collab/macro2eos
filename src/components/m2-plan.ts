import { LitElement, css, html } from 'lit';
import { customElement } from 'lit/decorators.js';
import {
  ACTIVITY,
  GOALS,
  cmToFeetInches,
  feetInchesToCm,
  kgToLb,
  lbToKg,
  targets,
} from '../lib/macros.js';
import { StoreController, store } from '../lib/store.js';
import type { ActivityLevel, Goal, Sex, Units } from '../lib/types.js';
import { shared } from '../styles/shared.js';
import './m2-data.js';

const clamp = (value: number, min: number, max: number) =>
  Math.min(max, Math.max(min, value));

/** The calculator: profile in, daily targets out. */
@customElement('m2-plan')
export class M2Plan extends LitElement {
  private store = new StoreController(this);

  static override styles = [
    shared,
    css`
      :host {
        display: grid;
        gap: 1rem;
      }

      .units {
        display: flex;
        gap: 0.25rem;
        padding: 0.2rem;
        background: var(--surface-2);
        border: 1px solid var(--border);
        border-radius: 999px;
      }

      .units button {
        border: none;
        background: transparent;
        border-radius: 999px;
        padding: 0.3rem 0.8rem;
        font-size: 0.85rem;
        color: var(--text-dim);
      }

      .units button[aria-pressed='true'] {
        background: var(--surface);
        color: var(--text);
        box-shadow: var(--shadow);
      }

      header.card-head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 1rem;
      }

      header.card-head h2 {
        margin: 0;
      }

      .height-imperial {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.5rem;
      }

      .choices {
        display: grid;
        gap: 0.5rem;
      }

      .choice {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 0.75rem;
        width: 100%;
        text-align: left;
        padding: 0.6rem 0.8rem;
      }

      .choice[aria-pressed='true'] {
        border-color: var(--accent);
        background: color-mix(in srgb, var(--accent) 12%, var(--surface-2));
      }

      .choice .hint {
        font-size: 0.78rem;
        font-weight: 450;
        color: var(--text-dim);
      }

      .summary {
        display: grid;
        gap: 0.9rem;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
      }

      .stat {
        background: var(--surface-2);
        border-radius: 12px;
        padding: 0.85rem;
        border-top: 3px solid var(--tint, var(--accent));
      }

      .stat .n {
        font-size: 1.6rem;
        font-weight: 680;
        font-variant-numeric: tabular-nums;
        line-height: 1.2;
      }

      .stat .k {
        font-size: 0.78rem;
        color: var(--text-dim);
        text-transform: uppercase;
        letter-spacing: 0.06em;
      }

      .basis {
        margin-top: 1rem;
        padding-top: 0.9rem;
        border-top: 1px solid var(--border);
        display: flex;
        gap: 1.5rem;
        flex-wrap: wrap;
      }
    `,
  ];

  private get profile() {
    return this.store.state.profile;
  }

  private onNumber(field: 'age' | 'weightKg' | 'heightCm', transform: (n: number) => number) {
    return (event: Event) => {
      const raw = Number((event.target as HTMLInputElement).value);
      if (!Number.isFinite(raw) || raw <= 0) return;
      store.updateProfile({ [field]: transform(raw) });
    };
  }

  private renderWeight() {
    const { units, weightKg } = this.profile;
    const imperial = units === 'imperial';
    const shown = imperial ? Math.round(kgToLb(weightKg)) : Math.round(weightKg);
    return html`
      <div>
        <label for="weight">Weight (${imperial ? 'lb' : 'kg'})</label>
        <input
          id="weight"
          type="number"
          inputmode="decimal"
          min="1"
          .value=${String(shown)}
          @change=${this.onNumber('weightKg', (n) =>
            clamp(imperial ? lbToKg(n) : n, 25, 350),
          )}
        />
      </div>
    `;
  }

  private renderHeight() {
    const { units, heightCm } = this.profile;
    if (units === 'metric') {
      return html`
        <div>
          <label for="height">Height (cm)</label>
          <input
            id="height"
            type="number"
            inputmode="numeric"
            min="1"
            .value=${String(Math.round(heightCm))}
            @change=${this.onNumber('heightCm', (n) => clamp(n, 100, 250))}
          />
        </div>
      `;
    }

    const { feet, inches } = cmToFeetInches(heightCm);
    const setHeight = (nextFeet: number, nextInches: number) =>
      store.updateProfile({
        heightCm: clamp(feetInchesToCm(nextFeet, nextInches), 100, 250),
      });

    return html`
      <div>
        <label for="feet">Height (ft / in)</label>
        <div class="height-imperial">
          <input
            id="feet"
            type="number"
            inputmode="numeric"
            min="3"
            max="8"
            aria-label="Height, feet"
            .value=${String(feet)}
            @change=${(e: Event) =>
              setHeight(Number((e.target as HTMLInputElement).value) || feet, inches)}
          />
          <input
            id="inches"
            type="number"
            inputmode="numeric"
            min="0"
            max="11"
            aria-label="Height, inches"
            .value=${String(inches)}
            @change=${(e: Event) =>
              setHeight(feet, clamp(Number((e.target as HTMLInputElement).value) || 0, 0, 11))}
          />
        </div>
      </div>
    `;
  }

  override render() {
    const profile = this.profile;
    const plan = targets(profile);

    return html`
      <section class="card">
        <header class="card-head">
          <h2>About you</h2>
          <div class="units" role="group" aria-label="Units">
            ${(['metric', 'imperial'] as Units[]).map(
              (unit) => html`
                <button
                  aria-pressed=${profile.units === unit}
                  @click=${() => store.updateProfile({ units: unit })}
                >
                  ${unit === 'metric' ? 'kg / cm' : 'lb / ft'}
                </button>
              `,
            )}
          </div>
        </header>

        <div class="grid">
          <div>
            <label for="sex">Sex</label>
            <select
              id="sex"
              .value=${profile.sex}
              @change=${(e: Event) =>
                store.updateProfile({ sex: (e.target as HTMLSelectElement).value as Sex })}
            >
              <option value="female">Female</option>
              <option value="male">Male</option>
            </select>
          </div>

          <div>
            <label for="age">Age</label>
            <input
              id="age"
              type="number"
              inputmode="numeric"
              min="14"
              max="100"
              .value=${String(profile.age)}
              @change=${this.onNumber('age', (n) => clamp(Math.round(n), 14, 100))}
            />
          </div>

          ${this.renderWeight()} ${this.renderHeight()}
        </div>
      </section>

      <section class="card">
        <h2>Activity</h2>
        <div class="choices">
          ${(Object.keys(ACTIVITY) as ActivityLevel[]).map((level) => {
            const option = ACTIVITY[level];
            return html`
              <button
                class="choice"
                aria-pressed=${profile.activity === level}
                @click=${() => store.updateProfile({ activity: level })}
              >
                <span>${option.label}</span>
                <span class="hint">${option.hint} · ×${option.multiplier}</span>
              </button>
            `;
          })}
        </div>
      </section>

      <section class="card">
        <h2>Goal</h2>
        <div class="choices">
          ${(Object.keys(GOALS) as Goal[]).map((goal) => {
            const option = GOALS[goal];
            return html`
              <button
                class="choice"
                aria-pressed=${profile.goal === goal}
                @click=${() => store.updateProfile({ goal })}
              >
                <span>${option.label}</span>
                <span class="hint">${option.hint} · ${option.proteinPerKg} g protein/kg</span>
              </button>
            `;
          })}
        </div>
      </section>

      <section class="card">
        <h2>Your daily targets</h2>
        <div class="summary">
          <div class="stat" style="--tint: var(--c-cal)">
            <div class="n">${plan.calories}</div>
            <div class="k">kcal</div>
          </div>
          <div class="stat" style="--tint: var(--c-protein)">
            <div class="n">${plan.protein}<small>g</small></div>
            <div class="k">Protein</div>
          </div>
          <div class="stat" style="--tint: var(--c-carbs)">
            <div class="n">${plan.carbs}<small>g</small></div>
            <div class="k">Carbs</div>
          </div>
          <div class="stat" style="--tint: var(--c-fat)">
            <div class="n">${plan.fat}<small>g</small></div>
            <div class="k">Fat</div>
          </div>
        </div>
        <div class="basis">
          <span class="muted num">Resting burn ${plan.bmr} kcal</span>
          <span class="muted num">Maintenance ${plan.tdee} kcal</span>
          <span class="muted">${GOALS[profile.goal].label} · ${GOALS[profile.goal].hint}</span>
        </div>
        <p class="muted">
          Mifflin–St Jeor for resting burn, scaled by activity. Protein is set per kilogram of
          bodyweight, fat takes a quarter of calories, and carbs fill the rest. Estimates, not
          medical advice.
        </p>
      </section>

      <m2-data></m2-data>
    `;
  }
}

declare global {
  interface HTMLElementTagNameMap {
    'm2-plan': M2Plan;
  }
}
