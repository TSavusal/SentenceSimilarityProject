# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
#Task description:
We have a database of sentence pairs that has been edited and reduced to 5 occurences (sentencepairs.txt).
Using the same format as in Task 1, we manually add the sentence pairs to array and iterate through these similar to Task 2.
The results are then compared to the original set of sentences provided in Task 1.

#Function Description:
If you need to loop though the sentence pairs then see function task2() for an example
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