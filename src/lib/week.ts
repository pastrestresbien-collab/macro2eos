import { parseISODate, shiftDays } from './dates.js';
import { caloriesOf, totals } from './macros.js';
import type { Entry, Macros } from './types.js';

export interface DaySummary {
  date: string;
  /** Short weekday name in the viewer's locale, e.g. "Mon". */
  label: string;
  entries: number;
  macros: Macros;
  calories: number;
}

export interface WeekSummary {
  /** Oldest first, so it reads left to right. */
  days: DaySummary[];
  loggedDays: number;
  /** Averaged over logged days only — a blank day is missing data, not a zero. */
  averageCalories: number;
  averageMacros: Macros;
  /** Logged days landing within `tolerance` of the calorie target. */
  onTargetDays: number;
  /** Tallest value the chart has to fit, never less than the target. */
  peakCalories: number;
}

/** A day counts as on target when it lands within ±10% of the calorie goal. */
export const ON_TARGET_TOLERANCE = 0.1;

export function weekSummary(
  days: Record<string, Entry[]>,
  targetCalories: number,
  endDate: string,
  length = 7,
): WeekSummary {
  const summaries: DaySummary[] = [];

  for (let offset = length - 1; offset >= 0; offset--) {
    const date = shiftDays(endDate, -offset);
    const entries = days[date] ?? [];
    const macros = totals(entries);
    summaries.push({
      date,
      label: parseISODate(date).toLocaleDateString(undefined, { weekday: 'short' }),
      entries: entries.length,
      macros,
      calories: caloriesOf(macros),
    });
  }

  const logged = summaries.filter((day) => day.entries > 0);
  const sum = logged.reduce<Macros & { calories: number }>(
    (acc, day) => ({
      calories: acc.calories + day.calories,
      protein: acc.protein + day.macros.protein,
      carbs: acc.carbs + day.macros.carbs,
      fat: acc.fat + day.macros.fat,
    }),
    { calories: 0, protein: 0, carbs: 0, fat: 0 },
  );

  const divisor = logged.length || 1;
  const margin = targetCalories * ON_TARGET_TOLERANCE;

  return {
    days: summaries,
    loggedDays: logged.length,
    averageCalories: sum.calories / divisor,
    averageMacros: {
      protein: sum.protein / divisor,
      carbs: sum.carbs / divisor,
      fat: sum.fat / divisor,
    },
    onTargetDays: logged.filter(
      (day) => Math.abs(day.calories - targetCalories) <= margin,
    ).length,
    peakCalories: Math.max(targetCalories, ...summaries.map((day) => day.calories)),
  };
}
