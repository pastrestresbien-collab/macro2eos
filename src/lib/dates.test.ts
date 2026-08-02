import { describe, expect, it } from 'vitest';
import { describeDate, isValidISODate, shiftDays, toISODate } from './dates.js';

describe('toISODate', () => {
  it('formats in local time, not UTC', () => {
    // Late enough in the day that a UTC conversion would roll the date forward
    // in the western hemisphere and back in the eastern one.
    expect(toISODate(new Date(2026, 0, 5, 23, 30))).toBe('2026-01-05');
    expect(toISODate(new Date(2026, 0, 5, 0, 30))).toBe('2026-01-05');
  });

  it('pads single-digit months and days', () => {
    expect(toISODate(new Date(2026, 8, 9))).toBe('2026-09-09');
  });
});

describe('shiftDays', () => {
  it('moves forward and back', () => {
    expect(shiftDays('2026-03-10', 1)).toBe('2026-03-11');
    expect(shiftDays('2026-03-10', -1)).toBe('2026-03-09');
  });

  it('crosses month and year boundaries', () => {
    expect(shiftDays('2026-01-31', 1)).toBe('2026-02-01');
    expect(shiftDays('2026-01-01', -1)).toBe('2025-12-31');
  });

  it('handles a leap day', () => {
    expect(shiftDays('2028-02-28', 1)).toBe('2028-02-29');
  });
});

describe('isValidISODate', () => {
  it('accepts the stored format', () => {
    expect(isValidISODate('2026-08-02')).toBe(true);
  });

  it('rejects anything else', () => {
    expect(isValidISODate('2026-8-2')).toBe(false);
    expect(isValidISODate('yesterday')).toBe(false);
    expect(isValidISODate(20260802)).toBe(false);
    expect(isValidISODate(undefined)).toBe(false);
  });
});

describe('describeDate', () => {
  const now = '2026-08-02';

  it('names the days either side of today', () => {
    expect(describeDate(now, now)).toBe('Today');
    expect(describeDate('2026-08-01', now)).toBe('Yesterday');
    expect(describeDate('2026-08-03', now)).toBe('Tomorrow');
  });

  it('writes out anything further away', () => {
    expect(describeDate('2026-07-20', now)).not.toBe('Today');
    expect(describeDate('2026-07-20', now)).toMatch(/20/);
  });
});
