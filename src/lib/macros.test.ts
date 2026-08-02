import { describe, expect, it } from 'vitest';
import {
  ACTIVITY,
  CALORIES_PER_GRAM,
  GOALS,
  bmr,
  caloriesOf,
  cmToFeetInches,
  feetInchesToCm,
  kgToLb,
  lbToKg,
  scaleMacros,
  targets,
  tdee,
  totals,
} from './macros.js';
import type { Entry, Profile } from './types.js';

const profile: Profile = {
  sex: 'male',
  age: 30,
  weightKg: 80,
  heightCm: 180,
  activity: 'moderate',
  goal: 'maintain',
  units: 'metric',
};

describe('bmr', () => {
  it('follows Mifflin–St Jeor for men', () => {
    // 10*80 + 6.25*180 - 5*30 + 5
    expect(bmr(profile)).toBe(1780);
  });

  it('applies the female constant', () => {
    expect(bmr({ ...profile, sex: 'female' })).toBe(1780 - 5 - 161);
  });

  it('drops with age', () => {
    expect(bmr({ ...profile, age: 50 })).toBeLessThan(bmr(profile));
  });
});

describe('tdee', () => {
  it('scales resting burn by the activity multiplier', () => {
    expect(tdee(profile)).toBeCloseTo(1780 * ACTIVITY.moderate.multiplier, 6);
  });

  it('rises monotonically across activity levels', () => {
    const levels = Object.keys(ACTIVITY) as (keyof typeof ACTIVITY)[];
    const values = levels.map((activity) => tdee({ ...profile, activity }));
    for (let i = 1; i < values.length; i++) {
      expect(values[i]).toBeGreaterThan(values[i - 1]);
    }
  });
});

describe('targets', () => {
  it('shifts calories by the goal', () => {
    const maintain = targets(profile).calories;
    expect(targets({ ...profile, goal: 'cut' }).calories).toBeCloseTo(maintain * 0.8, -1);
    expect(targets({ ...profile, goal: 'bulk' }).calories).toBeCloseTo(maintain * 1.2, -1);
  });

  it('sets protein from bodyweight and goal', () => {
    const plan = targets({ ...profile, goal: 'cut' });
    expect(plan.protein).toBe(Math.round(80 * GOALS.cut.proteinPerKg));
  });

  it('produces macros whose calories match the calorie target', () => {
    const plan = targets(profile);
    // Rounding each macro to a whole gram costs a few calories at most.
    expect(caloriesOf(plan)).toBeCloseTo(plan.calories, -1);
  });

  it('keeps fat above the per-kg floor on an aggressive cut', () => {
    const plan = targets({ ...profile, goal: 'cut', activity: 'sedentary' });
    expect(plan.fat).toBeGreaterThanOrEqual(Math.round(80 * 0.8));
  });

  it('never returns negative carbs', () => {
    const extreme = targets({
      ...profile,
      weightKg: 150,
      heightCm: 160,
      age: 70,
      activity: 'sedentary',
      goal: 'cut',
    });
    expect(extreme.carbs).toBeGreaterThanOrEqual(0);
  });

  it('reports the resting and maintenance figures it used', () => {
    const plan = targets(profile);
    expect(plan.bmr).toBe(1780);
    expect(plan.tdee).toBe(Math.round(tdee(profile)));
  });
});

describe('caloriesOf', () => {
  it('uses 4/4/9', () => {
    expect(caloriesOf({ protein: 10, carbs: 20, fat: 5 })).toBe(
      10 * CALORIES_PER_GRAM.protein + 20 * CALORIES_PER_GRAM.carbs + 5 * CALORIES_PER_GRAM.fat,
    );
  });
});

describe('totals', () => {
  const entries: Entry[] = [
    { id: 'a', name: 'Chicken', servings: 2, perServing: { protein: 30, carbs: 0, fat: 3 } },
    { id: 'b', name: 'Rice', servings: 0.5, perServing: { protein: 4, carbs: 60, fat: 1 } },
  ];

  it('multiplies each entry out by its servings', () => {
    expect(totals(entries)).toEqual({ protein: 62, carbs: 30, fat: 6.5 });
  });

  it('is zero for an empty day', () => {
    expect(totals([])).toEqual({ protein: 0, carbs: 0, fat: 0 });
  });
});

describe('scaleMacros', () => {
  it('scales every macro', () => {
    expect(scaleMacros({ protein: 1, carbs: 2, fat: 3 }, 3)).toEqual({
      protein: 3,
      carbs: 6,
      fat: 9,
    });
  });
});

describe('unit conversion', () => {
  it('round-trips pounds', () => {
    expect(kgToLb(lbToKg(154))).toBeCloseTo(154, 9);
  });

  it('matches known weights', () => {
    expect(lbToKg(220.462)).toBeCloseTo(100, 3);
  });

  it('round-trips feet and inches', () => {
    const { feet, inches } = cmToFeetInches(feetInchesToCm(5, 11));
    expect({ feet, inches }).toEqual({ feet: 5, inches: 11 });
  });

  it('carries 12 inches into a foot', () => {
    expect(cmToFeetInches(feetInchesToCm(5, 12))).toEqual({ feet: 6, inches: 0 });
  });
});
