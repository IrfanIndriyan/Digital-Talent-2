import sys
sys.path.append("..")

import re, string
from nltk import word_tokenize as tokenize
from ..Kamus.corpus import collect_stopword
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def lower_case(words):
	"""lower_case

	"""
	new_words = []

	for word in words:
		new_word = word.lower()
		new_words.append(new_word)

	return new_words

def remove_punctuation(words):
	"""remove_punctuation

	"""
	new_words = []

	for word in words:
		new_word = re.sub(r['^\w\s'], '', word)
		if new_word != '':
			new_words.append(new_word)

	return new_words

def remove_stopword(words):
	"""remove_stopword
	"""
	stopword = collect_stopword()

	new_words = []

	for word in words:
		if word not in stopword:
			new_word = word
			new_words.append(new_word)

	return new_words

def lemmatize():
	pass

def detokenize(words):
	new_words = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in words]).strip()

	return new_words