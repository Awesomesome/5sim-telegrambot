# Utility functions
def format_list(items):
    return "\n".join(sorted(items))

def chunk_list(lst, chunk_size):
    """Yield successive chunk_size-sized chunks from lst."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]