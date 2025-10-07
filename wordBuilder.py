from varna import *

def getDevanagari(tokens):
    processedTokens = []
    l = len(tokens)
    first = tokens[0]
    next = tokens[1]
    if first in vyanjana and (next in vyanjana or next in anya):
        processedTokens.append([first, 0])
        processedTokens.append([hal, 0])
    else:
        processedTokens.append([first, 0])
    for i in range(1, l-1):
        previous = tokens[i-1]
        current = tokens[i]
        next = tokens[i+1]
        if current in svara and previous in vyanjana:
            processedTokens.append([current, 1])
        elif current in vyanjana and (next in vyanjana or next in anya):
            processedTokens.append([current, 0])
            processedTokens.append([hal, 0])
        else:
            processedTokens.append([current, 0])
    previous = tokens[-2]
    last = tokens[-1]
    if last in vyanjana:
        processedTokens.append([last, 0])
        processedTokens.append([hal, 0])
    elif last in svara and previous in vyanjana:
        processedTokens.append([last, 1])
    else:
        processedTokens.append([last, 0])
    rawCharacters = [
        tokenToDevanagariMap[i[0]][i[1]] for i in processedTokens
    ]
    characters = []
    for i in rawCharacters:
        if i != '':
            characters.append(i[0])
    word = ''.join(characters)
    return word
