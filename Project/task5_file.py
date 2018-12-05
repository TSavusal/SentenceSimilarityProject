from nltk.corpus import brown
from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec
from nltk import word_tokenize
import logging
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
    
    #NOTE: Stop words were not removed since work2Vec vector can take into account the similarity of the "a" and "the" words too.
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
def task5(sentencePairs,model): 
    if model == None:
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
        sim = sentenceSimilarityForTask5(s1,s2,model)
        sim = (round(sim,3))
        print("Similarity2: " + str(sim).ljust(5) + " for sentence pair: "+ str(sentencePairs[i]))    #NOTE: ljust is used in order to format the print
    return(model)