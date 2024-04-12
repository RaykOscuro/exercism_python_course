def flatten(iterable):
    """
    Recursive function to flatten an iterable object.
    
    Args:
        iterable: An iterable object that may contain nested iterables.
        
    Returns:
        list: A flattened list containing all the elements from the input iterable.
    """
    flat_list = []
    for item in iterable:
        if hasattr(item, "__len__"):
            flat_list += flatten(item)
        elif item != None:
            flat_list.append(item)
    return flat_list
