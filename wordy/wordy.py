def answer(question):
    """
    A function that processes a question to perform a mathematical operation and returns the result.
    """
    words = question[0:-1].split()
    print(words,"---",question[-1]=="?")
    if words[0] != "What" or words[1] != "is" or question[-1] != "?":
        raise ValueError("unknown operation")
    try:
        int(words[2])
    except:
        raise ValueError("syntax error")
    else:
        if len(words) == 3:
            return int(words[2])
    result=int(words[2])
    operator=None
    for word in words[3:]:
        if word == "by":
            continue
        if not operator and word in ["plus","minus","multiplied","divided"]:
            operator=word
            continue
        elif not operator:
            try:
                int(word)
            except:
                raise ValueError("unknown operation")
            else:
                raise ValueError("syntax error")
        elif operator:
            try:
                int(word)
            except:
                raise ValueError("syntax error")
            else:
                if operator == "plus":
                    result+=int(word)
                elif operator == "minus":
                    result-=int(word)
                elif operator == "multiplied":
                    result*=int(word)
                elif operator == "divided":
                    result/=int(word)
        operator=None
    if operator:
        raise ValueError("syntax error")
    return int(result)