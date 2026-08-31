## 2024-05-24 - [Mobile Telegram Bot Keyboards]
**Learning:** Telegram custom keyboards default to taking up maximum vertical space, causing usability issues and excessive scrolling when presenting long lists of options like countries or products.
**Action:** When implementing Telegram bots, always use `resize_keyboard=True` to allow keyboards to size dynamically, and actively format long lists into chunked grids instead of single-column lists.
