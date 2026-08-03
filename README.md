# macro2eos

A macro planner and daily food tracker. Work out your calorie and macro targets
from your body stats, activity level, and goal — then log what you eat and watch
the rings fill up.

Built with [Lit](https://lit.dev), TypeScript, and Vite. No backend: everything
lives in `localStorage`, so nothing leaves the browser.

## Running it

```sh
npm install
npm run dev      # dev server with hot reload
npm test         # unit tests (vitest)
npm run build    # typecheck, then bundle to dist/
npm run preview  # serve the production build
```

## What it does

**Plan tab.** Sex, age, weight, height, activity, and goal go in; daily targets
come out. Resting burn uses Mifflin–St Jeor, scaled by an activity multiplier.
Protein is set per kilogram of bodyweight (higher when cutting), fat takes a
quarter of the calorie budget with a per-kg floor, and carbs absorb the rest.
Metric and imperial units convert in place rather than resetting the profile.

**Day tab.** Four rings — calories, protein, carbs, fat — show today against the
plan, and turn red once a target is passed. Foods come from a small built-in
list (a forgiving lookup, so "rice" finds White rice) or you can type macros in
by hand. Whatever you logged most recently comes back as one-tap chips, custom
entries included. Servings step in quarters, and the arrows move between days;
each day is stored separately.

**Week tab.** The last seven days as a column chart against the calorie target,
plus average intake, days logged, and days on target (within ±10%). Whether a
day ran over is read from the bar crossing the target line rather than from a
colour change, and every value is repeated in the table underneath, which stays
readable without sideways scrolling on a phone. Picking a column opens that day.

**Your data.** At the bottom of the Plan tab: download a JSON backup, restore
one, or reset everything. The log only lives in this browser, so a backup file
is the only thing standing between you and a cleared cache. Restoring over
existing data asks first, and a restored file goes through the same validation
as anything else loaded from storage.

## Layout

```
index.html            design tokens, light/dark theming
src/
  main.ts             registers the app element
  components/
    m2-app.ts         shell: header, hash-routed tabs
    m2-plan.ts        profile form and target summary
    m2-today.ts       rings, day navigation, logged entries
    m2-week.ts        7-day chart, averages, day-by-day table
    m2-add-food.ts    picker, recent chips, custom-food form
    m2-data.ts        backup, restore, reset
    m2-ring.ts        one SVG progress ring
  lib/
    macros.ts         BMR, TDEE, targets, totals, unit conversion
    dates.ts          local-time ISO dates and day arithmetic
    foods.ts          starter food list and lookup
    history.ts        recently logged foods
    week.ts           seven-day rollup and averages
    backup.ts         export and import, with validation
    store.ts          app state, persistence, Lit reactive controller
    types.ts
  styles/shared.ts    styles shared across components
```

State lives in a single `Store`. Components subscribe through
`StoreController`, a Lit reactive controller that re-renders its host on every
change; nothing mutates state in place. Anything read back from storage is
re-validated field by field, so a stale or corrupt blob degrades to defaults
instead of breaking the app.

The four data colours in `index.html` are a set, checked for colour-blind
separation, lightness band, and contrast against each mode's surface — the dark
values are stepped for the dark surface rather than flipped from the light ones.
Change them together, not one at a time.

The calculation and state modules are covered by unit tests (`src/lib/*.test.ts`);
the components are plain rendering on top of them. GitHub Actions runs the
typecheck, the tests, and the build on every push.

## Caveats

The food list holds rounded label figures, not a real nutrition database, and
the targets are population-average estimates — useful as a starting point, not
as medical advice.
