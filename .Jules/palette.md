## 2024-05-18 - Mobile Optimized Telegram Keyboards
**Learning:** Telegram default `ReplyKeyboardMarkup`s are notoriously large on mobile devices and single column lists require a lot of scrolling. Adding emojis to button labels breaks exact string matching.
**Action:** Always set `resize_keyboard=True` to save screen space, format buttons into a logical grid (e.g., 2 columns), and validate input using the `in` operator (e.g. `'keyword' in user_choice`) to gracefully accommodate emojis in button texts.
