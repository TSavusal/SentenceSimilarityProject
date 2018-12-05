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
pip3 install cython                #Needed for task5. Gensim model training only uses 1 thread if you don't install cython.
pip install gensim                #Task 5
pip install matplotlib
pip install smart_open
conda install -c conda-forge msinttypes
pip3 install pyqt5
'''

# try:
	# from nltk.book import *
# except:
	# import nltk
	# print("You need to download the nltk book! Select it from the menu")
	# nltk.download()
from nltk.corpus import wordnet as wn
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.corpus import brown
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import logging
from Semantic_Similarity import task3SemanticSim
#nltk.download()                #This must be run before the code works!
#from nltk.book import *



#import boto3
#import gensim
#from gensim.models import Word2Vec
#gensim.models.Word2Vec
# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Convert to compatible pos tag.
nltk.pos_tag (...) is not compatible with wn.synsets(). We need to convert to a compatible form.

Based on:
https://stackoverflow.com/questions/15586721/wordnet-lemmatization-and-pos-tagging-in-python/24948797
'''
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return ''
# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Sentence similarity as was instructed in section 2 of the document.

Example usage of the function:
s1 = "Car is driving on the road"
s2 = "Car is driving on the road"
similarity_method = "wupalmer_sim"

print(sentenceSimilarityForTask2(s1,s2,similarity_method))

'''
def sentenceSimilarityForTask2(s1,s2,method):
    val1 = PartialSim(s1,s2,method)
    return(val1)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
a More complex similarity measure. The equation was given during Exercise 2. Inverse document frequency was omitted as per the advice from the instructor.

#Function for calculating similarity = 0.5 *( (0.1 +0.2 + 0.3)/3 + (0.33 + 0.44 +0.55)/3)
def sentenceSimilarity(s1,s2):
    val1 = PartialSim(s1,s2)        #Simila
    val2 = PartialSim(s2,s1)
    total_sim = 0.5*(val1 + val2)
    #print(total_sim)
    return(total_sim)
'''
# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Calculates similarity score between sent 1 and sent 2.  NOTE: The direction that you use to input the sentences makes a difference.
Input format:  str, str, str

