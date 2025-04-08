from collections import defaultdict
def flatten_errors(errors):
    flattened = defaultdict(list)
    for field, error_list in errors.items():
        flattened[field].extend(error_list)
    return flattened