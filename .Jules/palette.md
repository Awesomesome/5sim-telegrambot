## 2024-03-20 - Mobile Keyboard Layout and Emoji Handling
**Learning:** Telegram custom keyboards default to taking up a significant portion of the screen, which can be intrusive on mobile. Grouping them into grids and enabling `resize_keyboard=True` makes the UX significantly cleaner. Additionally, using `in` for text matching instead of exact equality handles edge cases like trailing spaces or future emojis added to buttons.
**Action:** Always use `resize_keyboard=True` for `ReplyKeyboardMarkup` and use substring matching for handling text commands to ensure robustness.
