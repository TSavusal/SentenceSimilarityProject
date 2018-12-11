'''
Description  ------------------------------------------------------------------------
Function creates a list that contains paired sentences taken from the database
'sentencepairs.txt'.

Inputs  -----------------------------------------------------------------------------
No inputs

#Outputs ----------------------------------------------------------------------------
Returns a list containing sentence pairs.
'''
def task6():
    sentencePairs=[]
    #1.
    sent1 = "A cat is playing with a stuffed bear"
    sent2 = "A cat is playing with a toy"
    sentencePairs.append([sent1,sent2])
    #2.
    sent1 = "The sheep is grazing on the grass"
    sent2 = "An animal is grazing in a field"
    sentencePairs.append([sent1,sent2])
    #3.
    sent1 = "A girl is riding a horse"
    sent2 = "A girl is riding a brown horse"
    sentencePairs.append([sent1,sent2])
    #4.
    sent1 = "A boy is riding a bicycle"
    sent2 = "A dog is jumping a fence"
    sentencePairs.append([sent1,sent2])
    #5.
    sent1 = "A cat is resting on a chair"
    sent2 = "An onion is being cut by a man"
    sentencePairs.append([sent1,sent2])
    return(sentencePairs)
