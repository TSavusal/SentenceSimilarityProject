from sys import version_info
from sys import exit
if version_info <= (3, 0):
    print("\nUse python version 3.0 or higher. ( Code was tested with 3.5.2)")
    print("EXITING")
    exit(1)
'''
You may need to install these packages if you haven't already.
This assumes you use python 3.5.2 version.

pip3 install boto
pip install nltk
pip install matplotlib
pip install smart_open
pip install gensim
pip3 install cython
pip3 install git+git://github.com/gsi-upm/sematch.git

'''
# try:
	# from nltk.book import *
# except:
	# import nltk
	# print("You need to download the nltk book! Select it from the menu")
	# nltk.download()
import logging
from Semantic_Similarity import task3SemanticSim
from task5_file import sentenceSimilarityForTask5, task5
from task2_file import sentenceSimilarityForTask2, PartialSim, task2,get_wordnet_pos
from task4_file import task4
# ----------------------------------------------------------------
'''
#Task description:
First, you should construct your own database of sentences.
Ideally, this database should be constituted of pair of sentences.
These pair of sentences should be ordered in descending order for similarity.

#Function Description:
Function will return a list of tuples. Each unit in the list contains 2 sentences.
If you need to loop though the sentence pairs then see function task2() for an example
'''
def task1():
    sentencePairs=[]
    #1.
    sent1 = "Car is driving on the road"
    sent2 = "Car is driving on the road"
    sentencePairs.append([sent1,sent2])   #append the first sentence pair
    #2.
    sent1 = "Van is driving on the road"
    sent2 = "Car is driving on the road"
    sentencePairs.append([sent1,sent2])   #append the 2nd sentence pair
    #3.
    sent1 = "Van is travelling on the road"
    sent2 = "Car is driving on the road"
    sentencePairs.append([sent1,sent2])   #append the 2nd sentence pair
    #4. 
    sent1 = "Van is travelling on the highway"
    sent2 = "Car is driving on the road"
    sentencePairs.append([sent1,sent2])   #append the 2nd sentence pair
    #5.
    sent1 = "Van is commuting on a highway"
    sent2 = "Car is driving on the road"
    sentencePairs.append([sent1,sent2])   #append the 2nd sentence pair
    return(sentencePairs)
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def task3SemanticRunner(sentencePairs):
    for i in range(0,len(sentencePairs)):
        s1 = sentencePairs[i][0]
        s2 = sentencePairs[i][1]
        print("Similarity3 (Semantic): " + str(task3SemanticSim(s1,s2)).ljust(18) + " for sentence pair: "+ str(sentencePairs[i]))
# --------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__== "__main__":
    #Task 1: Build sentence pairs
    print("\nTask 1: Build sentence pairs -----------------------------------------------------------------------------------------------------------------")
    sentencePairs=task1()
    
    #Task 2: Calculate similarity for the sentence pairs
    print("\nTask 2: Calculate similarity ------------------------------------------------------------------------------------------")
    #similarity_method = "wupalmer_sim"
    #similarity_method = "path_sim"
    task2(sentencePairs,"path_sim")		#possible metrics: "wupalmer_sim"  or "path_sim"

    #Task 3
    print("\nTask 3: Calculate similarity for the sentence pairs ------------------------------------------------------------------------------------------")
    task3SemanticRunner(sentencePairs)

	#Task 4: Calculate similarity for the sentence pairs using YAGO
    print("\nTask 4: Calculate similarity for the sentence pairs using YAGO concepts ----------------------------------------------------------------------")
    task4(sentencePairs)

    #Task 5: Word2Vec for calculating sentence similarity. (Word2Vec)
    print("\nTask 5: Word2Vec for calculating sentence similarity -------------------------------------------------------------------------------------------")
    print("Task 5 NOTE: Building the model could take up to 60 seconds depending on the speed of your computer. Install Cython module to speed up the training.")
    task5(sentencePairs)