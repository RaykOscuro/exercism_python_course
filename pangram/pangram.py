def is_pangram(sentence):
    """
    Check if a given sentence is a pangram.

    Parameters:
        sentence (str): The sentence to be checked.

    Returns:
        bool: True if the sentence is a pangram, False otherwise.
    """
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in sentence.lower():
            return False
    return True
