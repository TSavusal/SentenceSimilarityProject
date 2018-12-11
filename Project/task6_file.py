'''
Description  ------------------------------------------------------------------------
Function creates a list that contains paired sentences taken from the given database.

Inputs  -----------------------------------------------------------------------------
filename - database-file's name (string)

#Outputs ----------------------------------------------------------------------------
Returns an array containing sentence pairs.
'''
def task6(filename):
    sentencePairs=[]

    #File operations
    text_file = open(filename, "r")
    textlines = text_file.read().splitlines() #Split lines
    text_file.close()

    #Split textlines into sentence pairs and add them to sentencePairs
    for line in textlines:
        sentencePairs.append(line.split(","))

    return(sentencePairs)
