def remove_duplicates(items):
    seen = []
    for char in items:
        if char in seen:
            return False
        seen.append(char)
    return True

remove_duplicates([1, 2, 3, 3])