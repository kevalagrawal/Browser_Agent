# Browser Agent (Playwright + Bing Automation)

This folder contains a simple browser automation project built with Python and Playwright.
It logs into a Microsoft account once, saves session state, and then runs repeated Bing searches using randomized queries.

## Folder Contents

- `authenticate.py`: One-time login helper that saves an authenticated browser session to `ms_session.json`.
- `main.py`: Runs automated Bing searches using the saved session.
- `ms_session.json`: Saved browser storage state (generated after authentication).
- `.gitignore`: Excludes local virtual environment and session file from version control.

## What The Scripts Do

### `authenticate.py`

1. Launches Chromium in non-headless mode.
2. Opens `https://www.bing.com`.
3. Waits for you to manually sign in to your Microsoft account.
4. Saves session/cookies/local storage to `ms_session.json`.

Use this when setting up for the first time or when your session expires.

### `main.py`

1. Tries to load `ms_session.json`.
2. If the session file is missing, it asks for manual login and creates the session file.
3. Generates unique random search queries from:
   - subjects
   - keywords
   - modifiers
4. Runs `NUM_SEARCHES` iterations (default: `30`).
5. For each iteration:
   - Opens a new Bing tab.
   - Types a query with a human-like delay.
   - Presses Enter and waits for network idle.
   - Waits a random time to simulate viewing results.
   - Closes the previous tab.

## Prerequisites

- Python 3.9+
- pip
- Playwright for Python
- Playwright browser binaries (Chromium)

## Setup

From this folder, run:

```bash
python -m venv venv
venv\Scripts\activate
pip install playwright
playwright install chromium
```

If `playwright` command is not found, use:

```bash
python -m playwright install chromium
```

## Usage

### 1. Authenticate (first time)

```bash
python authenticate.py
```

Then:

1. Sign in to Microsoft in the opened browser window.
2. Return to terminal and press Enter.
3. Confirm `ms_session.json` is created.

### 2. Run automated searches

```bash
python main.py
```

The browser opens visibly (`headless=False`) and performs multiple searches.

## Configuration

Edit constants in `main.py`:

- `SESSION_FILE`: Name/path of the session state file.
- `NUM_SEARCHES`: Number of searches to perform.
- `subjects`, `keywords`, `modifiers`: Query building pools.

Example:

```python
NUM_SEARCHES = 10
```

## Session Notes

- `ms_session.json` contains sensitive auth/session data.
- Do not commit this file.
- Re-run `authenticate.py` if login expires.

## Troubleshooting

- Session not loading:
  - Delete `ms_session.json` and run `python authenticate.py` again.
- Browser does not open:
  - Ensure Playwright Chromium is installed (`python -m playwright install chromium`).
- Search input not found or page load failures:
  - Retry after checking internet connectivity.
  - Increase wait time/timeout values in `main.py` if needed.

## Security And Responsible Use

- Use this project only on accounts and services you are authorized to automate.
- Respect platform terms of service and rate limits.
- Keep automation volume reasonable to avoid abuse detection.
