def find(sorted_list, target):
    """
    Binary search for the target in a sorted list.

    Args:
        sorted_list (list): A sorted list of elements.
        target (int): The target value to search for.

    Returns:
        int: The index of the target value in the list.

    Raises:
        ValueError: If the target value is not in the list.
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == target:
            return mid

        if sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError("value not in array")
