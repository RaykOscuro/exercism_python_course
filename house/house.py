def recite(start_verse, end_verse):
    """
    Generate verses of "The House That Jack Built" starting from a given verse number to an end verse number.
    
    Parameters:
    - start_verse: int, the starting verse number
    - end_verse: int, the ending verse number
    
    Returns:
    - list of strings, verses of "The House That Jack Built" from the starting verse to the ending verse
    """
    options = [
        "This is ",
        "the horse and the hound and the horn that belonged to ",
        "the farmer sowing his corn that kept ",
        "the rooster that crowed in the morn that woke ",
        "the priest all shaven and shorn that married ",
        "the man all tattered and torn that kissed ",
        "the maiden all forlorn that milked ",
        "the cow with the crumpled horn that tossed ",
        "the dog that worried ",
        "the cat that killed ",
        "the rat that ate ",
        "the malt that lay in ",
        "the house that Jack built.",
    ]

    verses = []
    for i in range(start_verse - 1, end_verse):
        newVerse = options[0]
        for j in range(i, -1, -1):
            newVerse += options[len(options) - 1 - j]
        verses.append(newVerse)

    return verses
