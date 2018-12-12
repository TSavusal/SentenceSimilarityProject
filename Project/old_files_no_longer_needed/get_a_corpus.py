from nltk.corpus import brown
from nltk.corpus import stopwords
from Ngram_Similarity import ngrams
from nltk import word_tokenize
from nltk import FreqDist
from nltk.stem.porter import PorterStemmer
import time
'''
Load brown corpus into a list

Inputs  ------------------------------------------------------------------------------
None

#Outputs -----------------------------------------------------------------------------
List of words. Stopwords are removed.

#Example -----------------------------------------------------------------------------
#Create wordlist where stopwords are removed
word_list = get_brown_corpus()

#Bonus:
#calculate frequency distribution of all words
fdist = FreqDist(word_list)
print(fdist.most_common(500))

'''
def get_brown_corpus():
    stemmer = PorterStemmer()
    custom_stopwords = []
    my_stopwords = stopwords.words('english') + custom_stopwords
    #stemmer = PorterStemmer()
    word_list=[]
    start = time.time()
    for word in brown.words():
        #At Least one alphabet must be found in the word. Otherwise it's not a word.
        if not any(c.isalpha() for c in word):
            continue
            
        #Remove numbers     ( Section disabled since the section above already takes care of removing numbers)
        # if word.isnumeric():
            # continue
            
        #Lowercase
        word = word.lower()
        
        #Stem
        word = stemmer.stem(word)
        
        #Remove Stopwords  (Has to be checked AFTER lowercasing & stemming)
        if word in my_stopwords:
            continue

        #append to list
        word_list.append(word)
    spent = start - time.time()
    print("Time spent: "+str(spent))
    return(word_list)
    
    
import sys
word_list = get_brown_corpus()

#Bonus:
#calculate frequency distribution of all words
fdist = FreqDist(word_list)
print(fdist.most_common(500))
sys.exit(0)

def get_brown_corpus_in_range2(the_range,word_list):
    stemmer = PorterStemmer()
    start = (the_range[0])
    end = int(the_range[1])
    print("Range: "+ str(start)+", "+str(end))
    custom_stopwords = []
    my_stopwords = stopwords.words('english') + custom_stopwords
    #word_list=[]
    #for word in brown.words() in range [start,end]:
    for i in range (start,end):
        word = brown.words()[i]
        #At Least one alphabet must be found in the word. Otherwise it's not a word.
        if not any(c.isalpha() for c in word):
            continue
        #Remove numbers     ( Section disabled since the section above already takes care of removing numbers)
        # if word.isnumeric():
            # continue 
        #Lowercase
        word = word.lower()
        #Stem
        word = stemmer.stem(word)
        #Remove Stopwords  (Has to be checked AFTER lowercasing & stemming)
        if word in my_stopwords:
            continue

        #append to list
        word_list.append(word)
    
    #return(word_list)
def get_brown_corpus_multithreaded():
    start = time.time()
    from multiprocessing.dummy import Pool as ThreadPool 
    from threading import Thread
    
    
    # print 'hello {0}'.format(bar)
    # result[index] = "foo"

    thead_count = 4
    full_dict = brown.words()
    word_count = len(full_dict)
    print("total words:" + str(word_count))
    
    per_thread = word_count // thead_count  #this many words per thread
    current_index = 0
    the_range=[]
    for i in range(0,thead_count):
        start = current_index
        end = current_index+per_thread
        new_range=[]
        if i == thead_count-1 or i >= word_count:
            new_range = [start,word_count]
        else:
            new_range = [start,end]
            
        print("new_range:   "+str(new_range))
        the_range.append(new_range)
        current_index += per_thread + 1
    
    print("--------------------------")
    '''
    threads = [None] * thead_count
    results = [None] * thead_count
    for i in range(len(threads)):
        threads[i] = Thread(target=get_brown_corpus_in_range2, args=(the_range[i], results))
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()
    print(results[0])
    spent = start - time.time()
    print("Time spent: "+str(spent))
    return()
    '''  

    spent = start - time.time()
    
    
    pool = ThreadPool(thead_count)
   
    #the_range = [ [0,100] ]
    # range = [0,100]
    print("start pool")
    return_list = pool.map(get_brown_corpus_in_range, the_range)

    
    
    print("Terminating")
    #pool.close()
    thread_pool.terminate()
    print("Termination: Start join")
    pool.join()
    print("Termination: joined")
    
    
    print("Time spent: "+str(spent))
    
    for status, data in return_list:
        print(data)
    
    print(result[0])
    #print(results)
    print("size of corpus == "+str(len(results)))
    return()
    return(results)


def get_brown_corpus_in_range(the_range):
    stemmer = PorterStemmer()
    start = (the_range[0])
    end = int(the_range[1])
    print("Range: "+ str(start)+", "+str(end))
    custom_stopwords = []
    my_stopwords = stopwords.words('english') + custom_stopwords
    #stemmer = PorterStemmer()
    word_list=[]

    #for word in brown.words() in range [start,end]:
    for i in range (start,end):
        word = brown.words()[i]
        #At Least one alphabet must be found in the word. Otherwise it's not a word.
        if not any(c.isalpha() for c in word):
            continue
            
        #Remove numbers     ( Section disabled since the section above already takes care of removing numbers)
        # if word.isnumeric():
            # continue
            
        #Lowercase
        word = word.lower()
        
        #Stem
        word = stemmer.stem(word)
        
        #Remove Stopwords  (Has to be checked AFTER lowercasing & stemming)
        if word in my_stopwords:
            continue

        #append to list
        word_list.append(word)
    return(word_list)


        
# Calculate frequency distribution


#Example usage on how to get a wordlist:
# word_list = get_brown_corpus()
# word_list = get_brown_corpus_in_range(0,100)
word_list = get_brown_corpus_multithreaded()

fdist = FreqDist(word_list)
print(fdist.most_common(500))



'''
TO DO:

L                           #the number of words between a n-gram and the heaviest one
termFrequency("car")        #Return the frequency of the word in the corpus
mostFrequent()              #frequency of the most frequent word in the corpus

'''

from numpy import log as ln

def termFrequency(word):
    ni = 1          
    return(ni)
def mostFrequent(corpus):
    
    ni = 1          
    return(ni)
 
# def ln()
    # return(math.log((1 + (FV * r) / p) / math.log(1 + r))))
k=0.1      # constant set according to the paper:     LIPN-CORE: Semantic Text Similarity using n-grams, WordNet, Syntactic Analysis, ESA and Information Retrieval based Features, Davide Buscaldi, Joseph Le Roux,Jorge J. Garcia Flores
L=2        # L is the number of words between a n-gram and the heaviest one
dxx_max = 1+ k*ln(1+ L)
one_per_dxx_max = 1/dxx_max

print(dxx_max)
print(one_per_dxx_max)



ni =  termFrequency("car")          #term frequency of the word in the corpus
N = mostFrequent("")