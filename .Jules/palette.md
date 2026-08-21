## 2024-08-21 - Telegram Keyboard Mobile Optimization
**Learning:** Telegram custom keyboards can take up excessive vertical space on mobile devices, and long single-column lists require excessive scrolling.
**Action:** Always set `resize_keyboard=True` for mobile optimization and chunk long single-column lists into multi-column grids (e.g., rows of 3). Ensure the keyboard array is passed as the first positional argument.
