import type { Entry, Macros } from './types.js';

/** A food worth offering again, remembered from an earlier day. */
export interface RecentFood {
  name: string;
  serving?: string;
  perServing: Macros;
}

/**
 * The foods logged most recently, newest first and one row per name, so custom
 * entries are as easy to re-add as anything in the built-in list. The macros
 * come from the latest time that food was logged.
 */
export function recentFoods(
  days: Record<string, Entry[]>,
  limit = 6,
): RecentFood[] {
  const dates = Object.keys(days).sort().reverse();
  const seen = new Set<string>();
  const recent: RecentFood[] = [];

  for (const date of dates) {
    // Within a day, the last thing logged is the most recent.
    for (const entry of [...(days[date] ?? [])].reverse()) {
      const key = entry.name.trim().toLowerCase();
      if (!key || seen.has(key)) continue;
      seen.add(key);
      recent.push({ name: entry.name, serving: entry.serving, perServing: entry.perServing });
      if (recent.length >= limit) return recent;
    }
  }

  return recent;
}
