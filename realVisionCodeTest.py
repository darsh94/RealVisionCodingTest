

import heapq
import re
import sys

# This method will accept a fileName of the file containing the list of common-words as an argument
# and will return a set of all the words presents the file
def getExcludedWords(fileName):
    fileObj = open(sys.path[0]+"/"+fileName,"r")
    isData = True
    exludedWords = set()
    while(isData):
        line = fileObj.readline()
        if line:
            line=line.lower()
            exludedWords.add(line.replace("\n",""))
        else:
            isData =False

    fileObj.close()
    return exludedWords

# This method will accept 2 arguments
# 1.filename of the actualTextFile to be read
# 2. a set having the all the words which need to be excluded
# This method will return a dictionary having
#  1. key => word present in the actualText but not present in excludedWordList
#  2. value => Frequency of the word
def getActualText(fileName,excludedWordList):
    fileObj = open(sys.path[0]+"/"+fileName ,"r")
    isData = True
    actualTextDict = {}
    while(isData):
        line = fileObj.readline()
        if line:
            line = line.replace("\n","")
            tempStr = re.sub('[!,*)@#%(&$_?.^\'`]', '', line)
            tempList = tempStr.split(" ")
            for i in tempList:
                if i:
                    i=i.lower()
                    i=i.replace('','')
                    if i not in excludedWordList:
                        if(actualTextDict.get(i)==None):
                            actualTextDict[i] =1
                        else:
                            actualTextDict[i] = actualTextDict.get(i)+1
        else:
            isData =False

    fileObj.close()
    return actualTextDict
##While processing the words, special characters have been removed
##Complexity of the algorithm (Complexity does not take into account compelxity of built-in functions)
## Time-complexity => Max time would be spent processing data from step 2, hence overall complexity => O(Nn)
## 1. Complexity to retrieve all the words to be excluded => O(m)
## 2. Complexity to retrieve all the words be actuallyRead (includes complexity for preprocessing the data) [We are reading the textFile line by line]
##  1. If there are N lines in the file and each file has n words => O(Nn)
## 3. Compelexity of storing elements in the heap=> logn
## 4. Complexity to remove top k elements from the heap=> klogn
## Space-complexity=> O(m+n)
## 1. set to store all the words to be excluded =>O(m), where n is the number of distinct words in the file
## 2. dictionary to store all words present in the actualTextFile=> O(n),where n is the number of distinct words in the file
## 3. A heap to store all key-value-pair in the dictionary=> O(n)
def main():
    print("The text file to be read is " + sys.argv[1])
    print("The text file having words to be exluded is " + sys.argv[2])
    print("The top "+ sys.argv[3]+" are to be retrieved based on the frequency")
    excludedWordList = getExcludedWords(sys.argv[2])
    wordFreq=getActualText(sys.argv[1],excludedWordList)
    heap = []
    di = [(k, v) for k, v in wordFreq.items()]
    for i in di:
        # Multiplying the frequncy of each word by -1, to store the words in descending order of their frequency
        heapq.heappush(heap,(i[1]*-1,i[0]))
    counter = 0
    for i in range(2):
        if(i==0):
            print("Count"+"  "+"Word")
        else:
            print("==="+"    "+"====")
    for i in heap:
        pooped = heapq.heappop(heap)
        if(counter==int(sys.argv[3])):
            break
        print(str(pooped[0]*-1)+"    "+pooped[1])
        counter+=1

    # print(wordFreq)
if __name__ == "__main__":
    main()
