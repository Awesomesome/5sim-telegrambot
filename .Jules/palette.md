## 2026-08-07 - Resize ReplyKeyboardMarkup in Telegram
**Learning:** Default Telegram custom keyboards can take up too much vertical space on mobile devices, making the chat history hard to read. Furthermore, a single row with many options is cramped and hard to tap.
**Action:** Always set `resize_keyboard=True` on `ReplyKeyboardMarkup` to ensure the keyboard height scales correctly based on the device's screen size. Additionally, logically group buttons into a grid layout (like 2x2) rather than a single long row.
