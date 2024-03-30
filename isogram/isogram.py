def is_isogram(sentence):
    """
    Determines if a given sentence is an isogram.

    Parameters:
    sentence (str): The sentence to check for isogram.

    Returns:
    bool: True if the sentence is an isogram, False otherwise.
    """
    used_letters = set()
    for char in sentence.lower():
        if char.isalpha() and char not in used_letters:
            used_letters.add(char)
        elif char in " -":
            continue
        else:
            return False
    return True
