## 2024-05-18 - Flexible Telegram Bot Keyboards
**Learning:** Telegram mobile users benefit greatly from resized keyboards (`resize_keyboard=True`), and strict string matching (like `== 'yes'`) breaks down when users append emojis or spaces to their input natively or via custom keyboards.
**Action:** Always set `resize_keyboard=True` for Telegram reply keyboards to ensure mobile optimization, and use `.startswith()` (or `Filters.text & ~Filters.command`) instead of strict regex or equality to gracefully handle inputs containing text alongside emojis.
