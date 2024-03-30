def value(colors):
    """
    Calculate the resistance value based on the color bands provided in the 'colors' parameter.
    """
    color_mappings = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    return color_mappings[colors[0]] * 10 + color_mappings[colors[1]]
