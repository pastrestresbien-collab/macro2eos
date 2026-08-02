import type { Food } from './types.js';

/**
 * A small starter list so the log is usable without typing macros by hand.
 * Values are rounded label figures, not a nutrition database.
 */
export const FOODS: readonly Food[] = [
  { id: 'chicken-breast', name: 'Chicken breast', serving: '150 g cooked', macros: { protein: 46, carbs: 0, fat: 5 } },
  { id: 'salmon', name: 'Salmon fillet', serving: '140 g cooked', macros: { protein: 39, carbs: 0, fat: 18 } },
  { id: 'eggs', name: 'Eggs', serving: '2 large', macros: { protein: 13, carbs: 1, fat: 10 } },
  { id: 'greek-yogurt', name: 'Greek yogurt, 0%', serving: '200 g', macros: { protein: 20, carbs: 8, fat: 1 } },
  { id: 'whey', name: 'Whey protein', serving: '1 scoop (30 g)', macros: { protein: 24, carbs: 3, fat: 2 } },
  { id: 'tofu', name: 'Firm tofu', serving: '150 g', macros: { protein: 17, carbs: 4, fat: 10 } },
  { id: 'lentils', name: 'Lentils', serving: '200 g cooked', macros: { protein: 18, carbs: 40, fat: 1 } },
  { id: 'rice', name: 'White rice', serving: '200 g cooked', macros: { protein: 5, carbs: 56, fat: 1 } },
  { id: 'oats', name: 'Rolled oats', serving: '60 g dry', macros: { protein: 8, carbs: 40, fat: 4 } },
  { id: 'sweet-potato', name: 'Sweet potato', serving: '200 g baked', macros: { protein: 4, carbs: 41, fat: 0 } },
  { id: 'pasta', name: 'Pasta', serving: '200 g cooked', macros: { protein: 10, carbs: 62, fat: 2 } },
  { id: 'bread', name: 'Wholemeal bread', serving: '2 slices', macros: { protein: 8, carbs: 30, fat: 3 } },
  { id: 'banana', name: 'Banana', serving: '1 medium', macros: { protein: 1, carbs: 27, fat: 0 } },
  { id: 'apple', name: 'Apple', serving: '1 medium', macros: { protein: 0, carbs: 25, fat: 0 } },
  { id: 'broccoli', name: 'Broccoli', serving: '150 g', macros: { protein: 4, carbs: 10, fat: 0 } },
  { id: 'olive-oil', name: 'Olive oil', serving: '1 tbsp', macros: { protein: 0, carbs: 0, fat: 14 } },
  { id: 'almonds', name: 'Almonds', serving: '30 g', macros: { protein: 6, carbs: 6, fat: 15 } },
  { id: 'peanut-butter', name: 'Peanut butter', serving: '2 tbsp', macros: { protein: 8, carbs: 6, fat: 16 } },
  { id: 'avocado', name: 'Avocado', serving: '1/2 medium', macros: { protein: 2, carbs: 6, fat: 15 } },
  { id: 'cheddar', name: 'Cheddar', serving: '30 g', macros: { protein: 7, carbs: 0, fat: 10 } },
  { id: 'milk', name: 'Whole milk', serving: '250 ml', macros: { protein: 8, carbs: 12, fat: 8 } },
  { id: 'dark-chocolate', name: 'Dark chocolate', serving: '25 g', macros: { protein: 2, carbs: 12, fat: 9 } },
];

/**
 * Looks a food up the way someone types it: an exact name first, then a unique
 * prefix or substring. "rice" finds White rice; "o" is ambiguous, so it fails
 * rather than guessing between oats, olive oil, and the rest.
 */
export function findFood(query: string): Food | undefined {
  const needle = query.trim().toLowerCase();
  if (!needle) return undefined;

  const exact = FOODS.find((food) => food.name.toLowerCase() === needle);
  if (exact) return exact;

  for (const match of [
    (name: string) => name.startsWith(needle),
    (name: string) => name.includes(needle),
  ]) {
    const hits = FOODS.filter((food) => match(food.name.toLowerCase()));
    if (hits.length === 1) return hits[0];
  }

  return undefined;
}
