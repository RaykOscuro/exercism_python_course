def color_code(color):
    """
    Returns the numerical value corresponding to the given color string.

    Parameters:
        color (str): The color string to be converted to its numerical value.

    Returns:
        int: The numerical value corresponding to the given color string.
    """
    color_mappings = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    return color_mappings[color]



def colors():
    """Return a list of valid color codes."""
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
