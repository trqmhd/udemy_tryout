import json
import sys
import difflib
from difflib import get_close_matches


data = json.load(open('data.json'))

def meaning (word):
    if word in data:
        return data[word]

    #elif word.title() in data:
        #return data[word.title()]

    elif len(get_close_matches(word,data.keys()))>0:
        answer= input(("Did you mean %s instead, if Yes press Y otherwise N: " %(get_close_matches(word,data.keys())[0])))
        answer = answer.lower()

        if answer =="y":
            return data[get_close_matches(word,data.keys(), cutoff=0.3)[1]]

        elif answer == 'n':
            return "The word doesn't exist."

        else:
            return "Don't know what you are saying."

    else:
        return("Words doesn't exist")


while True:
    word = input("For quit press:Q\nwrite your word here: \n > ")
    word = word.lower()
    if word == "q":
        sys.exit()
#word_meaning = get_close_matches(word,data.keys())[0]
    else:
        output = meaning (word)
# lower case insensitive;
#print ('For quit- PRESS "Q"')
        if type(output) == list:
            for item in output:
                print (item)
        else:
            print (output)
