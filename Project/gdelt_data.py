import requests
import lxml.html as lh
import pandas as pd
import os
import urllib
import zipfile

# GDELT 1.0 URL
gdelt_base_url = "http://data.gdeltproject.org/events/"

# get the list of all links on the gdelt file page
page = requests.get(gdelt_base_url)
doc	= lh.fromstring(page.content)
link_list = doc.xpath("//*/ul/li/a/@href")

# separate out those links that beign with four digits
# and
# links that are below 2012
file_list = [x for x in link_list if str.isdigit(x[0:4]) and int(x[0:4]) > 2011]

# Define
local_path = os.path.expanduser("~/myGit/DataStore/GDELT1/")

# Initialize filter
country_code = ["IDN"]
known_group_code = [""]
ethnic_code = [""]
event_code = [""]
religion_code = [""]
type_code = [""]

if not os.path.exists(local_path + "compressed"):
	os.makedirs(local_path + "compressed")

for compressed_file in file_list:
	print (compressed_file)

	while not os.path.isfile(local_path + "compressed/" + compressed_file):
		print ("Downloading...")
		urllib.request.urlretrieve(url=gdelt_base_url + compressed_file,
							filename=local_path+"compressed/"+compressed_file)
