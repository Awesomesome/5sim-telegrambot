# Utility functions
def format_list(items):
    return "\n".join(sorted(items))

def chunk_list(lst, chunk_size):
    """Chunks a list into a list of lists, useful for keyboard layouts."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
