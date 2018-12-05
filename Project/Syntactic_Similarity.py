import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize

def task3SyntacticSim(s1,s2):
	
	nltk.download('punkt') # if necessary
	stemmer = nltk.stem.porter.PorterStemmer()
	remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
	stemed_tokens = stem_tokens()
	
def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

	vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]
	
def intro():
		print("Syntactic similarity between two sentences\n")
		sent_one = input("Enter the first sentence to compare similarity : ")
		sent_two = input("Enter the second sentence : ")
		print("Calculating...\n")
		prob_sim_sent = task3SyntacticSim(sent_one, sent_two)
		print("Distance: ")
		print(prob_sim_sent)
	
if __name__ == "__main__":  
    print("-------------------Syntactic Similarity--------------------------")
    intro()
    print("Want to try once again? If yes enter 1, if not enter 0 : ")
    againtry = int(input())
    while(againtry == 1):
        intro()
        print("Want to try once again? If yes enter 1, if not enter 0 : ")
        againtry = int(input())