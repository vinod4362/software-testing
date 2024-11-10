# app/string_merger.py
def merge_strings(s1, s2):
    merged = ''.join(a + b for a, b in zip(s1, s2))
    merged += s1[len(s2):] + s2[len(s1):]  # Add any remaining characters
    return merged
