'''
Description  ------------------------------------------------------------------------
Function creates a list that contains paired sentences.

Inputs  -----------------------------------------------------------------------------
No inputs

#Outputs ----------------------------------------------------------------------------
Returns a list containing sentence pairs.
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