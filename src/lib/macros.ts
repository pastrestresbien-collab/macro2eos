import type {
  ActivityLevel,
  Entry,
  Goal,
  Macros,
  Profile,
  Targets,
} from './types.js';

export const CALORIES_PER_GRAM: Macros = { protein: 4, carbs: 4, fat: 9 };

export const ACTIVITY: Record<
  ActivityLevel,
  { label: string; hint: string; multiplier: number }
> = {
  sedentary: { label: 'Sedentary', hint: 'Desk job, little exercise', multiplier: 1.2 },
  light: { label: 'Light', hint: 'Training 1–3 days a week', multiplier: 1.375 },
  moderate: { label: 'Moderate', hint: 'Training 3–5 days a week', multiplier: 1.55 },
  active: { label: 'Active', hint: 'Training 6–7 days a week', multiplier: 1.725 },
  athlete: { label: 'Athlete', hint: 'Twice a day, or physical job', multiplier: 1.9 },
};

export const GOALS: Record<
  Goal,
  { label: string; hint: string; calorieShift: number; proteinPerKg: number }
> = {
  cut: { label: 'Cut', hint: '−20% calories', calorieShift: -0.2, proteinPerKg: 2.2 },
  'lean-cut': { label: 'Lean cut', hint: '−10% calories', calorieShift: -0.1, proteinPerKg: 2.0 },
  maintain: { label: 'Maintain', hint: 'Hold weight', calorieShift: 0, proteinPerKg: 1.8 },
  'lean-bulk': { label: 'Lean bulk', hint: '+10% calories', calorieShift: 0.1, proteinPerKg: 1.8 },
  bulk: { label: 'Bulk', hint: '+20% calories', calorieShift: 0.2, proteinPerKg: 1.6 },
};

/** Share of total calories that comes from fat. The rest, after protein, is carbs. */
const FAT_CALORIE_SHARE = 0.25;
/** Floor so a heavy cut never drops essential fat too low. */
const MIN_FAT_PER_KG = 0.8;

/** Mifflin–St Jeor resting energy expenditure, in kcal/day. */
export function bmr(profile: Pick<Profile, 'sex' | 'age' | 'weightKg' | 'heightCm'>): number {
  const base = 10 * profile.weightKg + 6.25 * profile.heightCm - 5 * profile.age;
  return base + (profile.sex === 'male' ? 5 : -161);
}

/** Total daily energy expenditure: BMR scaled by the activity multiplier. */
export function tdee(profile: Profile): number {
  return bmr(profile) * ACTIVITY[profile.activity].multiplier;
}

/**
 * Daily calorie and macro targets.
 *
 * Protein is set per kilogram of bodyweight, fat takes a fixed share of
 * calories (with a per-kg floor), and carbs absorb whatever is left. Carbs can
 * bottom out at zero on an aggressive cut for a heavy, low-activity profile.
 */
export function targets(profile: Profile): Targets {
  const restingEnergy = bmr(profile);
  const maintenance = restingEnergy * ACTIVITY[profile.activity].multiplier;
  const goal = GOALS[profile.goal];
  const calories = maintenance * (1 + goal.calorieShift);

  const protein = profile.weightKg * goal.proteinPerKg;
  const fat = Math.max(
    (calories * FAT_CALORIE_SHARE) / CALORIES_PER_GRAM.fat,
    profile.weightKg * MIN_FAT_PER_KG,
  );
  const remaining =
    calories - protein * CALORIES_PER_GRAM.protein - fat * CALORIES_PER_GRAM.fat;
  const carbs = Math.max(0, remaining / CALORIES_PER_GRAM.carbs);

  return {
    bmr: Math.round(restingEnergy),
    tdee: Math.round(maintenance),
    calories: Math.round(calories),
    protein: Math.round(protein),
    carbs: Math.round(carbs),
    fat: Math.round(fat),
  };
}

/** Calories implied by a set of macros. */
export function caloriesOf(macros: Macros): number {
  return (
    macros.protein * CALORIES_PER_GRAM.protein +
    macros.carbs * CALORIES_PER_GRAM.carbs +
    macros.fat * CALORIES_PER_GRAM.fat
  );
}

export function scaleMacros(macros: Macros, factor: number): Macros {
  return {
    protein: macros.protein * factor,
    carbs: macros.carbs * factor,
    fat: macros.fat * factor,
  };
}

/** Sum of every entry in a day, already multiplied out by servings. */
export function totals(entries: readonly Entry[]): Macros {
  return entries.reduce<Macros>(
    (sum, entry) => {
      const scaled = scaleMacros(entry.perServing, entry.servings);
      return {
        protein: sum.protein + scaled.protein,
        carbs: sum.carbs + scaled.carbs,
        fat: sum.fat + scaled.fat,
      };
    },
    { protein: 0, carbs: 0, fat: 0 },
  );
}

export const KG_PER_LB = 0.45359237;
export const CM_PER_INCH = 2.54;

export const lbToKg = (lb: number): number => lb * KG_PER_LB;
export const kgToLb = (kg: number): number => kg / KG_PER_LB;
export const inchesToCm = (inches: number): number => inches * CM_PER_INCH;
export const cmToInches = (cm: number): number => cm / CM_PER_INCH;

/** Split centimetres into whole feet plus remaining inches. */
export function cmToFeetInches(cm: number): { feet: number; inches: number } {
  const totalInches = Math.round(cmToInches(cm));
  return { feet: Math.floor(totalInches / 12), inches: totalInches % 12 };
}

export function feetInchesToCm(feet: number, inches: number): number {
  return inchesToCm(feet * 12 + inches);
}
