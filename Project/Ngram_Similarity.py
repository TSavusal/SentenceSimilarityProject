import nltk

def task3SyntacticSim(sequence, n, pad_left=False, pad_right=False, pad_symbol=None):
<<<<<<< HEAD

=======
>>>>>>> refs/remotes/origin/master

    if pad_left:
        sequence = chain((pad_symbol,) * (n-1), sequence)
    if pad_right:
        sequence = chain(sequence, (pad_symbol,) * (n-1))
    sequence = list(sequence)

    count = max(0, len(sequence) - n + 1)
    return [tuple(sequence[i:i+n]) for i in range(count)]
	
	def intro():
		print("Ngram similarity between two sentences\n")
		sent_one = input("Enter the first sentence to compare similarity : ")
		sent_two = input("Enter the second sentence to compare similarity : ")
		print("Calculating...\n")
		prob_sim_sent = task3NgramSim(sent_one, sent_two)
		print("Distance: ")
		print(prob_sim_sent)
	
if __name__ == "__main__":  
    print("-------------------Ngram Similarity--------------------------")
    intro()
    print("Want to try once again? If yes enter 1, if not enter 0 : ")
    againtry = int(input())
    while(againtry == 1):
        intro()
        print("Want to try once again? If yes enter 1, if not enter 0 : ")
        againtry = int(input())