import { LitElement, css, html } from 'lit';
import { customElement } from 'lit/decorators.js';
import { describeDate, shiftDays, today } from '../lib/dates.js';
import { caloriesOf, scaleMacros, targets, totals } from '../lib/macros.js';
import { StoreController, store } from '../lib/store.js';
import type { Entry } from '../lib/types.js';
import { shared } from '../styles/shared.js';
import './m2-add-food.js';
import './m2-ring.js';

const round = (n: number) => Math.round(n);

/** The day view: what the targets are, what has been eaten, what is left. */
@customElement('m2-today')
export class M2Today extends LitElement {
  private store = new StoreController(this);

  static override styles = [
    shared,
    css`
      :host {
        display: grid;
        gap: 1rem;
      }

      .date-nav {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.75rem;
      }

      .date-nav .day {
        min-width: 9rem;
        text-align: center;
        font-weight: 620;
      }

      .date-nav .iso {
        display: block;
        font-size: 0.75rem;
        font-weight: 450;
        color: var(--text-dim);
      }

      .date-nav button {
        width: 2.25rem;
        height: 2.25rem;
        padding: 0;
        border-radius: 50%;
        line-height: 1;
      }

      .rings {
        display: grid;
        gap: 1rem;
        grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      }

      .list {
        list-style: none;
        margin: 0;
        padding: 0;
        display: grid;
        gap: 0.5rem;
      }

      li {
        display: grid;
        grid-template-columns: minmax(0, 1fr) auto auto;
        align-items: center;
        gap: 0.75rem;
        padding: 0.65rem 0.8rem;
        background: var(--surface-2);
        border-radius: 12px;
      }

      .name {
        font-weight: 560;
        overflow-wrap: anywhere;
      }

      .serving {
        font-weight: 450;
        font-size: 0.8rem;
        color: var(--text-dim);
      }

      .serving::before {
        content: ' · ';
      }

      .breakdown {
        font-size: 0.8rem;
        color: var(--text-dim);
        font-variant-numeric: tabular-nums;
      }

      .servings {
        display: flex;
        align-items: center;
        gap: 0.35rem;
      }

      .servings button {
        width: 1.9rem;
        height: 1.9rem;
        padding: 0;
        border-radius: 50%;
        line-height: 1;
      }

      .servings .count {
        min-width: 2.4rem;
        text-align: center;
        font-variant-numeric: tabular-nums;
        font-size: 0.9rem;
      }

      .remove {
        border: none;
        background: none;
        color: var(--text-dim);
        font-size: 1.1rem;
        padding: 0.25rem 0.5rem;
      }

      .remove:hover {
        color: var(--danger);
      }

      .head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 1rem;
      }

      .head h2 {
        margin: 0;
      }

      .empty {
        text-align: center;
        color: var(--text-dim);
        padding: 1.5rem 0.5rem;
      }

      .totals {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 0.9rem;
        padding-top: 0.9rem;
        border-top: 1px solid var(--border);
        font-variant-numeric: tabular-nums;
      }

      /* Narrow screens: give the name its own row so nothing squeezes. */
      @media (max-width: 480px) {
        li {
          grid-template-columns: minmax(0, 1fr) auto;
        }

        li > div:first-child {
          grid-column: 1 / -1;
        }
      }
    `,
  ];

  private renderEntry(entry: Entry) {
    const macros = scaleMacros(entry.perServing, entry.servings);
    return html`
      <li>
        <div>
          <div class="name">
            ${entry.name}
            ${entry.serving ? html`<span class="serving">${entry.serving}</span>` : null}
          </div>
          <div class="breakdown">
            ${round(caloriesOf(macros))} kcal · P ${round(macros.protein)} · C
            ${round(macros.carbs)} · F ${round(macros.fat)}
          </div>
        </div>
        <div class="servings">
          <button
            aria-label=${`Fewer servings of ${entry.name}`}
            @click=${() => store.setServings(entry.id, entry.servings - 0.25)}
          >
            −
          </button>
          <span class="count">${entry.servings}×</span>
          <button
            aria-label=${`More servings of ${entry.name}`}
            @click=${() => store.setServings(entry.id, entry.servings + 0.25)}
          >
            +
          </button>
        </div>
        <button
          class="remove"
          aria-label=${`Remove ${entry.name}`}
          @click=${() => store.removeEntry(entry.id)}
        >
          ×
        </button>
      </li>
    `;
  }

  override render() {
    const { profile, selectedDate } = this.store.state;
    const entries = store.entries;
    const plan = targets(profile);
    const eaten = totals(entries);
    const calories = caloriesOf(eaten);

    return html`
      <nav class="date-nav" aria-label="Choose a day">
        <button aria-label="Previous day" @click=${() => store.selectDate(shiftDays(selectedDate, -1))}>
          ‹
        </button>
        <div class="day">
          ${describeDate(selectedDate)}
          <span class="iso">${selectedDate}</span>
        </div>
        <button
          aria-label="Next day"
          ?disabled=${selectedDate >= today()}
          @click=${() => store.selectDate(shiftDays(selectedDate, 1))}
        >
          ›
        </button>
      </nav>

      <section class="card">
        <div class="rings">
          <m2-ring
            label="Calories"
            unit="kcal"
            color="var(--c-cal)"
            .value=${calories}
            .target=${plan.calories}
          ></m2-ring>
          <m2-ring
            label="Protein"
            color="var(--c-protein)"
            .value=${eaten.protein}
            .target=${plan.protein}
          ></m2-ring>
          <m2-ring
            label="Carbs"
            color="var(--c-carbs)"
            .value=${eaten.carbs}
            .target=${plan.carbs}
          ></m2-ring>
          <m2-ring
            label="Fat"
            color="var(--c-fat)"
            .value=${eaten.fat}
            .target=${plan.fat}
          ></m2-ring>
        </div>
      </section>

      <section class="card">
        <h2>Log a food</h2>
        <m2-add-food></m2-add-food>
      </section>

      <section class="card">
        <div class="head">
          <h2>${describeDate(selectedDate)}'s food</h2>
          ${entries.length
            ? html`<button class="ghost" @click=${() => store.clearDay()}>Clear day</button>`
            : null}
        </div>
        ${entries.length
          ? html`
              <ul class="list">
                ${entries.map((entry) => this.renderEntry(entry))}
              </ul>
              <div class="totals">
                <strong>${round(calories)} kcal</strong>
                <span class="muted">
                  P ${round(eaten.protein)} g · C ${round(eaten.carbs)} g · F ${round(eaten.fat)} g
                </span>
              </div>
            `
          : html`<p class="empty">Nothing logged yet. Add your first food above.</p>`}
      </section>
    `;
  }
}

declare global {
  interface HTMLElementTagNameMap {
    'm2-today': M2Today;
  }
}
