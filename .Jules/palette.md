## 2024-05-24 - Telegram Custom Keyboard Optimization
**Learning:** Telegram custom keyboards (`ReplyKeyboardMarkup`) can take up too much vertical space on mobile devices if buttons are stacked linearly and not resized. Emojis add visual appeal but require careful string handling.
**Action:** Always use `resize_keyboard=True` for better mobile UX, group buttons logically into rows and columns (e.g., a 2x2 grid instead of a 1x4 list), and use the `in` operator (e.g., `'text' in input`) when matching text to accommodate added emojis without breaking functionality.
