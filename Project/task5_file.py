from nltk.corpus import brown
from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec
from nltk import word_tokenize
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
import logging
import re
import nltk
'''
Sentence similarity with Word2Vec model.

Inputs  ------------------------------------------------------------------------------
s1      sentence 1
s2      sentence 2
model   Word2Vec model

#Outputs -----------------------------------------------------------------------------
Outputs a float value that describes the similarity of the two sentences.


Example usage of the function  -------------------------------------------------------
#1. Create two sentences
s1 = "Car is driving on the road"
s2 = "Car is driving on the road"

#2.Create model
# Enable the line below if you want to show logging information during the model building
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Load brown corpus
sentences = brown.sents()
# Train model with brown corpus
model = Word2Vec(sentences, min_count=1, workers=12)      #NOTE: Have Cython installed. Otherwise the number of workers will be 1. 

#3.    Calculate similarity
print(sentenceSimilarityForTask5(s1,s2,model))

'''
def keep_allowed_chars(sentence):
    allowed = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\''
    # sentence = ''.join( c for c in sentence if c in allowed )
    sentence = ''.join( c for c in sentence if c in allowed )
    return(sentence)

def sentenceSimilarityForTask5(s1,s2,model):
    # https://stackoverflow.com/questions/27632404/how-should-i-train-gensim-on-brown-corpus
    # https://rare-technologies.com/word2vec-tutorial/
 
    #Lowercase
    s1 = s1.lower()
    s2 = s2.lower()
    
    #Strip non-alphabets
    s1 = keep_allowed_chars(s1)
    s2 = keep_allowed_chars(s2)
    
    #Tokenize
    s1_tokenized=word_tokenize(s1)
    s2_tokenized=word_tokenize(s2)

    #Stem
    # stemmer = nltk.stem.porter.PorterStemmer()
    # s1_tokenized =  [stemmer.stem(item) for item in s1_tokenized]
    # s2_tokenized =  [stemmer.stem(item) for item in s2_tokenized]

    # Remove stop words
    #s1_tokenized = [word for word in s1_tokenized if word not in stopwords.words('english')]
    #s2_tokenized = [word for word in s2_tokenized if word not in stopwords.words('english')]
    
    #NOTE: Stop words were not removed since work2Vec vector can take into account the similarity of the "a" and "the" words too.
    #Words at the bottom of the corpus were shown higher similarity scores than expected.

    #Stopword removal needed    --> no
    #Stemming needed            --> ?

    avg=0
    total=0
    items=0
    for a in s1_tokenized:
        for b in s2_tokenized:
            try:
                sim = model.similarity(a, b)
            except:
                continue
            #print("Similarity between words '("+str(a)+")' and '("+str(b)+")': "+str(sim))
            items=items+1
            total=total+sim
    if items>0:
        avg = total / items
    return(avg)
# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Description  ---------------------------------------------------------------
Function that will calculate several sentence similarities.
The results of all these will be printed.

Inputs  ---------------------------------------------------------------
sentencePairs       A list containing pairs of sentences
model               The model that will be used to evaluate the sentences.

#Outputs -----------------------------------------------------------------------------
Returns a Word2Vec model

Example usage of the function  -------------------------------------------------------
See the main section at the bottom of this file.
'''
def task5(sentencePairs,model):
    if model == None:
        print("Task 5 NOTE: Building the model could take up to 60 seconds depending on the speed of your computer. Install Cython module to speed up the training.")
        # Build Word2Vec model is its not saved to disk already.
        name_of_the_model = "word2VecModel.model"
        try:
            #Load a model if it exists
            model = KeyedVectors.load(name_of_the_model, mmap='r')
        except FileNotFoundError:
            #Enable the line below if you want to show logging information during the model building
            #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
            
            #Load brown corpus
            sentences = brown.sents()
            
            #Train model with brown corpus
            model = Word2Vec(sentences, min_count=1, workers=12)      #NOTE: Have Cython installed. Otherwise training could be slow
            # SAVE MODEL:
            # model.save(model_path)
            # There seems to be a problem when trying to save a gensim model.
            # An unresolved issue is found on github: https://github.com/RaRe-Technologies/gensim/issues/1129
            
            #Using alternative saving method for saving (found here: https://github.com/RaRe-Technologies/gensim/issues/1129#issuecomment-326728974) 
            print("Attemtpting to save model into file: "+str(name_of_the_model))
            import dill
            #Save your model
            with open(name_of_the_model,'wb') as f:
              dill.dump(model, f)
            print("The model was saved")
    #Evaluate sentences with the model
    for i in range(0,len(sentencePairs)):
        s1 = sentencePairs[i][0]
        s2 = sentencePairs[i][1]
        sim = sentenceSimilarityForTask5(s1,s2,model)
        sim = (round(sim,3))
        
        #Write to csv
        # with open('sim.csv','a') as fd:
            # my_str = str(sim) + "\n"
            # fd.write(my_str)
        
        print("Similarity: " + str(sim).ljust(5) + " for sentence pair: "+ str(sentencePairs[i]))    #NOTE: ljust is used in order to format the print
    return(model)
# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Main function. Wil be used when 'task5_file.py' is run
'''
if __name__== "__main__":
    # Download requirements	 ---------------------------------------------------------------------------------------------------------------------------------
    from task0_download_reqs import download_requirements
    download_requirements()
    # Import modules	 -------------------------------------------------------------------------------------------------------------------------------------
    from Semantic_Similarity import task3SemanticRunner
    from task1_file import task1
    #Task 1: Build sentence pairs
    print("\nTask 1: Build sentence pairs ----------------------------------------------------------------------------------------------------------------")
    sentencePairs=task1()
    #Task 5: Word2Vec for calculating sentence similarity. (Word2Vec)
    print("\nTask 5: Word2Vec for calculating sentence similarity ----------------------------------------------------------------------------------------")
    model = task5(sentencePairs,None)