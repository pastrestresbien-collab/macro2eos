import { describe, expect, it } from 'vitest';
import { FOODS, findFood } from './foods.js';
import { caloriesOf } from './macros.js';

describe('FOODS', () => {
  it('has unique ids and names', () => {
    expect(new Set(FOODS.map((food) => food.id)).size).toBe(FOODS.length);
    expect(new Set(FOODS.map((food) => food.name)).size).toBe(FOODS.length);
  });

  it('describes a serving and carries at least one macro', () => {
    for (const food of FOODS) {
      expect(food.serving, food.name).not.toBe('');
      expect(caloriesOf(food.macros), food.name).toBeGreaterThan(0);
    }
  });
});

describe('findFood', () => {
  it('matches an exact name regardless of case', () => {
    expect(findFood('chicken breast')?.id).toBe('chicken-breast');
  });

  it('matches a unique prefix', () => {
    expect(findFood('avoc')?.id).toBe('avocado');
  });

  it('falls back to a unique substring', () => {
    expect(findFood('rice')?.id).toBe('rice');
    expect(findFood('yogurt')?.id).toBe('greek-yogurt');
  });

  it('refuses to guess when several foods match', () => {
    // Both "Almonds" and "Avocado" start with "a".
    expect(findFood('a')).toBeUndefined();
  });

  it('returns nothing for an unknown food or blank input', () => {
    expect(findFood('unicorn steak')).toBeUndefined();
    expect(findFood('   ')).toBeUndefined();
  });

  it('prefers an exact name over a longer one containing it', () => {
    // "Eggs" is exact; nothing else should win it.
    expect(findFood('Eggs')?.id).toBe('eggs');
  });
});
