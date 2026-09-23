## 2024-03-20 - Telegram Keyboard Mobile Optimization
**Learning:** Telegram custom keyboards can easily become unwieldy on mobile devices if they contain long single-column lists or lack the `resize_keyboard=True` parameter, which forces users to scroll excessively and takes up too much vertical screen real estate.
**Action:** Always organize dynamically generated list items (like countries, products, and operators) into multi-column grids (using a helper like `chunk_list`), and universally apply `resize_keyboard=True` to all `ReplyKeyboardMarkup` instances for better mobile responsiveness.
