## 2024-08-06 - Telegram Keyboard UX & Input Robustness
**Learning:** Telegram mobile users benefit greatly from `resize_keyboard=True` to prevent keyboards from taking up excessive screen space. Additionally, strict regex matching for `ConversationHandler` filters fails when users insert emojis or trailing spaces along with their choice.
**Action:** Use logical 2x2 grids for mobile optimization, always set `resize_keyboard=True` for `ReplyKeyboardMarkup`, and use `.startswith()` in combination with `Filters.text & ~Filters.command` instead of exact matching to support text with emojis.
