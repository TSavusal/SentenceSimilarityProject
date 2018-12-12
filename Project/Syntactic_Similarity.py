import nltk
import string
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize


def task3SyntacticRunner(sentencePairs):
    for i in range(0,len(sentencePairs)):
        s1 = sentencePairs[i][0]
        s2 = sentencePairs[i][1]
        sim = task3SyntacticSim(s1,s2)
        sim = (round(sim,3))
        print("Similarity (Syntactic): " + str(sim).ljust(5) + " for sentence pair: "+ str(sentencePairs[i]))
        
def task3SyntacticSim(sent1,sent2):
	vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
	tfidf = vectorizer.fit_transform([sent1, sent2])
	return ((tfidf * tfidf.T).A)[0,1]

def stem_tokens(tokens):
    stemmer = nltk.stem.porter.PorterStemmer()
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

def intro():
	print("Syntactic similarity between two sentences\n")
	sent_one = raw_input("Enter the first sentence to compare similarity : ")
	sent_two = raw_input("Enter the second sentence to compare similarity : ")
	print("Calculating...\n")
	prob_sim_sent = task3SyntacticSim(sent_one, sent_two)
	print("Distance: ")
	print(prob_sim_sent)
	
if __name__ == "__main__":  
    print("-------------------Syntactic Similarity--------------------------")
    intro()
    print("Want to try once again? If yes enter 1, if not enter 0 : ")
    againtry = int(raw_input())
    while(againtry == 1):
        intro()
        print("Want to try once again? If yes enter 1, if not enter 0 : ")
        againtry = int(raw_input())