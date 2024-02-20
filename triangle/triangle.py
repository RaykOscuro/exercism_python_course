def isTriangle(sides):
    [a,b,c]=sides
    if a>0 and b>0 and c>0 and a+b>=c and a+c>=b and b+c>=a:
        return True
    return False

def equilateral(sides):
    [a,b,c]=sides
    if isTriangle(sides) and a==b and a==c:
        return True
    return False


def isosceles(sides):
    [a,b,c]=sides
    if isTriangle(sides) and (a==b or b==c or a==c):
        return True
    return False


def scalene(sides):
    if isTriangle(sides) and not isosceles(sides):
        return True
    return False
