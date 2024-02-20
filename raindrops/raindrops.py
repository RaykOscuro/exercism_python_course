def convert(number):
    result = ""
    numbers=[3,5,7]
    appendi=["Pling","Plang","Plong"]
    for iter in range(0,3):
        if number%numbers[iter]==0:
            result+=appendi[iter]
    if result == "":
        return str(number)
    return result
    