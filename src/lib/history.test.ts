import { describe, expect, it } from 'vitest';
import { recentFoods } from './history.js';
import type { Entry } from './types.js';

const entry = (id: string, name: string, protein = 10): Entry => ({
  id,
  name,
  servings: 1,
  perServing: { protein, carbs: 0, fat: 0 },
});

describe('recentFoods', () => {
  it('is empty with no history', () => {
    expect(recentFoods({})).toEqual([]);
  });

  it('puts the newest day first', () => {
    const recent = recentFoods({
      '2026-08-01': [entry('a', 'Oats')],
      '2026-08-03': [entry('b', 'Salmon')],
      '2026-08-02': [entry('c', 'Tofu')],
    });
    expect(recent.map((food) => food.name)).toEqual(['Salmon', 'Tofu', 'Oats']);
  });

  it('treats the last entry of a day as the most recent', () => {
    const recent = recentFoods({ '2026-08-02': [entry('a', 'Oats'), entry('b', 'Milk')] });
    expect(recent.map((food) => food.name)).toEqual(['Milk', 'Oats']);
  });

  it('lists a repeated food once, with its latest macros', () => {
    const recent = recentFoods({
      '2026-08-01': [entry('a', 'Oats', 8)],
      '2026-08-02': [entry('b', 'oats', 12)],
    });
    expect(recent).toHaveLength(1);
    expect(recent[0].perServing.protein).toBe(12);
  });

  it('keeps the serving label when there is one', () => {
    const recent = recentFoods({
      '2026-08-02': [{ ...entry('a', 'Chicken breast'), serving: '150 g cooked' }],
    });
    expect(recent[0].serving).toBe('150 g cooked');
  });

  it('honours the limit and stops scanning early', () => {
    const days: Record<string, Entry[]> = {};
    for (let day = 1; day <= 20; day++) {
      days[`2026-08-${String(day).padStart(2, '0')}`] = [entry(`e${day}`, `Food ${day}`)];
    }
    expect(recentFoods(days)).toHaveLength(6);
    expect(recentFoods(days, 3).map((food) => food.name)).toEqual([
      'Food 20',
      'Food 19',
      'Food 18',
    ]);
  });

  it('skips entries with a blank name', () => {
    expect(recentFoods({ '2026-08-02': [entry('a', '   ')] })).toEqual([]);
  });
});
