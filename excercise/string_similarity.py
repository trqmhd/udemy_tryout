from nltk.corpus import wordnet
import wordnet
import synsets

list1 = ['Compare', 'require']
list2 = ['choose', 'copy', 'define', 'duplicate', 'find', 'how', 'identify', 'label', 'list', 'listen', 'locate', 'match', 'memorise', 'name', 'observe', 'omit', 'quote', 'read', 'recall', 'recite', 'recognise', 'record', 'relate', 'remember', 'repeat', 'reproduce', 'retell', 'select', 'show', 'spell', 'state', 'tell', 'trace', 'write']
list = []

for word1 in list1:
    for word2 in list2:
        wordFromList1 = wordnet.synsets(word1)[0]
        wordFromList2 = wordnet.synsets(word2)[0]
        s = wordFromList1.wup_similarity(wordFromList2)
        list.append(s)

print(max(list))
