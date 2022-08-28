"""Functions to read in a decklist and assign parameters to the cards it contains"""

def decklist_readin(deckfilename):

    with open(deckfilename) as f:
        lines = f.readlines()

    maindecklines = lines[0:lines.index('\n')]
    sideboardlines = lines[lines.index('\n') + 1:]

    cardnums = []
    cardnames = []
    for element in maindecklines:
        cardnums.append(element[0:element.index(' ')])
        cardnames.append(element[element.index(' ') + 1:-1])

    maindeck = []
    for x in range(len(maindecklines)):
        for y in range(int(cardnums[x])):
            maindeck.append(cardnames[x])

def assignparams