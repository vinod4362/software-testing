# app/character_frequency.py

def character_frequency(text):
    """Returns a dictionary with the frequency of each character in the text."""
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency