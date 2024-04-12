def distance(strand_a, strand_b):
    """
    Calculate the Hamming distance between two DNA strands.

    Args:
    strand_a (str): The first DNA strand.
    strand_b (str): The second DNA strand.

    Returns:
    int: The Hamming distance between the two DNA strands.
    Raises:
    ValueError: If the input strands are not of equal length.
    """
    if len(strand_a)==len(strand_b):
        count = 0
        for x in range(len(strand_a)):
            if strand_a[x]!=strand_b[x]:
                count+=1
        return count
    raise ValueError("Strands must be of equal length.")