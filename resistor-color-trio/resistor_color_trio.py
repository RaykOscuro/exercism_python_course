def label(colors):
    """
    Given a list of resistor color codes, returns the resistance value and units of the resistor.
    
    Args:
    - colors (list of str): A list of three strings representing the color codes of the resistor.
    
    Returns:
    - str: A string representing the resistance value and units of the resistor.
    """
    color_mappings = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    total_value = (color_mappings[colors[0]] * 10 + color_mappings[colors[1]])*10**color_mappings[colors[2]]
    if total_value / 10**9 > 1:
        return str(int(total_value / 10**9)) + " gigaohms"
    elif total_value / 10**6 > 1:
        return str(int(total_value / 10**6)) + " megaohms"
    elif total_value / 10**3 > 1:
        return str(int(total_value / 10**3)) + " kiloohms"
    else:
        return str(total_value) + " ohms"
