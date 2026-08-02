export type Sex = 'male' | 'female';

export type Units = 'metric' | 'imperial';

export type ActivityLevel =
  | 'sedentary'
  | 'light'
  | 'moderate'
  | 'active'
  | 'athlete';

export type Goal = 'cut' | 'lean-cut' | 'maintain' | 'lean-bulk' | 'bulk';

/** Everything the calculator needs. Weight/height are always stored in metric. */
export interface Profile {
  sex: Sex;
  age: number;
  /** kilograms */
  weightKg: number;
  /** centimetres */
  heightCm: number;
  activity: ActivityLevel;
  goal: Goal;
  units: Units;
}

export interface Macros {
  protein: number;
  carbs: number;
  fat: number;
}

export interface Targets extends Macros {
  calories: number;
  bmr: number;
  tdee: number;
}

/** One logged food for a given day. Macros are for the whole entry. */
export interface Entry {
  id: string;
  name: string;
  servings: number;
  /** what one serving is, e.g. "150 g cooked" — absent for custom entries */
  serving?: string;
  /** per single serving */
  perServing: Macros;
}

export interface Food {
  id: string;
  name: string;
  serving: string;
  macros: Macros;
}

export interface State {
  profile: Profile;
  /** ISO `YYYY-MM-DD` -> entries logged that day */
  days: Record<string, Entry[]>;
  selectedDate: string;
}
