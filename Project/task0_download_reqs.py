'''
Description  ---------------------------------------------------------------
Function will check python version. It should be python3, otherwise execution is halted.
Function will search for the required NLTK packages and download them if necessary.

Inputs  ---------------------------------------------------------------
No inputs

#Outputs -----------------------------------------------------------------------------
No outputs

Example usage of the function  -------------------------------------------------------
See "main.py" file for an example.
'''
def download_requirements():
	# Verify Python Version	 ---------------------------------------------------------------------------------------------------------------------------------
	from sys import version_info
	from sys import exit
	if version_info <= (3, 0):
		print("\nUse python version 3.0 or higher. ( Code was tested with 3.5.2)")
		print("EXITING")
		exit(1)
	try:
		#Verify that we have the required nlkt packages
		from nltk.data import find as nltk_find
		nltk_find('tokenizers/punkt')
		nltk_find('corpora/wordnet')
		nltk_find('corpora/wordnet_ic')
		nltk_find('taggers/averaged_perceptron_tagger')
		nltk_find('corpora/brown')
		nltk_find('corpora/stopwords')
	except LookupError:
		print("Download packages since some packages were missing")
		from nltk import download as nltk_download
		nltk_download('wordnet')
		nltk_download('wordnet_ic')
		nltk_download('punkt')
		nltk_download('averaged_perceptron_tagger')
		nltk_download('stopwords')
		nltk_download('brown')