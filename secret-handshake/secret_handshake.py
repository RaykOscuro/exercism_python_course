def commands(binary_str):
    """
    A function that generates a secret handshake sequence based on a binary string input.
    Takes in a binary string as input and returns a list of actions for the secret handshake.
    """
    handshake=[]
    if binary_str[4]=='1': handshake.append('wink')
    if binary_str[3]=='1': handshake.append('double blink')
    if binary_str[2]=='1': handshake.append('close your eyes')
    if binary_str[1]=='1': handshake.append('jump')
    if binary_str[0]=='1': handshake.reverse()
    return handshake
