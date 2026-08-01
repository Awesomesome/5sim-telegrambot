## 2024-03-21 - Optimize Telegram Keyboards for Mobile

**Learning:** Large, unresized custom keyboards (`ReplyKeyboardMarkup` without `resize_keyboard=True`) consume too much screen real estate on mobile devices, making chat history unreadable. Furthermore, strict regular expressions or exact string matching for user input handling fails when users accidentally type punctuation or emojis (e.g., 'Yes 👍' or 'yes ').

**Action:** Always initialize `ReplyKeyboardMarkup` with `resize_keyboard=True` to adapt to mobile screens. Organize buttons into logical grids (e.g., 2x2 instead of a single list). Replace strict string matching (`== 'yes'`) or regex (`Filters.regex('^(Yes|No)$')`) with `.startswith('yes')` and `Filters.text & ~Filters.command` to handle user input gracefully.
