def word_count(words):
	# Removing Punctuation
	# new_words = re.sub(r'[^\w\s]', '', words)
	words = remove_punctuation(words)
	words = tokenize(words)
	words = lowercasing(words)
	unique_words = unique(list(words))
	vocabulary = {}

	for word in unique_words:
		vocabulary[word] = count(words, word)

	return vocabulary

def tokenize(words):
	new_words = words.split(" ")

	del(new_words[new_words.index('')])
	
	return new_words

def remove_punctuation(words):
	new_words = words.replace('.', '')
	new_words = new_words.replace(',', '')
	new_words = new_words.replace('(', '')
	new_words = new_words.replace(')', '')

	return new_words

def lowercasing(words):
	new_words = []

	for word in words:
		new_word = word.lower()
		new_words.append(new_word)

	return new_words

def unique(words):
	new_words = []

	for word in words:
		if word in new_words:
			del(words[words.index(word)])
		else:
			new_words.append(word)

	return new_words

def count(words, find):
	c = 0

	for word in words:
		if word == find:
			c += 1

	return c