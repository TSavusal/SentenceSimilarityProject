from sys import version_info
from sys import exit
if version_info <= (3, 0):
    print("\nUse python version 3.0 or higher. ( Code was tested with 3.5.2)")
    print("EXITING")
    exit(1)
try:
    from nltk.corpus import brown
    from nltk.corpus import wordnet as wn
except:
    import nltk
    print("Download the nltk book! Select it from the menu.\nWhen finished then close the menu.")
    nltk.download()
from Semantic_Similarity import task3SemanticRunner
from task1_file import task1
from task2_file import sentenceSimilarityForTask2, PartialSim, task2,get_wordnet_pos
from task5_file import sentenceSimilarityForTask5, task5
from task4_file import task4
# --------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__== "__main__":
    #Task 1: Build sentence pairs
    print("\nTask 1: Build sentence pairs -----------------------------------------------------------------------------------------------------------------")
    sentencePairs=task1()
    #Task 2: Calculate similarity for the sentence pairs
    print("\nTask 2: Calculate similarity ------------------------------------------------------------------------------------------")
    print("\nTask 2a: path_sim metric")
    task2(sentencePairs,"path_sim")        #possible metrics: "wupalmer_sim"  or "path_sim"
    print("\nTask 2b: Wu-Palmer metric")
    task2(sentencePairs,"wupalmer_sim")        #possible metrics: "wupalmer_sim"  or "path_sim"

    #Task 3
    print("\nTask 3: Calculate similarity for the sentence pairs ------------------------------------------------------------------------------------------")
    task3SemanticRunner(sentencePairs)

    #Task 4: Calculate similarity for the sentence pairs using YAGO
    print("\nTask 4: Calculate similarity for the sentence pairs using YAGO concepts ----------------------------------------------------------------------")
    task4(sentencePairs)

    #Task 5: Word2Vec for calculating sentence similarity. (Word2Vec)
    print("\nTask 5: Word2Vec for calculating sentence similarity -------------------------------------------------------------------------------------------")
    print("Task 5 NOTE: Building the model could take up to 60 seconds depending on the speed of your computer. Install Cython module to speed up the training.")
    model = task5(sentencePairs,None)
    
    #2nd call to task5 now we can use the model that was created on the previous step
    task5(sentencePairs,model)