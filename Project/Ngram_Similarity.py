import re
import math
import numpy as np
from itertools import chain
from collections import Counter
import nltk
from nltk.util import ngrams
from sys import warnoptions as sys_warnoptions
from warnings import simplefilter as warnings_simplefilter
if not sys_warnoptions:     #Hide warnings from sklearn package
    warnings_simplefilter("ignore")

#NGRAM = 4

"""re_stripper_alpha = re.compile('[^a-zA-Z]+')
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')"""

def get_tuples_nosentences(txt,ngramLen):
    """Get tuples that ignores all punctuation (including sentences)."""
    re_stripper_alpha = re.compile('[^a-zA-Z]+')
    if not txt: return None
    ng = ngrams(re_stripper_alpha.sub(' ', txt).split(), ngramLen)
    return list(ng)

def get_tuples_nltk_punkt_sentences(txt,ngramLen):
    """Get tuples."""
    re_stripper_alpha = re.compile('[^a-zA-Z]+')
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    if not txt: return None
    sentences = (re_stripper_alpha.split(x) for x in sent_detector.tokenize(txt) if x)
    # Need to filter X because of empty 'words' from punctuation split
    ng = (ngrams(filter(None, x), ngramLen) for x in sentences if len(x) >= ngramLen)
    return list(chain(*ng))

def cosine_similarity_ngrams(a, b):
    vec1 = Counter(a)
    vec2 = Counter(b)
    
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    return float(numerator) / denominator

def task3NgramSimRunner(sentencePairs,ngramLen):
    for i in range(0,len(sentencePairs)):
        s1 = sentencePairs[i][0]
        s2 = sentencePairs[i][1]
        sim = task3NgramSim(s1,s2,ngramLen)
        sim = (round(sim,3))
        print("Similarity (N-GRAM): " + str(sim).ljust(5) + " for sentence pair: "+ str(sentencePairs[i]))
def task3NgramSim(sent1,sent2,ngramLen):
	#print(sent1)
	_ = get_tuples_nltk_punkt_sentences(sent1,ngramLen);#print("Number of N-grams (first sentence):", len(_));_
	#print(sent2)
	_ = get_tuples_nltk_punkt_sentences(sent2,ngramLen);#print("Number of N-grams (second sentence):", len(_));_

	a = get_tuples_nosentences(sent1,ngramLen)
	b = get_tuples_nosentences(sent2,ngramLen)
	"""print("Ngram distance: {}".format(cosine_similarity_ngrams(a, b)))"""
	return cosine_similarity_ngrams(a, b)
	
def intro():
    print("Ngram similarity between two sentences\n")
    """sent = input("Enter the two sentences to compare similarity, split with a punctuation point: ")"""
    sent_one = input("Enter the first sentence to compare similarity : ")
    sent_two = input("Enter the second sentence to compare similarity : ")
    print("Calculating...\n")
    ngramLen = 1
    prob_sim_sent = task3NgramSim(sent_one,sent_two,ngramLen)
    print("N-GRAM Similarity: "+str(prob_sim_sent))

if __name__ == "__main__":  
    print("-------------------Ngram Similarity--------------------------")
    intro()
    print("Want to try once again? If yes enter 1, if not enter 0 : ")
    againtry = int(input())
    while(againtry == 1):
        intro()
        print("Want to try once again? If yes enter 1, if not enter 0 : ")
        againtry = int(input())