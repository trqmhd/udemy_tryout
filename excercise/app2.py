import json
import sys

data = json.load(open('dic_data.json'))

def meaning (word):
    if word in data:
        return data[word]
    else:
        print("Word doesn't exist\n")


while True:
    word = input('write your word here: \n >')
    if (word !='Q'.lower()):
        print(meaning(word.lower()))  # lower case insensitive;
        print ('For quit- PRESS "Q"')
    else:
        sys.exit()
