import re
import nltk

from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer, sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("input.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
with open('splitout.txt', 'w+') as f:
 f.flush()
for r in words:
    if not r in stop_words:
        appendFile = open('output3.txt','a')
        appendFile.write(" "+r)
        appendFile.close()

file_content = open("inputquery.txt").read()
list1 = nltk.word_tokenize(file_content)
file_content = open("output3.txt").read()
list2 = nltk.word_tokenize(file_content)
print list2
list = []
s=0
#text = open("fin_result.txt", "r")
#list2 = text.readlines()
#print(list2)
#mylst = map(lambda each:each.strip('\'), list2):
#print mylst
#sed 's/\\''//g' list2
#for x in list2():
#ist3 =x.split(". ")
#list1 = ['apple']
#list2 = ['Ship', 'copy', 'define', 'duplicate', 'find', 'how', 'identify', 'label', 'list', 'listen', 'locate', 'match', 'memorise', 'name', 'observe', 'omit', 'quote', 'read', 'recall', 'recite', 'recognise', 'record', 'relate', 'remember', 'repeat', 'reproduce', 'retell', 'select', 'show', 'spell', 'state', 'tell', 'trace', 'write']
list = []
#lines =list2.split('.')
#print lines
for x in list1:
   for word2 in list2:
	if(word2=='.' or word2== ','):
		#print list
		#list.clear()
		continue
        
        wordFromList1 = wordnet.synsets(x)
    #print wordFromList1
    
        wordFromList2 = wordnet.synsets(word2)
    #print wordFromList2
        if wordFromList1 and wordFromList2: #Thanks to @alexis' note
            s = wordFromList1[0].wup_similarity(wordFromList2[0])
        print x
        print word2
        print s    
        list.append(s)

print(max(list))

