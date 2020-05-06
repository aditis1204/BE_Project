import io

import unicodedata
import re
import nltk

from nltk.corpus import wordnet

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer, sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.
#stop_words = set(stopwords.words('english'))
#file1 = open("input.txt")
#line = file1.read()# Use this to read file content as a stream:
#words = line.split()
#clearFile=open('filteredtext.txt','rw+')
#clearFile.truncate(0)
#clearFile.close()


def title_score(sentence,query):
    #print("query from function")
    #print(query)
    list2 = nltk.word_tokenize(query)
    #print(list2)
   # for r in words:
    #    if not r in stop_words: 
     #       appendFile = open('filteredtext.txt','a')
      #      appendFile.write(" "+r)
       #     appendFile.close()
    #text=open("filteredtext.txt").read()
    #text=unicode(text,'utf=8')
    #ps=PorterStemmer()
    #sent_text = nltk.sent_tokenize(text) # this gives us a list of sentence
    # now loop over each sentence and tokenize it separately
    flag=0
    #print("Print from function")
    #print(query)
    #file_content = open("inputquery.txt").read()
    #list1 = nltk.word_tokenize(query)
    #print("from function")
    #print(sentences)
    s=0
    temp=0
    score_matrix = []
    no_of_words=0
    score = 0

    #for sentence in sent_text:
    no_of_words=0
    leng = len(sentence)
    leng1 = len(list2)
    #print(leng1)
    final_leng = leng * leng1
     #tagged = nltk.pos_tag(sentence)
    #for word in tagged:            
        #tag=wo]
        #if (tag=='VERB'): 
         #sentence.remove(tagged(0))
    #print(sentence)
    #tokenized_text = nltk.word_tokenize(sentence)
    for x in list2:
     for y in sentence:
         #print(x)      
         wordFromList1 = wordnet.synsets(x)
         wordFromList2 = wordnet.synsets(y) 
         if wordFromList1 and wordFromList2:
            s = wordFromList1[0].wup_similarity(wordFromList2[0])  
         score_matrix.append(s)
    #print(score_matrix)
    for n, i in enumerate(score_matrix):
      if i == None:
         score_matrix[n]=0
    #list(filter(lambda a: a != "None" , score_matrix))    
    #print(score_matrix)
    for num in score_matrix:
      temp+=num
    temp = temp/final_leng
    score_matrix.clear()
    #print("final title score")
    #print(temp)
    return temp
     



