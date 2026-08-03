import { LitElement, css, html } from 'lit';
import { customElement } from 'lit/decorators.js';
import { describeDate, today } from '../lib/dates.js';
import { targets } from '../lib/macros.js';
import { StoreController, store } from '../lib/store.js';
import { weekSummary, type DaySummary } from '../lib/week.js';
import { shared } from '../styles/shared.js';

const round = (n: number) => Math.round(n);

/**
 * The last seven days against the calorie target.
 *
 * One series, one colour: whether a day ran over is read from the bar crossing
 * the target line, not from a colour change, and every number is repeated in the
 * table underneath.
 */
@customElement('m2-week')
export class M2Week extends LitElement {
  private store = new StoreController(this);

  static override styles = [
    shared,
    css`
      :host {
        display: grid;
        gap: 1rem;
      }

      /* Grid items default to min-width: auto, which would let the table's
         min-content width push the whole page wider than the viewport. */
      .card {
        min-width: 0;
      }

      .kpis {
        display: grid;
        gap: 0.9rem;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
      }

      .kpi {
        background: var(--surface-2);
        border-radius: 12px;
        padding: 0.85rem;
      }

      .kpi .n {
        font-size: 1.6rem;
        font-weight: 680;
        font-variant-numeric: tabular-nums;
        line-height: 1.2;
      }

      .kpi .k {
        font-size: 0.78rem;
        color: var(--text-dim);
        text-transform: uppercase;
        letter-spacing: 0.06em;
      }

      .plot {
        position: relative;
        display: flex;
        align-items: flex-end;
        gap: 6px;
        height: 170px;
        margin-top: 0.5rem;
      }

      /* Hairline, solid, one step off the surface: chrome, not data. */
      .target {
        position: absolute;
        left: 0;
        right: 0;
        border-top: 1px solid var(--border);
        pointer-events: none;
      }

      .col {
        flex: 1 1 0;
        min-width: 0;
        height: 100%;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        padding: 0;
        border: none;
        background: none;
        border-radius: 8px;
      }

      .col:hover {
        background: color-mix(in srgb, var(--accent) 8%, transparent);
      }

      .bar {
        width: 100%;
        max-width: 24px;
        background: var(--c-cal);
        border-radius: 4px 4px 0 0;
        transition: height 360ms cubic-bezier(0.22, 1, 0.36, 1);
      }

      .bar.empty {
        background: var(--border);
        border-radius: 2px;
      }

      .axis {
        display: flex;
        gap: 6px;
        margin-top: 0.4rem;
      }

      .axis span {
        flex: 1 1 0;
        min-width: 0;
        text-align: center;
        font-size: 0.78rem;
        color: var(--text-dim);
      }

      .axis .now {
        color: var(--text);
        font-weight: 650;
      }

      .scroll {
        overflow-x: auto;
      }

      table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.88rem;
        font-variant-numeric: tabular-nums;
      }

      th,
      td {
        text-align: right;
        padding: 0.45rem 0.5rem;
        border-bottom: 1px solid var(--border);
        white-space: nowrap;
      }

      th:first-child,
      td:first-child {
        text-align: left;
      }

      /* Column headers are chrome; row headers are content and stay plain. */
      thead th {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: var(--text-dim);
        font-weight: 600;
      }

      tbody th,
      tfoot th {
        text-align: left;
        font-weight: inherit;
      }

      tbody tr:last-child th,
      tbody tr:last-child td {
        border-bottom: none;
      }

      tfoot th,
      tfoot td {
        border-top: 1px solid var(--border);
        border-bottom: none;
        color: var(--text-dim);
      }

      tr.today td {
        font-weight: 620;
      }

      td.blank {
        color: var(--text-dim);
      }

      .abbr {
        display: none;
      }

      /* On a phone the whole table has to fit without scrolling — it is the
         readable fallback for the chart, so shorten the headers instead. */
      @media (max-width: 520px) {
        th,
        td {
          padding: 0.4rem 0.3rem;
          font-size: 0.84rem;
        }

        .full {
          display: none;
        }

        .abbr {
          display: inline;
        }
      }
    `,
  ];

