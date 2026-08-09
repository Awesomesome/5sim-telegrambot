## 2024-05-19 - Keyboard Mobile Optimization and Permissive Matching
**Learning:** In Telegram bots, default `ReplyKeyboardMarkup` settings create oversized, clunky buttons on mobile devices. Additionally, strict regex matching for user input breaks when users append emojis (e.g. "Yes 👍"), a common behavior on mobile.
**Action:** Always set `resize_keyboard=True` to adapt keyboards to mobile screens and use `Filters.text & ~Filters.command` combined with string methods like `.startswith()` for resilient text input parsing.
