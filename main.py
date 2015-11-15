import requests
import json
import sys

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
	print("##########################################################")
	print("The following people broke the build:")
	for i in range(0, max(count)):
		for j in range(0, len(list)):
			if(count[j] == i):
				 print(list[j] + " " + str(count[j]))


url_no = "http://deco2800.uqcloud.net/jenkins/job/" + str(sys.argv[1]) + "/"
print(url_no)
r = requests.post(url_no + "lastBuild/api/json")
data = r.json();
lastBuild = data['number']
starting_build = 1
print(len(sys.argv[2]))
if len(sys.argv) == 3 and int(sys.argv[2]) > 0 and int(sys.argv[2]) <= lastBuild:
	starting_build = int(sys.argv[2])
print("Starting from build " + str(starting_build))
print("There are " + str(lastBuild - starting_build + 1) + " builds to check")

for i in range(starting_build, lastBuild):
	try:
		x = requests.post(url_no + str(i) + "/api/json")
		d = x.json()
		print("\n" + str(i) + " " + d['result']),
		if(d['result'] == 'FAILURE'):
			changers = []
			for w in range(0, len(d['changeSet']['items'])):
                                print(d['changeSet']['items'][w]['author']['fullName'] + " "),
				changers.append(d['changeSet']['items'][w]['author']['fullName'])
			for changer in set(changers):
				addToList(changer)
	except:
		pass
printSortedList()