  private openDay(date: string) {
    store.selectDate(date);
    location.hash = '#today';
  }

  private renderColumn(day: DaySummary, scaleMax: number, targetCalories: number) {
    const height = scaleMax > 0 ? (day.calories / scaleMax) * 100 : 0;
    const over = day.calories - targetCalories;
    const summary = day.entries
      ? `${round(day.calories)} kcal, ${over > 0 ? `${round(over)} over` : `${round(-over)} under`} target`
      : 'nothing logged';

    return html`
      <button
        class="col"
        title=${`${describeDate(day.date)} — ${summary}`}
        aria-label=${`${describeDate(day.date)}, ${summary}. Open this day.`}
        @click=${() => this.openDay(day.date)}
      >
        <span
          class=${day.entries ? 'bar' : 'bar empty'}
          style=${`height: ${day.entries ? Math.max(height, 1.5) : 0.9}%`}
        ></span>
      </button>
    `;
  }

  override render() {
    const { profile } = this.store.state;
    const plan = targets(profile);
    const week = weekSummary(this.store.state.days, plan.calories, today());
    // Headroom, so the target line never sits flush against the top edge on a
    // week where nothing reached it.
    const scaleMax = week.peakCalories * 1.08;
    const targetOffset = scaleMax > 0 ? (plan.calories / scaleMax) * 100 : 0;

    return html`
      <section class="card">
        <h2>Last 7 days</h2>
        <div class="kpis">
          <div class="kpi">
            <div class="n">${week.loggedDays ? round(week.averageCalories) : '—'}</div>
            <div class="k">Avg kcal</div>
          </div>
          <div class="kpi">
            <div class="n">${week.loggedDays}<small>/7</small></div>
            <div class="k">Days logged</div>
          </div>
          <div class="kpi">
            <div class="n">${week.onTargetDays}<small>/${week.loggedDays || 0}</small></div>
            <div class="k">On target</div>
          </div>
        </div>
      </section>

      <section class="card">
        <h2>Calories against your ${plan.calories} kcal target</h2>
        <div class="plot">
          <div class="target" style=${`bottom: ${targetOffset}%`}></div>
          ${week.days.map((day) => this.renderColumn(day, scaleMax, plan.calories))}
        </div>
        <div class="axis" aria-hidden="true">
          ${week.days.map(
            (day) => html`<span class=${day.date === today() ? 'now' : ''}>${day.label}</span>`,
          )}
        </div>
        <p class="muted">A bar above the line is a day over target. Pick one to open it.</p>
      </section>

      <section class="card">
        <h2>Day by day</h2>
        <div class="scroll">
          <table>
            <thead>
              <tr>
                <th scope="col">Day</th>
                <th scope="col">kcal</th>
                <th scope="col">
                  <span class="full">Protein</span><span class="abbr">P</span>
                </th>
                <th scope="col">
                  <span class="full">Carbs</span><span class="abbr">C</span>
                </th>
                <th scope="col"><span class="full">Fat</span><span class="abbr">F</span></th>
              </tr>
            </thead>
            <tbody>
              ${week.days.map(
                (day) => html`
                  <tr class=${day.date === today() ? 'today' : ''}>
                    <th scope="row">${describeDate(day.date)}</th>
                    ${day.entries
                      ? html`
                          <td>${round(day.calories)}</td>
                          <td>${round(day.macros.protein)} g</td>
                          <td>${round(day.macros.carbs)} g</td>
                          <td>${round(day.macros.fat)} g</td>
                        `
                      : html`<td class="blank" colspan="4">
                          <span class="full">Nothing logged</span><span class="abbr">—</span>
                        </td>`}
                  </tr>
                `,
              )}
            </tbody>
            <tfoot>
              <tr>
                <th scope="row">Target</th>
                <td>${plan.calories}</td>
                <td>${plan.protein} g</td>
                <td>${plan.carbs} g</td>
                <td>${plan.fat} g</td>
              </tr>
            </tfoot>
          </table>
        </div>
      </section>
    `;
  }
}

declare global {
  interface HTMLElementTagNameMap {
    'm2-week': M2Week;
  }
}
