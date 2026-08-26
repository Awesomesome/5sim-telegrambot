## 2024-05-15 - Telegram Mobile Keyboard Optimization
**Learning:** `ReplyKeyboardMarkup` buttons in Telegram without `resize_keyboard=True` will appear unnecessarily tall on mobile displays, reducing available screen space for messages. Long single-column lists in dynamic keyboard arrays (e.g., countries, products) can cause infinite scroll fatigue.
**Action:** Always set `resize_keyboard=True` for Telegram keyboards to ensure mobile optimization, and use a `chunk_list` helper to split long lists into multi-column grids for better UI layout.
