import { describe, expect, it } from 'vitest';
import { ON_TARGET_TOLERANCE, weekSummary } from './week.js';
import type { Entry } from './types.js';

/** An entry worth exactly `calories` kcal, all from carbs. */
const carbs = (id: string, calories: number): Entry => ({
  id,
  name: `Food ${id}`,
  servings: 1,
  perServing: { protein: 0, carbs: calories / 4, fat: 0 },
});

const days = {
  '2026-08-02': [carbs('a', 2000)],
  '2026-08-01': [carbs('b', 1000)],
  '2026-07-30': [carbs('c', 3000)],
};

describe('weekSummary', () => {
  it('covers the requested window, oldest first, ending on the given day', () => {
    const week = weekSummary(days, 2000, '2026-08-02');
    expect(week.days).toHaveLength(7);
    expect(week.days[0].date).toBe('2026-07-27');
    expect(week.days[6].date).toBe('2026-08-02');
  });

  it('honours a custom window length', () => {
    expect(weekSummary(days, 2000, '2026-08-02', 3).days.map((d) => d.date)).toEqual([
      '2026-07-31',
      '2026-08-01',
      '2026-08-02',
    ]);
  });

  it('totals each day and leaves untouched days empty', () => {
    const week = weekSummary(days, 2000, '2026-08-02');
    const last = week.days[6];
    expect(last.calories).toBe(2000);
    expect(last.entries).toBe(1);
    expect(week.days[5].calories).toBe(1000);
    expect(week.days[2]).toMatchObject({ date: '2026-07-29', entries: 0, calories: 0 });
  });

  it('labels every day', () => {
    for (const day of weekSummary(days, 2000, '2026-08-02').days) {
      expect(day.label).not.toBe('');
    }
  });

  it('averages over logged days only, ignoring blank ones', () => {
    const week = weekSummary(days, 2000, '2026-08-02');
    expect(week.loggedDays).toBe(3);
    // (2000 + 1000 + 3000) / 3, not / 7.
    expect(week.averageCalories).toBe(2000);
    expect(week.averageMacros.carbs).toBe(500);
  });

  it('reports zero rather than dividing by zero for an empty week', () => {
    const week = weekSummary({}, 2000, '2026-08-02');
    expect(week.loggedDays).toBe(0);
    expect(week.averageCalories).toBe(0);
    expect(week.onTargetDays).toBe(0);
  });

  it('counts a day on target within the tolerance, inclusive of the edge', () => {
    const target = 2000;
    const edge = target * (1 + ON_TARGET_TOLERANCE);
    const week = weekSummary(
      {
        '2026-08-02': [carbs('a', target)],
        '2026-08-01': [carbs('b', edge)],
        '2026-07-31': [carbs('c', edge + 4)],
      },
      target,
      '2026-08-02',
    );
    expect(week.onTargetDays).toBe(2);
  });

  it('never counts a blank day as on target', () => {
    expect(weekSummary({}, 0, '2026-08-02').onTargetDays).toBe(0);
  });

  it('scales the chart to the target when every day is under it', () => {
    expect(weekSummary({ '2026-08-02': [carbs('a', 500)] }, 2200, '2026-08-02').peakCalories).toBe(
      2200,
    );
  });

  it('scales the chart to the biggest day when one goes over', () => {
    expect(weekSummary(days, 2000, '2026-08-02').peakCalories).toBe(3000);
  });
});
