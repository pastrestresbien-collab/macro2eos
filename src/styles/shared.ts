import { css } from 'lit';

/** Controls and surfaces that show up in more than one component. */
export const shared = css`
  :host {
    display: block;
    font-family: var(--font);
    color: var(--text);
  }

  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 1.25rem;
  }

  h2 {
    font-size: 0.8rem;
    font-weight: 650;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-dim);
    margin: 0 0 1rem;
  }

  label {
    display: block;
    font-size: 0.8rem;
    font-weight: 550;
    color: var(--text-dim);
    margin-bottom: 0.35rem;
  }

  input,
  select {
    width: 100%;
    padding: 0.55rem 0.65rem;
    font: inherit;
    font-size: 0.95rem;
    color: var(--text);
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 10px;
    transition: border-color 120ms ease, box-shadow 120ms ease;
  }

  input:focus-visible,
  select:focus-visible,
  button:focus-visible {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 30%, transparent);
  }

  button {
    font: inherit;
    font-weight: 550;
    color: var(--text);
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.5rem 0.9rem;
    cursor: pointer;
    transition: background 120ms ease, border-color 120ms ease, transform 120ms ease;
  }

  button:hover {
    border-color: color-mix(in srgb, var(--accent) 50%, var(--border));
  }

  button:active {
    transform: translateY(1px);
  }

  button.primary {
    background: var(--accent);
    border-color: var(--accent);
    color: var(--accent-text);
  }

  button.ghost {
    background: transparent;
  }

  .row {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
  }

  .grid {
    display: grid;
    gap: 0.9rem;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  }

  .muted {
    color: var(--text-dim);
    font-size: 0.85rem;
  }

  .num {
    font-variant-numeric: tabular-nums;
  }

  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0 0 0 0);
    white-space: nowrap;
    border: 0;
  }
`;
