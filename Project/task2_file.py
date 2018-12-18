from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
# from task5 import keep_allowed_chars
# --------------------------------------------------------------------------------------------------------------------------------------------------------

# def sentenceSimilarityForTask2(s1,s2,method):
    # val1 = PartialSim(s1,s2,method)
    # return(val1)
# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Description  -------------------------------------------------------------------------
Calculates sentence similarity based on either Wu-Palmer or path similarity.

Inputs  ------------------------------------------------------------------------------
s1          Sentence 1
s2          Sentence 2
method      The method to be used. Either "wupalmer_sim"  or "path_sim"

#Outputs -----------------------------------------------------------------------------
Returns the value the represents the similarity between the sentences.

Example usage of the function  -------------------------------------------------------

s1 = "Car is driving on the road"
s2 = "Car is driving on the road"
print(sentenceSimilarityForTask2(s1,s2,"wupalmer_sim"))
'''
def sentenceSimilarityForTask2(s1,s2,method):
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
# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Description
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
# ----------------------------------------------------------------
'''
Description  -------------------------------------------------------------------------
Function that will calculate sentence similarities based on wordnet.
Prints the results

Inputs  ------------------------------------------------------------------------------
sentencePairs       A list containing pairs of sentences
similarity_method   The method to be used for calculating the similarity
#Outputs -----------------------------------------------------------------------------
No outputs

Example usage of the function  -------------------------------------------------------
See "main.py" file for an example.
'''
def task2(sentencePairs,similarity_method):
    for i in range(0,len(sentencePairs)):
        s1 = sentencePairs[i][0]
        s2 = sentencePairs[i][1]
        sim = sentenceSimilarityForTask2(s1,s2,similarity_method)
        sim = (round(sim,3))
        
        #Write to csv
        # with open('sim.csv','a') as fd:
            # my_str = str(sim) + "\n"
            # fd.write(my_str)
        
        print("Similarity: ("+str(similarity_method)+") " + str(sim).ljust(5) + " for sentence pair: "+ str(sentencePairs[i]))    #NOTE: ljust is used in order to format the print