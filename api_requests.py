"""Functions to handle api calls to scryfall and manage saved scryfall data"""

import requests
import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def loadcarddata(update=False):
    # Load in scryfall carddata,
    filename = 'cardbulkdata.json'
    if not update:
        try:
            with open(filename) as f:
                scrydata = json.load(f)
                print('Scryfall card data located')
        except FileNotFoundError:
            print('Scryfall card data not found')
            update = True
    if update:
        print('Downloading Scryfall Data...')
        datadownload = requests.get(
            requests.get("https://api.scryfall.com/bulk-data").json()['data'][0]['download_uri'])
        with open(filename, 'w') as f:
            json.dump(datadownload.json(), f)
        scrydata = datadownload.json()
        print('Scryfall data downloaded')
    return scrydata


def getcarddata(cardname, scryfallcarddata):
    # Get available data on a named card
    carddata = None
    for card in range(len(scryfallcarddata)):
        if scryfallcarddata[card]['name'] == cardname:
            carddata = scryfallcarddata[card]
    if carddata is not None:
        return carddata
    else:
        print('Card ' + cardname + ' not found')
        return None


def downloadcardimage(savedirectory, cardname, scryfallcarddata, pref_size='normal'):
    # Download and save card images from scryfall
    carddata = None
    for card in range(len(scryfallcarddata)):
        if scryfallcarddata[card]['name'] == cardname:
            carddata = scryfallcarddata[card]
    if carddata is not None:
        art_types = carddata['image_uris'].keys()
        if pref_size in art_types:
            cardimage = requests.get(carddata['image_uris'][pref_size])
            cardsavename = cardname.replace(' // ', ' ')
            imgfilename = savedirectory + cardsavename + '.png'
            with open(imgfilename, "wb") as f:
                f.write(cardimage.content)
        else:
            # If selected image size is not available offer a selection of the available sizes IN PROGRESS
            print('Available image sizes: ')
    else:
        print('Card ' + cardname + ' not found')
        return None
