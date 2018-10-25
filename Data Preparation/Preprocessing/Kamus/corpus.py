import csv

def collect_stopword():
	stopword_collection = []

	with open("stopwordbahasa.csv", 'r') as csvfile:
		read_csvfile = csv.reader(csvfile)

		for word in read_csvfile:
			stopword_collection.append(word[0])

	return stopword_collection