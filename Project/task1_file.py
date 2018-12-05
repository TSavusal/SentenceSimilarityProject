
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