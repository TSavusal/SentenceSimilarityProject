import re
import math
import numpy as np
from itertools import chain
from collections import Counter
import nltk
from nltk.util import ngrams

NGRAM = 4

"""re_stripper_alpha = re.compile('[^a-zA-Z]+')
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')"""

def get_tuples_nosentences(txt):
    """Get tuples that ignores all punctuation (including sentences)."""
    re_stripper_alpha = re.compile('[^a-zA-Z]+')
    if not txt: return None
    ng = ngrams(re_stripper_alpha.sub(' ', txt).split(), NGRAM)
    return list(ng)

def get_tuples_nltk_punkt_sentences(txt):
    """Get tuples."""
    re_stripper_alpha = re.compile('[^a-zA-Z]+')
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    if not txt: return None
    sentences = (re_stripper_alpha.split(x) for x in sent_detector.tokenize(txt) if x)
    # Need to filter X because of empty 'words' from punctuation split
    ng = (ngrams(filter(None, x), NGRAM) for x in sentences if len(x) >= NGRAM)
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

def task3NgramSim(sent1,sent2):
	print(sent1)
	_ = get_tuples_nltk_punkt_sentences(sent1);print("Number of N-grams (first sentence):", len(_));_
	print(sent2)
	_ = get_tuples_nltk_punkt_sentences(sent2);print("Number of N-grams (second sentence):", len(_));_

	a = get_tuples_nosentences(sent1)
	b = get_tuples_nosentences(sent2)
	"""print("Ngram distance: {}".format(cosine_similarity_ngrams(a, b)))"""
	return cosine_similarity_ngrams(a, b)
	
def intro():
	print("Ngram similarity between two sentences\n")
	"""sent = raw_input("Enter the two sentences to compare similarity, split with a punctuation point: ")"""
	sent_one = raw_input("Enter the first sentence to compare similarity : ")
	sent_two = raw_input("Enter the second sentence to compare similarity : ")
	print("Calculating...\n")
	prob_sim_sent = task3NgramSim(sent_one,sent_two)
	
if __name__ == "__main__":  
    print("-------------------Ngram Similarity--------------------------")
    intro()
    print("Want to try once again? If yes enter 1, if not enter 0 : ")
    againtry = int(input())
    while(againtry == 1):
        intro()
        print("Want to try once again? If yes enter 1, if not enter 0 : ")
        againtry = int(input())