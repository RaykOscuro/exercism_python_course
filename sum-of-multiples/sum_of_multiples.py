def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples within the specified limit for the given list of multiples.
    """
    multipled_multiples = set()
    for item in multiples:
        multi = item
        if item != 0:
            while multi < limit:
                multipled_multiples.add(multi)
                multi += item
    return sum(multipled_multiples)
