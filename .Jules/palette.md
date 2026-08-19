## 2024-05-25 - Telegram Custom Keyboard Optimization
**Learning:** Custom Telegram keyboards containing long single-column lists can lead to excessive scrolling and poor user experience, especially on mobile devices.
**Action:** Always set `resize_keyboard=True` to adapt the keyboard size to mobile screens, and organize long lists of options into multiple columns using a chunking utility.
