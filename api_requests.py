import requests
import json
import datetime as dt

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def loadcarddata(update=None):
    # Load in scryfall carddata
    filename = 'cardbulkdata.json'
    if update == None:
        with open(filename) as f:
            scrydata = json.load(f)
    print(scrydata)
    return scrydata

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