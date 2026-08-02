/** Local-time `YYYY-MM-DD`. Avoids `toISOString`, which shifts to UTC. */
export function toISODate(date: Date): string {
  const month = `${date.getMonth() + 1}`.padStart(2, '0');
  const day = `${date.getDate()}`.padStart(2, '0');
  return `${date.getFullYear()}-${month}-${day}`;
}

export function today(): string {
  return toISODate(new Date());
}

export function parseISODate(iso: string): Date {
  const [year, month, day] = iso.split('-').map(Number);
  return new Date(year, month - 1, day);
}

export function shiftDays(iso: string, delta: number): string {
  const date = parseISODate(iso);
  date.setDate(date.getDate() + delta);
  return toISODate(date);
}

export function isValidISODate(value: unknown): value is string {
  return typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value);
}

/** "Today", "Yesterday", or a written-out date for anything further away. */
export function describeDate(iso: string, now = today()): string {
  if (iso === now) return 'Today';
  if (iso === shiftDays(now, -1)) return 'Yesterday';
  if (iso === shiftDays(now, 1)) return 'Tomorrow';
  return parseISODate(iso).toLocaleDateString(undefined, {
    weekday: 'short',
    day: 'numeric',
    month: 'short',
  });
}
