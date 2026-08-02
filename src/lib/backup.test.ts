import { describe, expect, it } from 'vitest';
import { backupFilename, parseBackup, serializeBackup } from './backup.js';
import { DEFAULT_PROFILE } from './store.js';
import type { State } from './types.js';

const state: State = {
  profile: { ...DEFAULT_PROFILE, weightKg: 77, goal: 'lean-bulk' },
  days: {
    '2026-08-01': [
      { id: 'a', name: 'Oats', servings: 1.5, perServing: { protein: 8, carbs: 40, fat: 4 } },
    ],
  },
  selectedDate: '2026-08-01',
};

describe('serializeBackup', () => {
  it('round-trips through parseBackup', () => {
    expect(parseBackup(serializeBackup(state))).toEqual(state);
  });

  it('stamps the file with the app, version, and time', () => {
    const backup = JSON.parse(serializeBackup(state, new Date('2026-08-02T10:00:00Z')));
    expect(backup.app).toBe('macro2eos');
    expect(backup.version).toBe(1);
    expect(backup.exportedAt).toBe('2026-08-02T10:00:00.000Z');
  });
});

describe('backupFilename', () => {
  it('is dated and sorts chronologically', () => {
    expect(backupFilename(new Date('2026-08-02T22:00:00Z'))).toBe('macro2eos-backup-2026-08-02.json');
  });
});

describe('parseBackup', () => {
  it('rejects text that is not JSON', () => {
    expect(() => parseBackup('nope')).toThrow(/valid JSON/);
  });

  it('rejects JSON from some other app', () => {
    expect(() => parseBackup(JSON.stringify({ app: 'something-else', state }))).toThrow(
      /macro2eos backup/,
    );
    expect(() => parseBackup(JSON.stringify([1, 2, 3]))).toThrow(/macro2eos backup/);
  });

  it('refuses a backup from a future version', () => {
    expect(() =>
      parseBackup(JSON.stringify({ app: 'macro2eos', version: 99, state })),
    ).toThrow(/newer version/);
  });

  it('rejects a backup with no state', () => {
    expect(() => parseBackup(JSON.stringify({ app: 'macro2eos', version: 1 }))).toThrow(
      /no data/,
    );
  });

  it('sanitises a hand-edited backup instead of trusting it', () => {
    const restored = parseBackup(
      JSON.stringify({
        app: 'macro2eos',
        version: 1,
        state: {
          profile: { weightKg: -10, goal: 'become-a-bird' },
          days: { 'someday': [{ id: 'x', name: 'X', servings: 1, perServing: {} }] },
        },
      }),
    );

    expect(restored.profile.weightKg).toBe(DEFAULT_PROFILE.weightKg);
    expect(restored.profile.goal).toBe(DEFAULT_PROFILE.goal);
    expect(restored.days).toEqual({});
  });
});