returns the similarity value in numeric format
'''
def PartialSim(s1,s2,method):
    #Format the input sentences to desired form
    s1=s1.lower()
    s2=s2.lower()
    #Separate sentence into words. Aka list of words.
    s1_words = word_tokenize(s1)    
    s2_words = word_tokenize(s2)
    #POS tags for each word in sentence.
    pos1 = pos_tag(s1_words)
    pos2 = pos_tag(s2_words)
    #Remove stop words from the pos, tagged sentences
    pos1 = [word for word in pos1 if word[0] not in stopwords.words('english')]
    pos2 = [word for word in pos2 if word[0] not in stopwords.words('english')]
    #Calculate similarity for all words in pos1  (pos1 is a modified "s1". AKA modified sentence 1)
    s1_total=0
    count=0
    s1_sim=0    
    for a in pos1:
        word1 = str(a[0])
        pos_tag1_incompatible = str(a[1])        # get the incompatible pos tag that was received
                                                 # from nltk.pos_tag(...) function.
        pos_tag1 = get_wordnet_pos(pos_tag1_incompatible)    #converting to compatible pos tag.s
        if pos_tag1 == '':
            continue            #could not find pos tag. Let's skip this word
        #print("word1:    " + str(word1))
        #print("pos_tag1: " + pos_tag1)
        synset_a = wn.synsets(word1, pos_tag1)
        biggest_similarity=-9999999999      #Compare a word in S1 (more precisely it's synset) to every word in S2. 
                                            #The highest similarity value will be saved.
        for b in pos2:
            word2 = str(b[0])
            pos_tag2_incompatible = str(b[1])
            pos_tag2 = get_wordnet_pos(pos_tag2_incompatible)
            if pos_tag2 == '':  
                continue        #could not find pos tag. Let's skip this word
            #print("word2:    " + str(word2))
            #print("pos_tag2: " + pos_tag2)
            synset_b = wn.synsets(word2, pos_tag2)
            # loop though both synsets and find the combination where similarity is highest.
            # NOTE: here we are comparing first word from sentence 1 to all words in sentence 2.
            # The synsets that has the highest similarity will be included in the calculation.
            temp_number=0
            for c in synset_a:
                #Find the synset_b that has the highest similarity value with 
                for d in synset_b:
                    if method == "wupalmer_sim":
                        temp_number = c.wup_similarity  (d)     #Wu-Palmer similarity
                    elif method == "path_sim":
                        temp_number = c.path_similarity(d)     #Path similarity
                    if (temp_number is not None) and (temp_number > biggest_similarity):
                        biggest_similarity = temp_number
        if (biggest_similarity != -9999999999):
            count=count+1
            s1_sim=s1_sim+biggest_similarity
        else:
            print("\"biggest_similarity\" is still the default value after looping all the words. --> No similarity found.  The word in question is word1: "+str(word1))
    if(count > 0):
        s1_total=(s1_sim / count)
    else:
        s1_total = 0
    return(s1_total)
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
# ----------------------------------------------------------------
'''
#Task Description:
Next use standard wordnet semantic score. Namely, if the sentence S1 is tokenized as {a1, a2, a3} I and
sentence S2 of the pair is tokenized as {b1, b2} for example. Then the overall wordnet semantic score will be
Sim(S1, S2) =[ max(Sim(a1,b1), Sim(a1, b2)) + max(Sim(a2,b1), Sim(a2, b2)) + max(Sim(a3,b1), Sim(a3, b2)) ]/3
( In other words we compare first word in sentence S1, get it's synonym set and 
for instance in Sim(a1,b1)   we calculate simlarity between first word in S1 and first word in S2. 
in max(Sim(a1,b1), Sim(a1, b2))  we take the maximum value. AKA compare first word in S1 and find the word in S2
that has the highest similarity with the first word. Then that similarity score will be in the calculus.
e.g.   S = (0.5 + 0.6 + 0.7) /3   #Here 3 is the number of words in S1

#Function description:
Takes a list of sentencepairs as input. This list was constructed in fucntion: task1()
Prints the similarity scores for each sentence pair.
'''
def task2(sentencePairs,similarity_method):
    for i in range(0,len(sentencePairs)):
        s1 = sentencePairs[i][0]
        s2 = sentencePairs[i][1]
        print("Similarity2: " + str(sentenceSimilarityForTask2(s1,s2,similarity_method)).ljust(18) + " for sentence pair: "+ str(sentencePairs[i]))    #NOTE: ljust is used in order to format the print
# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Sentence similarity with Word2Vec model

Example usage of the function:

# 1. Create two sentences
s1 = "Car is driving on the road"
s2 = "Car is driving on the road"

# 2. Create model
#       Enable the line below if you want to show logging information during the model building
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#       Load brown corpus
sentences = brown.sents()
#       Train model with brown corpus
model = Word2Vec(sentences, min_count=1, workers=12)      #NOTE: Have Cython installed. Otherwise the number of workers will be 1. 

#Calculate similarity
print(sentenceSimilarityForTask5(s1,s2,model))

'''
def sentenceSimilarityForTask5(s1,s2,model):
    # https://stackoverflow.com/questions/27632404/how-should-i-train-gensim-on-brown-corpus
    # https://rare-technologies.com/word2vec-tutorial/
 
    s1 = s1.lower()
    s2 = s2.lower()
    s1_tokenized=word_tokenize(s1)
    s2_tokenized=word_tokenize(s2)

    # Remove stop words
    # s1_tokenized = [word for word in s1_tokenized if word not in stopwords.words('english')]
    # s2_tokenized = [word for word in s2_tokenized if word not in stopwords.words('english')]
    
    #NOTE: Stop words were not removed. Removing stop words seems to have a negative effect on the similarity scores for Word2Vec model.
    #Words at the bottom of the corpus were shown higher similarity scores than expected.

    #Stopword removal needed    --> no
    #Stemming needed            --> ?

    avg=0
    total=0
    items=0
    for a in s1_tokenized:
        for b in s2_tokenized:
            sim = model.similarity(a, b)
            #print("Similarity between words '("+str(a)+")' and '("+str(b)+")': "+str(sim))
            items=items+1
            total=total+sim
    if items>0:
        avg = total / items
    return(avg)
def task5(sentencePairs): 
    # Build Word2Vec model
    model_path = get_tmpfile("word2vec_model/browncorpus.model")
    try:
        #Load a model if it exists
        model = Word2Vec.load(model_path)
    except FileNotFoundError:
        #Enable the line below if you want to show logging information during the model building
        #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        
        #Load brown corpus
        sentences = brown.sents()
        #Train model with brown corpus
        model = Word2Vec(sentences, min_count=1, workers=12)      #NOTE: Have Cython installed. Otherwise the number of workers will be 1. 
        
        # There seems to be a problem when trying to save a gensim model.
        # There is an unresolved issue regarding this in github: https://github.com/RaRe-Technologies/gensim/issues/1129
        # Model saving is disabled due to this reason
        #model.save(model_path)

    #Evaluate sentences with the model
    for i in range(0,len(sentencePairs)):
        s1 = sentencePairs[i][0]
        s2 = sentencePairs[i][1]
        print("Similarity2: " + str(sentenceSimilarityForTask5(s1,s2,model)).ljust(18) + " for sentence pair: "+ str(sentencePairs[i]))    #NOTE: ljust is used in order to format the print
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

    #Task 5: Word2Vec for calculating sentence similarity. (Word2Vec)
    print("\nTask 5: Word2Vec for calculating sentence similarity -------------------------------------------------------------------------------------------")
    print("Task 5 NOTE: Building the model could take up to 60 seconds depending on the speed of your computer. Install Cython module to speed up the training.")
    #task5(sentencePairs)