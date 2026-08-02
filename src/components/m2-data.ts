import { LitElement, css, html } from 'lit';
import { customElement, query, state } from 'lit/decorators.js';
import { backupFilename, parseBackup, serializeBackup } from '../lib/backup.js';
import { StoreController, store } from '../lib/store.js';
import { shared } from '../styles/shared.js';

const plural = (count: number, word: string) => `${count} ${word}${count === 1 ? '' : 's'}`;

/**
 * Backup and restore. The log only lives in this browser, so clearing site data
 * or switching machines loses it unless there is a file somewhere.
 */
@customElement('m2-data')
export class M2Data extends LitElement {
  private store = new StoreController(this);
  @state() private status = '';
  @state() private failed = false;
  @query('#import-file') private fileInput!: HTMLInputElement;

  static override styles = [
    shared,
    css`
      .actions {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
      }

      input[type='file'] {
        display: none;
      }

      .status {
        margin: 0.9rem 0 0;
        font-size: 0.85rem;
      }

      .status.bad {
        color: var(--danger);
      }

      .danger {
        color: var(--danger);
        border-color: color-mix(in srgb, var(--danger) 40%, var(--border));
      }
    `,
  ];

  private get summary() {
    const days = Object.keys(this.store.state.days);
    const entries = days.reduce(
      (count, date) => count + (this.store.state.days[date]?.length ?? 0),
      0,
    );
    return { days: days.length, entries };
  }

  private report(message: string, failed = false) {
    this.status = message;
    this.failed = failed;
  }

  private exportBackup() {
    const json = serializeBackup(this.store.state);
    const url = URL.createObjectURL(new Blob([json], { type: 'application/json' }));
    const link = document.createElement('a');
    link.href = url;
    link.download = backupFilename();
    link.click();
    URL.revokeObjectURL(url);
    this.report('Backup downloaded.');
  }

  private async importBackup(event: Event) {
    const input = event.target as HTMLInputElement;
    const file = input.files?.[0];
    // Reset the input so picking the same file twice still fires a change event.
    input.value = '';
    if (!file) return;

    const { days, entries } = this.summary;
    if (
      entries > 0 &&
      !confirm(
        `Restoring replaces what is already here (${plural(entries, 'food')} across ${plural(days, 'day')}). Continue?`,
      )
    ) {
      return;
    }

    try {
      const restored = parseBackup(await file.text());
      store.replaceState(restored);
      this.report(`Restored ${plural(Object.keys(restored.days).length, 'day')} from ${file.name}.`);
    } catch (error) {
      this.report(error instanceof Error ? error.message : 'That backup could not be read.', true);
    }
  }

  private resetEverything() {
    const { days, entries } = this.summary;
    const warning = entries
      ? `Delete your profile and ${plural(entries, 'logged food')} across ${plural(days, 'day')}? This cannot be undone.`
      : 'Reset your profile back to the defaults?';
    if (!confirm(warning)) return;
    store.reset();
    this.report('Everything reset.');
  }

  override render() {
    const { days, entries } = this.summary;

    return html`
      <section class="card">
        <h2>Your data</h2>
        <p class="muted">
          ${entries
            ? `${plural(entries, 'food')} logged across ${plural(days, 'day')}, stored in this browser only.`
            : 'Nothing logged yet. Everything you log stays in this browser only.'}
        </p>
        <div class="actions">
          <button @click=${this.exportBackup}>Download backup</button>
          <button @click=${() => this.fileInput.click()}>Restore from file</button>
          <button class="ghost danger" @click=${this.resetEverything}>Reset everything</button>
        </div>
        <input
          id="import-file"
          type="file"
          accept="application/json,.json"
          @change=${this.importBackup}
        />
        ${this.status
          ? html`<p class="status ${this.failed ? 'bad' : 'muted'}" role="status">${this.status}</p>`
          : null}
      </section>
    `;
  }
}

declare global {
  interface HTMLElementTagNameMap {
    'm2-data': M2Data;
  }
}
