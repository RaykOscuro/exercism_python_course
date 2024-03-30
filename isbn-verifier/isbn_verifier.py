def is_valid(isbn):
    """
    Checks if the given ISBN is valid.

    Parameters:
        isbn (str): The ISBN to be checked.

    Returns:
        bool: True if the ISBN is valid, False otherwise.
    """
    if len(isbn)==0:
        return False 
    noHyph = list(filter(lambda x: (x != '-'),isbn[0:-1]))
    testDig = isbn[-1]
    if len(noHyph)!=9:
        return False
    notAllowed = list(filter(lambda x: (x not in "01234567890"),noHyph))
    if testDig not in "0123456789X":
        return False
    if len(notAllowed)!=0:
        return False
    if testDig == "X":
        testDig = 10
    else:
        testDig = int(testDig)
    checksum = 0
    multiply = 10
    for char in noHyph:
        checksum+=int(char)*multiply
        multiply-=1
    return (checksum + testDig) % 11 == 0