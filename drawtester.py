import random

with open('Deck - Spirits v11.txt') as f:
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

goodhand = 0
numits = 500000
for x in range(numits):
    hand = random.sample(maindeck, 7)
    if (('Curious Obsession' in hand or 'Curiosity' in hand) and
            ('Spectral Sailor' in hand or 'Ascendant Spirit' in hand or 'Mausoleum Wanderer' in hand) and
            ('Geistlight Snare' in hand or 'Slip Out the Back' in hand or 'Spell Pierce' in hand) and
            (hand.count('Snow-Covered Island') + hand.count('Otawara, Soaring City')) >= 2):
        goodhand += 1
playopener = goodhand / numits
mulltosix = (1-playopener) * playopener + playopener
mulltofive = (1-mulltosix) * mulltosix + playopener + mulltosix

print('% in opener: ' + str(round(playopener, 5)))
print('% in mull to 6: ' + str(round(mulltosix, 5)))
print('% in mull to 5: ' + str(round(mulltofive, 5)))

# Rerun for however many and then look at the distribution around the true value
