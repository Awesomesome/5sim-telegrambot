## 2024-05-18 - Telegram Keyboard Optimization
**Learning:** Default Telegram custom keyboards take up too much vertical space on mobile and buttons in a single row can get truncated or look cramped.
**Action:** When modifying `ReplyKeyboardMarkup`, set `resize_keyboard=True` and organize buttons into a logical grid to improve mobile layout and usability.
