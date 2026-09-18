## 2024-05-24 - Telegram Custom Keyboard Optimization
**Learning:** Telegram custom keyboards default to full screen height on mobile devices, which is a poor UX for simple confirmations or short lists, and single-column lists require excessive scrolling.
**Action:** Always include `resize_keyboard=True` in `ReplyKeyboardMarkup` to ensure the keyboard only takes up the necessary vertical space based on button content, and use column chunking for long lists to reduce scrolling.
