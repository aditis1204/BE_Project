from __future__ import division
from PreProcess import doPreProcessing
from VectorSpaceModel import convertToVSM
from TF_ISF import calcMeanTF_ISF
#from tRank import modifiedSummarizer
from wordNet import wordNetFeature
from nltk import pos_tag
from importlib import reload
from title import title_score

from unn import rem_unn
import numpy as np
import sys
import csv
import random
import math
import nltk.data
from importlib import reload
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 
#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 

# Feature Vector -
# Features - [ Mean_TF_ISF, Sentence Length,  Sentence Position,   textRank,   ProperNouns ,    Numerical Data,   Wordnet        ]
# Indexes  - [     0      ,        1       ,          2        ,   3       ,   4           ,     5            ,      6        ]
finalscore = {}
without_reranking = []
leng = 0
def extractFeatures(ip_doc,query,file_name):
    #print(ip_doc)
    sentences, lengths, sentencesWithoutStemming,sent_text = doPreProcessing(ip_doc)
    #sentences1, lengths1, sentencesWithoutStemming1,sent_text1 = doPreProcessing(query)
    #print(sentences1)
    #print(sentencesWithoutStemming)
    #print(sentences)#
    sentences_len = len(sentences)
    maxlen = max(lengths)
    VSM = convertToVSM(sentences)
    VSM_deepCopy=VSM[:]
    #summarizer = modifiedSummarizer()
    #sentenceRanks=summarizer.summarize(VSM_deepCopy,1,None,"english",False,True)
    wordNetWeights = wordNetFeature(ip_doc)
    featureVectors = []
    sum = []
    final = 0
    for i in range(sentences_len):
        if lengths[i] != 0:     
            fVect = []
            fadd = []

            #TF-ISF
            fVect.append(calcMeanTF_ISF(VSM, i))
            		

            #Sentence Length
            fVect.append(lengths[i]*1.0/maxlen)
            
            #Sentence Position
            if i <= sentences_len/2:
                fVect.append(0.9 - 1.6*i/sentences_len)
            else:
                fVect.append(0.1 + 1.6*(min([i-sentences_len/2, sentences_len/2]))/sentences_len)
            #non-essential
            fVect.append(rem_unn(sentences[i]))
            #title similarity
            fVect.append(title_score(sentences[i],query))


            #fVect.append(sentenceRanks[i])
            #print(sentenceRanks[i])



            #Proper nouns
            for j in sentences:
             tagged_sent = nltk.pos_tag(j)
             #print(tagged_sent)
            if len(tagged_sent) != 0:
                fVect.append(len([word for word, tag in tagged_sent if (tag == "JJ" or tag == "NN")])/len(tagged_sent))
            else:
                fVect.append(0)
            #fVect.append(0.40)

            #Numerical Data
            #nnd = len([nd for nd in sentences[i] if nd.translate(str.maketrans('','','.,%').isdigit())])
            #fVect.append(nnd/lengths[i])
            #fVect.append(0.50)
             #Wordnet
            fVect.append(wordNetWeights[i])
            #print(fVect)
            temp=0
            for num in fVect:
             temp+=num
            sum.append(temp)
            


            #print(sum)
            #if sum > 2.80:
             #print(sum)
             #print(sent_text[i])
            
  
        
        else:
            fVect = [0, 0, 0, 0, 0, 0, 0]    
         
        featureVectors.append(fVect)
    print("Score matrix for each sentence: ")     
    print(featureVectors)
    print("Total score for each sentence")
    print(sum)
    #print("Final Sum")
    for num in sum:
      final+=num
    #print(leng)
    #print(final)

    finalscore[file_name] = (final/sentences_len) 
    without_reranking.append(file_name)
    without_reranking.append(final/sentences_len)  
    print("Summarized Text: ") 
    cnt=0
    f=0
    threshold = np.mean(sum)
    for t in sum:
       
       if t > threshold:
             #print(t)
             print(sent_text[cnt])
             f+=1
             #print(len(featureVectors))
       cnt+=1
    print("Lenth of the summarized text = ")
    print(f)
    return featureVectors




def main(a1,a2,a3,a4,a5,a6):
	
	#if(len(sys.argv) != 7 ):
	#	print ("Please provide proper arguments... python giveSummary.py <path_to_the_input_doc> ")
	#	print(len(sys.argv))
	#	print(sys.argv)
	#	return
	input_full_doc = []
	query = [] 
	print(a1,a2,a3,a4,a5,a6)
	newlist = []
	input_full_doc.append(a1)
	input_full_doc.append(a2)
	input_full_doc.append(a3)
	input_full_doc.append(a4)
	input_full_doc.append(a5)
	query = a6
	#print(query)
	#print(input_full_doc)
	try:
			#f1 = open("/home/mohan/Desktop/BE/twitter_input.txt","r") 
			f1 = open(query,"r")
	except Exception in e:
			print ("--- Could not access the the input file ---")
			# print e
			return
	full_doc1 = f1.read()
	full_doc_lines1 = tokenizer.tokenize(full_doc1)
	full_doc_lines1 = [a.replace('.','') for a in full_doc_lines1]
	#print("from main")
	#print(full_doc_lines1)
	

	
	for t in input_full_doc:

		try:
			#f1 = open("/home/mohan/Desktop/BE/twitter_input.txt","r") 
			f1 = open(t,"r")

			#inputVectors = loadCsv(input_vector_file)
		except Exception in e:
			print ("--- Could not access the the input file ---")
			# print e
			return
		full_doc = f1.read()
		#print("Full Document: ")
		#print(full_doc)
		full_doc_lines = tokenizer.tokenize(full_doc)
		full_doc_lines = [a.replace('.','') for a in full_doc_lines]

		#full_doc_lines = filter(lambda a: a.strip() != ".", full_doc_lines)
		#print("Text after Preprocessing = ")
		#print(full_doc_lines)
		print ("Length of the document= ")
		leng = len(full_doc_lines)
		#print(leng)
		print(len(full_doc_lines))
		finalscore[t] = 0
		inputVectors = extractFeatures(full_doc,full_doc1,t)
	print("without sorting")
	print(without_reranking)
	
	print("After reranking")
	print(sorted(finalscore.items(), key= lambda x:x[1], reverse=True))
	          
	

#main(a1,a2,a3,a4,a5,a6)

#if __name__ == "__main__":
 #   main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
