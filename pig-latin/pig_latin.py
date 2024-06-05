def word_translate(text):
    to_move = ""
    rest = ""
    if text[0] in ["a", "e", "i", "o", "u"] or text[0:2] in ["xr", "yt"]:
        return text + "ay"
    if text[0] not in ["a", "e", "i", "o", "u"] and text[1:3] == "qu":
        return text[3 : len(text)] + text[0] + "quay"
    if text[0:2] == "qu":
        return text[2:len(text)]+"quay"
    if len(text) == 2 and text[1] == "y":
        return "y" + text[0] + "ay"
    if text[0] not in ["a", "e", "i", "o", "u"]:
        to_move += text[0]
        for x in range(1, len(text) - 1):
            if text[x] not in ["a", "e", "i", "o", "u", "y"]:
                to_move += text[x]
            else:
                rest = text[x : len(text)]
                break
    return rest + to_move + "ay"

    # for x in text:
    #     if len(to_move) == 0:
    #         to_move+=x
    #     if to_move[len(to_move)-1] in ["a","e","i","o","u"]:
    #         return
    
def translate(text):
    words = text.split()
    translated = ""
    for word in words:
        translated+=word_translate(word)+" "
    return translated[0:len(translated)-1]