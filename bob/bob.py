import re

def only_uppercase(hey_bob):
    found = False
    for chara in hey_bob:
        if re.match(r"[a-z]",chara):
            return False
        if re.match(r"[A-Z]",chara):
            found = True
    return found

def response(hey_bob):
    if hey_bob.strip()=="":
        return "Fine. Be that way!"
    if only_uppercase(hey_bob.strip()[0:len(hey_bob.strip())-1]) and (hey_bob.strip()[-1]=="?"):
        return "Calm down, I know what I'm doing!"
    if only_uppercase(hey_bob.strip()):
        return "Whoa, chill out!"
    if hey_bob.strip()[-1]=="?":
        return "Sure."
    return "Whatever."
    
print(only_uppercase("AAA!A!"))