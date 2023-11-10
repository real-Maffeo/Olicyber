
data = "fmcj{yo_ackyzb_ihruvcvjam}"
special = '}{_'

def decrypt(data):
    result = ""
    toAdd = ""
    for i in range (0 , len(data)): 
        toAdd = data[i]
        if data[i] not in special:
            toAdd = chr((ord(data[i])-i - ord('a'))%26 + ord('a'))
        result += toAdd
    return result

print(decrypt(data))