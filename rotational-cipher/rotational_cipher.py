def rotate(text, key):
    """
    Rotate the characters in the input text by a certain key value.
    
    Parameters:
    text (str): The text to be rotated.
    key (int): The key value to rotate the characters by.
    
    Returns:
    str: The rotated text.
    """
    charbase_l="abcdefghijklmnopqrstuvwxyz"
    charbase_u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cypher=""
    for char in text:
        if char in charbase_l:
            cypher+=charbase_l[(charbase_l.index(char)+key)%26]
        elif char in charbase_u:
            cypher+=charbase_u[(charbase_u.index(char)+key)%26]
        else:
            cypher+=char
    return cypher