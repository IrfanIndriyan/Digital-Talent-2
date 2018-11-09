import csv
import os

base = os.path.dirname(os.path.abspath(__file__))

def get_cameo(cameo_name):
	cameo_filename = base + "/CAMEO/CAMEO.%s.txt" % cameo_name
	cameo_dict = {}

	with open(cameo_filename, 'r') as file:
		file.readline()

		for line in file:
			line.replace('\n', '')
			(key, val) = line.split('\t')
			cameo_dict[key] = val

	return cameo_dict

def get_feature():
	feature_filename = base + "/feature/header.csv"
	feature_list = []

	with open(feature_filename, 'r') as file:
		reader = csv.reader(file)
		
		for features in reader:
			for feature in features:
				feature_list.append(feature)

	return feature_list