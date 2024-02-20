def score(x, y):
    ranges = [1,5,10]
    for iter in range(0,3):
        if (x**2+y**2)**(0.5)<=ranges[iter]:
            return ranges[-(iter+1)]
    return 0
