import requests
import json
import datetime as dt


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
            print('Scryfall card data not found, downloading now')
            update = True
    if update:
        datadownload = requests.get(requests.get("https://api.scryfall.com/bulk-data").json()['data'][0]['download_uri'])
        with open(filename, 'w') as f:
            json.dump(datadownload.json(), f)
        scrydata = datadownload.json()
    return scrydata


def downloadcardimage(cardname, scryfallcarddata):
    # Download and save card images from scryfall
    for card in range(len(scryfallcarddata)):
        if scryfallcarddata[card]['name'] == cardname:
            carddata = scryfallcarddata[card]
    art_types = carddata['image_uris'].keys()
    for art_type in art_types:
        imageurl = carddata['image_uris'][art_type]
        cardimage = requests.get(imageurl)
        file = open(cardname + '_' + art_type + '.png', "wb")
        file.write(cardimage.content)
        file.close()


scryfalldata = loadcarddata()
downloadcardimage('Narcomoeba', scryfalldata)


# jprint(scrydata)

# response = requests.get("https://api.scryfall.com/bulk-data")
# something = response.json()['data'][0]['download_uri']
# scrydata = requests.get(something)
# filename = 'cardbulkdata.json'
# with open(filename, 'w') as f:
#     json.dump(scrydata.json(), f)
#
# cardname = 'Narcomoeba'
# for card in range(len(scrydata)):
#     if scrydata[card]['name'] == cardname:
#         carddata = scrydata[card]
#
# art_types = carddata['image_uris'].keys()
# for art_type in art_types:
#     imageurl = carddata['image_uris'][art_type]
#     cardimage = requests.get(imageurl)
#     file = open(cardname + '_' + art_type + '.png', "wb")
#     file.write(cardimage.content)
#     file.close()
