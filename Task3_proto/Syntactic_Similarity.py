import nltk 
from nltk.tag.hunpos import HunposTagger
from nltk.tokenize import word_tokenize

s1 = "This is a short sentence"
s2 = "That is the same sentence"

ht = HunposTagger('en_wsj.model')
print ht.tag(word_tokenize(corpus))http://nltk.org/

# Tag the sentences with HunPos
t1 = ht.tag(word_tokenize(s1))
t2 = ht.tag(word_tokenize(s2))

#Extract only the POS tags
pos1 = [i[1] for i in t1]
pos2 = [j[1] for j in t2]

if pos1 == pos2:
    print "same sentence according to POS tags"
else:
    print "diff sentences according to POS tags"