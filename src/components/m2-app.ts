import { LitElement, css, html } from 'lit';
import { customElement, state } from 'lit/decorators.js';
import { today } from '../lib/dates.js';
import { StoreController, store } from '../lib/store.js';
import { shared } from '../styles/shared.js';
import './m2-plan.js';
import './m2-today.js';
import './m2-week.js';

type Tab = 'today' | 'week' | 'plan';

const TABS: { id: Tab; label: string }[] = [
  { id: 'today', label: 'Day' },
  { id: 'week', label: 'Week' },
  { id: 'plan', label: 'Plan' },
];

function tabFromHash(hash: string): Tab {
  const id = hash.replace('#', '');
  return TABS.some((tab) => tab.id === id) ? (id as Tab) : 'today';
}

/** App shell: header, tabs, and whichever view is active. */
@customElement('m2-app')
export class M2App extends LitElement {
  private store = new StoreController(this);
  @state() private tab: Tab = tabFromHash(location.hash);

  private onHashChange = () => {
    this.tab = tabFromHash(location.hash);
  };

  static override styles = [
    shared,
    css`
      :host {
        display: block;
        max-width: 780px;
        margin: 0 auto;
        padding: 1.25rem 1rem 4rem;
      }

      header.app {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        flex-wrap: wrap;
        margin-bottom: 1.25rem;
      }

      .brand {
        display: flex;
        align-items: center;
        gap: 0.6rem;
      }

      .brand h1 {
        font-size: 1.15rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        margin: 0;
      }

      .brand p {
        margin: 0;
        font-size: 0.8rem;
        color: var(--text-dim);
      }

      .mark {
        width: 34px;
        height: 34px;
        flex: none;
      }

      nav.tabs {
        display: flex;
        gap: 0.25rem;
        padding: 0.2rem;
        background: var(--surface-2);
        border: 1px solid var(--border);
        border-radius: 999px;
      }

      nav.tabs a {
        padding: 0.35rem 1rem;
        border-radius: 999px;
        font-size: 0.9rem;
        font-weight: 550;
        color: var(--text-dim);
        text-decoration: none;
      }

      nav.tabs a[aria-current='page'] {
        background: var(--surface);
        color: var(--text);
        box-shadow: var(--shadow);
      }

      nav.tabs a:focus-visible {
        outline: 2px solid var(--accent);
        outline-offset: 2px;
      }

      footer {
        margin-top: 2rem;
        text-align: center;
      }
    `,
  ];

  override connectedCallback(): void {
    super.connectedCallback();
    window.addEventListener('hashchange', this.onHashChange);
    // A tab left open overnight should land on the new day, not yesterday.
    if (this.store.state.selectedDate < today()) store.selectDate(today());
  }

  override disconnectedCallback(): void {
    window.removeEventListener('hashchange', this.onHashChange);
    super.disconnectedCallback();
  }

  override render() {
    return html`
      <header class="app">
        <div class="brand">
          <svg class="mark" viewBox="0 0 32 32" aria-hidden="true">
            <g transform="rotate(-90 16 16)" fill="none" stroke-width="5" stroke-linecap="round">
              <circle cx="16" cy="16" r="13" stroke="var(--surface-2)" />
              <circle
                cx="16"
                cy="16"
                r="13"
                stroke="var(--accent)"
                stroke-dasharray="61 82"
              />
            </g>
          </svg>
          <div>
            <h1>macro2eos</h1>
            <p>Plan your macros, track your day.</p>
          </div>
        </div>
        <nav class="tabs">
          ${TABS.map(
            (tab) => html`
              <a
                href=${`#${tab.id}`}
                aria-current=${this.tab === tab.id ? 'page' : 'false'}
              >
                ${tab.label}
              </a>
            `,
          )}
        </nav>
      </header>

      <main>
        ${this.tab === 'plan'
          ? html`<m2-plan></m2-plan>`
          : this.tab === 'week'
            ? html`<m2-week></m2-week>`
            : html`<m2-today></m2-today>`}
      </main>

      <footer>
        <p class="muted">Everything stays in this browser — nothing is uploaded.</p>
      </footer>
    `;
  }
}

declare global {
  interface HTMLElementTagNameMap {
    'm2-app': M2App;
  }
}
