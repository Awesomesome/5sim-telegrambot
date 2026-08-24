## 2026-08-24 - Optimize Telegram Keyboards for Mobile
**Learning:** By default, Telegram's ReplyKeyboardMarkup creates large buttons that take up maximum screen real estate, which is problematic for long lists (like countries or operators). Combining `resize_keyboard=True` with array chunking drastically improves mobile UX by keeping the chat visible and reducing scroll fatigue.
**Action:** Always set `resize_keyboard=True` when creating Telegram custom keyboards, and structure single-column lists into multi-column grids for better spatial efficiency.
