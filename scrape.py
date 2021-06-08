import requests
import pandas as pd
import numpy as np

headers = {"User-Agent": "XY"}
link = "https://brokercenter.net/playa-del-carmen/" # enter specific page
r = requests.get(link, headers=headers)
print(len(r.text.split('<tr class="row')))

Dataset = "" # declare variable so python does not freak out

cols = []
for row in range(1, len(r.text.split('<tr class="row'))): # loop through rows
	l = r.text.split(f'<tr class="row-{row} ')[1].split('</tr>')[0]
	s = l.split('">')
	icols = []
	for col in range(7): # loop through columns in rows

		# get data from html
		if s[col].split("<")[0] == '\n\t' or s[col].split("<")[0] == "odd" or s[col].split("<")[0] == "even":
			continue
		if row == 1:
			cols.append(s[col].split("<")[0])
		else:
			icols.append(s[col].split("<")[0])


	# append data to dataset
	if row == 1:
		continue
	if row == 2:
		print(cols) # print columns
		Dataset = pd.DataFrame(np.array(icols).reshape([1, len(icols)]), index=[1], columns=cols)
		print(Dataset) # print columns and first row of data
	else:
		# appease pandas with odd reshaping of data lists
		Dataset = Dataset.append(pd.DataFrame(np.array(icols).reshape([1, len(icols)]), index=[1], columns=cols))

print(Dataset) # print data(it tends to run together when printed but is clean in memory)

Dataset.to_csv("data.csv") # save as csv file