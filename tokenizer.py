from varna import *

def getTokens(devanagariStr):
    rawTokens = []
    for c in devanagariStr:
        if c in devanagariToTokenMap:
            rawTokens.append(devanagariToTokenMap[c])
        else:
            continue
    tokens = []
    l = len(rawTokens)
    for i in range(l-1):
        current = rawTokens[i]
        next = rawTokens[i+1]
        if current == hal:
            continue
        elif current in vyanjana and next in vyanjana:
            tokens.append(current)
            tokens.append(a)
        else:
            tokens.append(current)
    last = rawTokens[-1]
    if last == hal:
        pass
    elif last in vyanjana:
        tokens.append(last)
        tokens.append(a)
    else:
        tokens.append(last)
    return tokens
