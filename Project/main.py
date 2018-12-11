# Download requirements	 ---------------------------------------------------------------------------------------------------------------------------------
from task0_download_reqs import download_requirements
download_requirements()
# Import modules	 -------------------------------------------------------------------------------------------------------------------------------------
from Semantic_Similarity import task3SemanticRunner
from task1_file import task1
from task2_file import sentenceSimilarityForTask2, task2,get_wordnet_pos
from task5_file import sentenceSimilarityForTask5, task5
from task4_file import task4
from task6_file import task6
# --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Main function. This will be used to run all the tests.
'''
if __name__== "__main__":
    #Task 1: Build sentence pairs
    print("\nTask 1: Build sentence pairs ----------------------------------------------------------------------------------------------------------------")
    sentencePairs=task1()
    #Task 2: Calculate similarity for the sentence pairs
    print("\nTask 2: Calculate similarity ----------------------------------------------------------------------------------------------------------------")
    print("\nTask 2a: path_sim metric")
    task2(sentencePairs,"path_sim")        #possible metrics: "wupalmer_sim"  or "path_sim"
    print("\nTask 2b: Wu-Palmer metric")
    task2(sentencePairs,"wupalmer_sim")        #possible metrics: "wupalmer_sim"  or "path_sim"

    #Task 3
    print("\nTask 3: Calculate similarity for the sentence pairs -----------------------------------------------------------------------------------------")
    task3SemanticRunner(sentencePairs)

    #Task 4: Calculate similarity for the sentence pairs using YAGO
    print("\nTask 4: Calculate similarity for the sentence pairs using YAGO concepts ---------------------------------------------------------------------")
    task4(sentencePairs)

    #Task 5: Word2Vec for calculating sentence similarity. (Word2Vec)
    print("\nTask 5: Word2Vec for calculating sentence similarity ----------------------------------------------------------------------------------------")
    model = task5(sentencePairs,None)

    #2nd call to task5 now we can use the model that was created on the previous step
    print("2nd call to task5")
    task5(sentencePairs,model)

	#Task 6: Build and use dataset sentence pairs in tasks 2,3,4 and 5
    sentencePairs2=task6("sentencepairs.txt")

    print("\nTask 6 sentence similarity using method from Task 2: -----------------------------------------------------------------------------------------")
    print("\npath_sim metric")
    task2(sentencePairs2,"path_sim")
    print("\nWu-Palmer metric")
    task2(sentencePairs2,"wupalmer_sim")

    print("\nTask 6 sentence similarity using method from Task 3: -----------------------------------------------------------------------------------------")
    task3SemanticRunner(sentencePairs2)

    print("\nTask 6 sentence similarity using method from Task 4: -----------------------------------------------------------------------------------------")
    task4(sentencePairs2)

    print("\nTask 6 sentence similarity using method from Task 5: -----------------------------------------------------------------------------------------")
    task5(sentencePairs2, model)
