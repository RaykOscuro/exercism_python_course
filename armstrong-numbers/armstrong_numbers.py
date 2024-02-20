def is_armstrong_number(number):
    calc_res = 0
    for dig in str(number):
        calc_res+=int(dig)**len(str(number))
    if calc_res == number:
        return True
    return False
