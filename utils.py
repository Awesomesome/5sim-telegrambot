# Utility functions
def format_list(items):
    return "\n".join(sorted(items))
def chunk_keyboard_list(items, chunk_size=2):
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
