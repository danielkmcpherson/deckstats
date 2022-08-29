"""Functions to read in a decklist and assign parameters to the cards it contains"""
from api_requests import jprint, loadcarddata, getcarddata, downloadcardimage
import os
import json


def make_deck_folder(deckfilename):
    deckfoldername = deckfilename.split('.')[0]
    if not os.path.isdir(deckfoldername):
        os.mkdir(deckfoldername)
        os.mkdir(deckfoldername + '/images')
    return deckfoldername


def decklist_readin(deckfilename):

    with open(deckfilename) as f:
        lines = f.readlines()

    make_deck_folder(deckfilename)

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

    cardnums = []
    cardnames = []
    for element in sideboardlines:
        cardnums.append(element[0:element.index(' ')])
        cardnames.append(element[element.index(' ') + 1:-1])

    sideboard = []
    for x in range(len(sideboardlines)):
        for y in range(int(cardnums[x])):
            sideboard.append(cardnames[x])

    return maindeck, sideboard


def assignparams(deckfilename, cardlist, carddata):
    deckfoldername = make_deck_folder(deckfilename)
    assignedcardlist = []
    for card in cardlist:
        assignedcard = getcarddata(card, carddata)
        assignedcardlist.append(assignedcard)
    if len(assignedcardlist) == 15:
        listtype = 'sideboard'
    else:
        listtype = 'maindeck'
    filename = deckfoldername + '/' + listtype + '.json'
    with open(filename, 'w') as f:
        json.dump(assignedcardlist, f)
    return assignedcardlist


def getdeckimages(deckfilename, cardlist, carddata):
    deckfoldername = make_deck_folder(deckfilename)
    for card in cardlist:
        downloadcardimage(deckfoldername + '/images/', card, carddata)

def run(deckname):
    carddata = loadcarddata()
    maindeck, sideboard = decklist_readin(deckname)
    assignedmaindeck = assignparams(deckname, maindeck, carddata)
    assignedsideboard = assignparams(deckname, sideboard, carddata)
    getdeckimages(deckname, maindeck, carddata)
    getdeckimages(deckname, sideboard, carddata)
    return assignedmaindeck, assignedsideboard

if __name__ == '__main__':
    deckname = 'Deck - Spirits v13.txt'
    maindeck, sideboard = run(deckname)
    jprint(sideboard)
