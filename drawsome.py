#Vamshidhar Dantu
#Aug 2012

#! /usr/bin/python

import sys, os
import itertools 

# TOO MANY GLOBALS ... BADDDDDDDD
f=''
dictionary=dict()
resultDict=dict()

# debug tool
def printDict(length):
    print dictionary[length]

# Check if the word is already appended to resultDict
def CheckIfWordAddedtoRsltDict(word):
    if 'result' in resultDict:
        for k in resultDict['result']:
            if k == word:
                return 0        # This is a non-unique entity. Dont queue it in the resultDict.
    return 1                    # This is a unique entity. Queue it up in the resultDict

# append the correct permutations in the dictionary
def FoundWords(word):
    if word in dictionary:
        if CheckIfWordAddedtoRsltDict(word): # check for uniqueness
            resultDict.setdefault('result',[]).append(word)

# create a dictionary out of the raw data file
def CreateDict(rawDictFile):
    for line in rawDictFile:
        line=line.rstrip()
        dictionary.setdefault(line,[]).append(len(line)) # Word : length format . Length field dummy
    
# Bad coding. Should push some functionality to the main funciton....
def PermuteAndFind(word,boundry):
    wordToSearch = ''
    for a in itertools.permutations(word,boundry): # saves in tuples :( 
        wordToSearch="".join(a)                    # convert each tuple to word :D
#        print wordToSearch
        FoundWords(wordToSearch)              # NOW HUNT THE WORDS IN THE DICTIONARY
# Useful for debugging
#        printDict(int(len(wordToSearch)))         

# IT ALL BEGINS HERE >:)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "USAGE:",sys.argv[0]," <list of letters> <range>"
        print "If you dont give the range, the whole word is considered and permuted over the length of the word."
        sys.exit(1)
    dirname = os.path.dirname(sys.argv[0])
    actPath= os.path.abspath(dirname)+'/dictionary.txt' # Dictionary that we love. Has repeated words though!!!!
    boundry=None
    word=sys.argv[1]
    if len(sys.argv)==3:
        boundry=int(sys.argv[2])
    f = open(actPath,'r+')
    CreateDict(f)
    f.close()
    PermuteAndFind(word, boundry)
    if 'result' in resultDict:
        print "AND THE POSSIBLE WORDS ARE: \n%s" %(resultDict['result'])
    else :
        print "NONE FOUND :("
