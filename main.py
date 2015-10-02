import requests
import json

list = []
count = [];
def addToList(name):
	for i in range(0, len(list)):
		if(list[i] == name):
			count[i] += 1
			return;
	list.append(name);
	count.append(1);

def printList():
	for i in range(0, len(list)):
		print(list[i] + " " + str(count[i]))

def printSortedList():
	for i in range(0, max(count)):
		for j in range(0, len(list)):
			if(count[j] == i):
				 print(list[j] + " " + str(count[j]))

url = "http://deco2800.uqcloud.net/jenkins/job/Mine/lastBuild/api/json"
url_no = "http://deco2800.uqcloud.net/jenkins/job/Mine/"
r = requests.post(url)
data = r.json();
lastBuild = data['number']

for i in range(1, lastBuild-1):
	try:
		x = requests.post(url_no + str(i) + "/api/json")
		d = x.json()
		if(d['result'] == 'FAILURE'):
			print(str(i) + " " + d['result'] + " " + d['changeSet']['items'][0]['author']['fullName'])
			addToList(d['changeSet']['items'][0]['author']['fullName'])
	except:
		pass
printSortedList()


