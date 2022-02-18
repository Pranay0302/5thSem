import os
from functools import reduce
import sys

dict ={}
wordlen = []

if(len(sys.argv) != 2):
    print('invalid format')
    exit()

if(not(os.path.exists(sys.argv[0]))):
    print('invalid file path')
    exit()


with open(sys.argv[1]) as file:
    for line in file:
        for word in line.split():
            dict[word] = dict.get(word, 0) + 1
 
sortedDict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
for i in range(len(sortedDict)):
	print(sortedDict[i])

for i in range(10):
	try:
		wordTuple = sortedDict[i]
		wordlen.append(len(wordTuple[0]))
		print (wordTuple[0], ", Frequency: " , wordTuple[1] , ", Length " , len(wordTuple[0]))
	except IndexError:
		print ("file has less than 10 words")
		break

print(wordlen)
