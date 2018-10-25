import re, string
from nltk import word_tokenize as tokenize
from Kamus.corpus import *
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def preprocessing(set_of_words, tokenization=1, lowercasing=2, removing_punctuation=3, removing_stopword=4, stemming=5, lemmatization=0, detokenization=6):
	"""preprocessing

	"""
	new_set_of_words = []


	factory = StemmerFactory()
	stemmer = factory.create_stemmer()

	for words in set_of_words:
		new_words = tokenize(words)
		new_words = lower_case(new_words)
		new_words = remove_punctuation(new_words)
		new_words = remove_stopword(new_words)
		new_words = stemmer.stem(new_words)
		new_words = detokenize(new_words)

		new_set_of_words.append(new_words)

	return new_set_of_words

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