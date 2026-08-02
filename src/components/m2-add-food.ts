import { LitElement, css, html } from 'lit';
import { customElement, query, state } from 'lit/decorators.js';
import { FOODS, findFood } from '../lib/foods.js';
import { caloriesOf } from '../lib/macros.js';
import { store } from '../lib/store.js';
import { shared } from '../styles/shared.js';

/** Adds an entry to the selected day, either from the starter list or by hand. */
@customElement('m2-add-food')
export class M2AddFood extends LitElement {
  @state() private custom = false;
  @state() private error = '';
  @query('#food') private foodInput!: HTMLInputElement;

  static override styles = [
    shared,
    css`
      form {
        display: grid;
        gap: 0.75rem;
      }

      .pick {
        display: grid;
        grid-template-columns: minmax(0, 1fr) 5.5rem auto;
        gap: 0.5rem;
        align-items: end;
      }

      .custom-grid {
        display: grid;
        gap: 0.5rem;
        grid-template-columns: repeat(auto-fit, minmax(90px, 1fr));
      }

      .error {
        color: var(--danger);
        font-size: 0.85rem;
        margin: 0;
      }

      .toggle {
        justify-self: start;
        padding-left: 0;
        padding-right: 0;
        color: var(--accent);
        border: none;
        background: none;
        font-size: 0.85rem;
      }

      @media (max-width: 520px) {
        .pick {
          grid-template-columns: minmax(0, 1fr) 5rem;
        }

        .pick button {
          grid-column: 1 / -1;
        }
      }
    `,
  ];

  private addFromList(event: SubmitEvent) {
    event.preventDefault();
    const form = event.currentTarget as HTMLFormElement;
    const data = new FormData(form);
    const name = String(data.get('food') ?? '').trim();
    const servings = Number(data.get('servings')) || 1;

    const food = findFood(name);
    if (!food) {
      this.error = `No single match for "${name}" — pick from the list, or add it as a custom food.`;
      return;
    }

    store.addEntry({
      name: food.name,
      serving: food.serving,
      servings,
      perServing: food.macros,
    });
    this.error = '';
    form.reset();
    this.foodInput.focus();
  }

  private addCustom(event: SubmitEvent) {
    event.preventDefault();
    const form = event.currentTarget as HTMLFormElement;
    const data = new FormData(form);
    const name = String(data.get('name') ?? '').trim();
    const macros = {
      protein: Number(data.get('protein')) || 0,
      carbs: Number(data.get('carbs')) || 0,
      fat: Number(data.get('fat')) || 0,
    };

    if (!name) {
      this.error = 'Give the food a name.';
      return;
    }
    if (caloriesOf(macros) === 0) {
      this.error = 'Enter at least one macro.';
      return;
    }

    store.addEntry({ name, servings: Number(data.get('servings')) || 1, perServing: macros });
    this.error = '';
    form.reset();
  }

  private renderPicker() {
    return html`
      <form @submit=${this.addFromList}>
        <div class="pick">
          <div>
            <label for="food">Food</label>
            <input
              id="food"
              name="food"
              list="m2-foods"
              placeholder="Start typing…"
              autocomplete="off"
              required
            />
          </div>
          <div>
            <label for="servings">Servings</label>
            <input id="servings" name="servings" type="number" min="0.25" step="0.25" value="1" />
          </div>
          <button class="primary" type="submit">Add</button>
        </div>
        <datalist id="m2-foods">
          ${FOODS.map(
            (food) => html`<option value=${food.name}>${food.serving}</option>`,
          )}
        </datalist>
      </form>
    `;
  }

  private renderCustom() {
    return html`
      <form @submit=${this.addCustom}>
        <div>
          <label for="name">Name</label>
          <input id="name" name="name" placeholder="Leftover curry" required />
        </div>
        <div class="custom-grid">
          <div>
            <label for="protein">Protein (g)</label>
            <input id="protein" name="protein" type="number" min="0" step="0.1" value="0" />
          </div>
          <div>
            <label for="carbs">Carbs (g)</label>
            <input id="carbs" name="carbs" type="number" min="0" step="0.1" value="0" />
          </div>
          <div>
            <label for="fat">Fat (g)</label>
            <input id="fat" name="fat" type="number" min="0" step="0.1" value="0" />
          </div>
          <div>
            <label for="custom-servings">Servings</label>
            <input
              id="custom-servings"
              name="servings"
              type="number"
              min="0.25"
              step="0.25"
              value="1"
            />
          </div>
        </div>
        <button class="primary" type="submit">Add custom food</button>
      </form>
    `;
  }

  override render() {
    return html`
      ${this.custom ? this.renderCustom() : this.renderPicker()}
      ${this.error ? html`<p class="error" role="alert">${this.error}</p>` : null}
      <button
        class="toggle"
        @click=${() => {
          this.custom = !this.custom;
          this.error = '';
        }}
      >
        ${this.custom ? '← Back to the food list' : '+ Something not on the list'}
      </button>
    `;
  }
}

declare global {
  interface HTMLElementTagNameMap {
    'm2-add-food': M2AddFood;
  }
}
