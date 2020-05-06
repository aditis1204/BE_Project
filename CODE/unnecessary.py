import io
import nltk
import unicodedata
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer, sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def normalized(number):
    if number<1: return 1
    elif 1<=number<3: return 0.9
    elif 3<=number<5: return 0.8
    elif 5<=number<7: return 0.6    
    elif 7<=number<10: return 0.4
    elif 10<=number: return 0.2
#word_tokenize accepts a string as an input, not a file.
def useless(input):
  stop_words = set(stopwords.words('english'))
  file1 = open(input,'r')
  line = file1.read()# Use this to read file content as a stream:
  words = line.split()
  clearFile=open('filteredtext.txt','rw+')
  clearFile.truncate(0)
  clearFile.close()

  for r in words:
      if not r in stop_words:
          appendFile = open('filteredtext.txt','a')
          appendFile.write(" "+r)
          appendFile.close()
  text=open("filteredtext.txt").read()
  text=unicode(text,'utf=8')
  ps=PorterStemmer()
  sent_text = nltk.sent_tokenize(text) # this gives us a list of sentence
  # now loop over each sentence and tokenize it separately
  flag=0
  cnt=0
  no_of_words=0
  score=[]
  for sentence in sent_text:
      no_of_words=0
      tokenized_text = nltk.word_tokenize(sentence)
      tagged = nltk.pos_tag(tokenized_text)
      for word in tagged:            
              tag=word[1]
              if (tag=='CC' or tag=='DT' or tag=='IN' or tag=='WDT' or tag=='WP' or tag=='WRB' or tag=='RB' or tag=='RBR' or tag=='RBS' or tag=='RP'):
                 flag=1
                 no_of_words+=1

      print (no_of_words)           
      if flag==1:
       score.append(normalized(no_of_words))
       print(sentence)
       flag=0
      else :
       score.append(normalized(no_of_words))
      cnt+=1
  return(score)           
      

