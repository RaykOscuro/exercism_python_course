def resistor_label(colors):
    color_mappings = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    tolerance_mappings = {"grey": "0.05%", "violet": "0.1%", "blue": "0.25%", "green": "0.5%", "brown": "1%", "red": "2%", "gold": "5%", "silver": "10%"}
    if len(colors) == 1:
        return "0 ohms"
    elif len(colors) == 4:
        total_value = (color_mappings[colors[0]] * 10 + color_mappings[colors[1]])*10**color_mappings[colors[2]]
    else:
        total_value = (color_mappings[colors[0]] * 100 + color_mappings[colors[1]]*10 + color_mappings[colors[2]])*10**color_mappings[colors[3]]
    
    if total_value / 10**9 > 1:
        return str(total_value / 10**9).rstrip('.0') + " gigaohms ±" + tolerance_mappings[colors[len(colors)-1]]
    elif total_value / 10**6 > 1:
        return str(total_value / 10**6).rstrip('.0') + " megaohms ±" + tolerance_mappings[colors[len(colors)-1]]
    elif total_value / 10**3 > 1:
        return str(total_value / 10**3).rstrip('.0') + " kiloohms ±" + tolerance_mappings[colors[len(colors)-1]]
    else:
        return str(total_value) + " ohms ±" + tolerance_mappings[colors[len(colors)-1]]