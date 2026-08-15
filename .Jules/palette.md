## 2024-05-18 - Telegram Keyboard Optimization
**Learning:** Default Telegram custom keyboards take up the entire native device keyboard height, causing awkwardly massive buttons. Furthermore, rendering long dynamic lists (like countries or products) as single-column buttons creates an excessively long scroll that breaks the bot experience on mobile.
**Action:** Always set `resize_keyboard=True` when instantiating `ReplyKeyboardMarkup`. Always chunk dynamic flat lists into multi-column grids (e.g., 3 columns) before passing them to the keyboard to improve navigation and visual hierarchy.
