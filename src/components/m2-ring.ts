import { LitElement, css, html, svg } from 'lit';
import { customElement, property } from 'lit/decorators.js';

const RADIUS = 52;
const CIRCUMFERENCE = 2 * Math.PI * RADIUS;

/** A single progress ring: how much of one target has been eaten so far. */
@customElement('m2-ring')
export class M2Ring extends LitElement {
  @property({ type: Number }) value = 0;
  @property({ type: Number }) target = 0;
  @property({ type: String }) label = '';
  @property({ type: String }) unit = 'g';
  @property({ type: String }) color = 'var(--accent)';

  static override styles = css`
    :host {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.4rem;
    }

    svg {
      width: 100%;
      max-width: 128px;
      height: auto;
    }

    .track {
      stroke: var(--surface-2);
    }

    .fill {
      transition: stroke-dashoffset 420ms cubic-bezier(0.22, 1, 0.36, 1);
    }

    .value {
      font-size: 26px;
      font-weight: 660;
      fill: var(--text);
      font-variant-numeric: tabular-nums;
    }

    .of {
      font-size: 13px;
      fill: var(--text-dim);
      font-variant-numeric: tabular-nums;
    }

    .label {
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 0.02em;
      color: var(--text-dim);
    }

    .over {
      color: var(--c-cal);
      font-weight: 650;
    }
  `;

  override render() {
    const value = Math.round(this.value);
    const target = Math.round(this.target);
    const ratio = target > 0 ? value / target : 0;
    const offset = CIRCUMFERENCE * (1 - Math.min(1, Math.max(0, ratio)));
    const over = target > 0 && value > target;
    const remaining = target - value;

    return html`
      <svg viewBox="0 0 128 128" role="img" aria-label=${`${this.label}: ${value} of ${target} ${this.unit}`}>
        ${svg`
          <g transform="rotate(-90 64 64)" fill="none" stroke-width="11" stroke-linecap="round">
            <circle class="track" cx="64" cy="64" r=${RADIUS} />
            <circle
              class="fill"
              cx="64"
              cy="64"
              r=${RADIUS}
              stroke=${over ? 'var(--c-cal)' : this.color}
              stroke-dasharray=${CIRCUMFERENCE}
              stroke-dashoffset=${offset}
            />
          </g>
          <text class="value" x="64" y="62" text-anchor="middle" dominant-baseline="middle">${value}</text>
          <text class="of" x="64" y="84" text-anchor="middle" dominant-baseline="middle">of ${target} ${this.unit}</text>
        `}
      </svg>
      <span class="label">${this.label}</span>
      <span class=${over ? 'label over' : 'label'}>
        ${over ? `${Math.abs(remaining)} ${this.unit} over` : `${remaining} ${this.unit} left`}
      </span>
    `;
  }
}

declare global {
  interface HTMLElementTagNameMap {
    'm2-ring': M2Ring;
  }
}
