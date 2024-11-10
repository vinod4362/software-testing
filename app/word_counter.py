# app/word_counter.py
def count_words(text):
    return len(text.split())

def count_occurrences(text, char):
    return text.count(char)
