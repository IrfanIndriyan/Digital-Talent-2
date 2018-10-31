import sys
sys.path.append("..")

def collect_stopword():
	import csv
	stopword_collection = []

	with open("stopwordbahasa.csv", 'r') as csvfile:
		read_csvfile = csv.reader(csvfile)

		for word in read_csvfile:
			stopword_collection.append(word[0])

	return stopword_collection

def collect_kbbi():
	from nltk import word_tokenize

	kbbi_collection = {}

	with open("kata_dasar.txt", 'r') as file:

		get_file = file.readlines()

		for line in get_file:
			word_syllable = word_tokenize(line)
			word_syllable = remove_punctuation(word_syllable)

			word = word_syllable[0]
			syllable = ' '.join(word_syllable[1:])

			kbbi_collection[word] = syllable

	return kbbi_collection

def remove_punctuation(words):
	"""remove_punctuation

	"""
	import re

	new_words = []

	for word in words:
		new_word = re.sub(r'[^\w\s]', '', word)
		if new_word != '':
			new_words.append(new_word)

	return new_words