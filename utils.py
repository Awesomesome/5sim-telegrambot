# Utility functions
def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def format_list(items):
    return "\n".join(sorted(items))