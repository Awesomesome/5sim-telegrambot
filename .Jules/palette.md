## 2024-05-24 - Defensive UX and Emoji Resilience in Bots
**Learning:** Strict text matching for Telegram buttons (like Yes/No) breaks when users append emojis. Additionally, destructive actions need defensive placement to prevent accidental taps.
**Action:** Refactored handlers to use `.lower().startswith()` for graceful degradation, replaced strict regex filters with `Filters.text & ~Filters.command`, and enforced `['No', 'Yes']` ordering for confirmations.

## 2024-05-24 - Mobile Keyboard Optimization
**Learning:** Single-column list keyboards on Telegram cause excessive scrolling and poor scannability on mobile devices.
**Action:** Introduced `chunk_list` to format long single-column lists into multi-column grids and enabled `resize_keyboard=True` globally on `ReplyKeyboardMarkup`.