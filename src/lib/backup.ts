import { reviveState } from './store.js';
import type { State } from './types.js';

export const BACKUP_APP = 'macro2eos';
export const BACKUP_VERSION = 1;

export interface Backup {
  app: typeof BACKUP_APP;
  version: number;
  exportedAt: string;
  state: State;
}

/** The JSON a user downloads to keep a copy of their log. */
export function serializeBackup(state: State, now = new Date()): string {
  const backup: Backup = {
    app: BACKUP_APP,
    version: BACKUP_VERSION,
    exportedAt: now.toISOString(),
    state,
  };
  return JSON.stringify(backup, null, 2);
}

/** A filename that sorts by date and won't collide across days. */
export function backupFilename(now = new Date()): string {
  const stamp = now.toISOString().slice(0, 10);
  return `macro2eos-backup-${stamp}.json`;
}

/**
 * Reads a backup file back into state. Throws a message worth showing the user;
 * the state itself still goes through the same field-by-field validation as
 * anything loaded from storage, so a hand-edited file cannot corrupt the app.
 */
export function parseBackup(json: string): State {
  let parsed: unknown;
  try {
    parsed = JSON.parse(json);
  } catch {
    throw new Error("That file isn't valid JSON.");
  }

  if (typeof parsed !== 'object' || parsed === null) {
    throw new Error("That file doesn't look like a macro2eos backup.");
  }

  const backup = parsed as Partial<Backup>;
  if (backup.app !== BACKUP_APP) {
    throw new Error("That file doesn't look like a macro2eos backup.");
  }
  if (typeof backup.version !== 'number' || backup.version > BACKUP_VERSION) {
    throw new Error('That backup comes from a newer version of macro2eos.');
  }
  if (typeof backup.state !== 'object' || backup.state === null) {
    throw new Error('That backup has no data in it.');
  }

  return reviveState(backup.state);
}
