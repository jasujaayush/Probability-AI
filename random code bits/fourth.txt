import math
import csv
import sys

def countBigram(a,b):
        val = 0
        for x in bCount:
                if (x[0] == a) and (x[1] == b):
                        #print "count", unigram[a], unigram[b]
                        temp = x[2]
                        val = temp
        #print val, val/float(uCount[a])
        return val/float(uCount[a])


def probBigram(a,b):
	val = sys.float_info.min
	flag = 0
	for x in bCount:
		if (x[0] == a) and (x[1] == b):
			#print unigram[a], unigram[b]
			flag = 1
			temp = x[2]
			val = float(temp)/float(uCount[a])
	#print val
	if flag == 0:
		print "not there : ", unigram[a], unigram[b]
	return math.log(val)

def probUnigram(word):
	#print "Unigram : " + word
	return math.log(uDict[word])

with open('vocab.txt') as v:
	unigram = v.read().splitlines()

with open('unigram.txt') as u:
        uCount = u.read().splitlines()

bCount = []
theIndex = unigram.index("THE")
theBigrams = {}
with open('bigram.txt') as b:
	temp = b.read().splitlines()
	for x in temp:
		element = x.split('\t')
		element[0] = int(element[0]) -1
		element[1] = int(element[1]) - 1
		element[2] = int(element[2])
		bCount.append(element)

uDict = {}
totalCount = 0

for x in uCount:
	totalCount = totalCount + int(x)

print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
for x in xrange(0,len(unigram)):
	uDict[unigram[x]] = float(uCount[x])/totalCount
	if unigram[x].startswith('A'):
		print unigram[x], uDict[unigram[x]]
print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

temp = 0
for x in bCount:
	if x[0] is theIndex:
		#print unigram[x[1]], unigram.index(unigram[x[1]]), x[2]
		temp = temp + int(x[2])
		theBigrams[unigram[x[1]]] = float(x[2])/int(uCount[theIndex])

#print temp, uCount[theIndex]

sortedTheBigrams = sorted(theBigrams.iteritems(), key=lambda (k,v): (v,k))
l = len(sortedTheBigrams)
print "THEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
for x in xrange(1,6):
	print str(sortedTheBigrams[l - x])
print "THEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"

cSentence = []
cSentence.append(uDict['LAST'])
cSentence.append(uDict['WEEK'])
cSentence.append(uDict['THE'])
cSentence.append(uDict['STOCK'])
cSentence.append(uDict['MARKET'])
cSentence.append(uDict['FELL'])
cSentence.append(uDict['BY'])
cSentence.append(uDict['ONE'])
cSentence.append(uDict['HUNDRED'])
cSentence.append(uDict['POINTS'])
cLogUnigram = 0.0
for x in cSentence:
	cLogUnigram = cLogUnigram + math.log(x)
print "cLogUnigram : ", cLogUnigram

s = "<s> LAST WEEK THE STOCK MARKET FELL BY ONE HUNDRED POINTS".split(" ")
prob = 0.0
for x in xrange(1, len(s)):
	#print s[x-1], unigram.index(s[x-1]),s[x], unigram.index(s[x])
	prob = prob + probBigram(unigram.index(s[x-1]),unigram.index(s[x])) 
print "cLogBigram : ", prob


s = "THE NINETEEN OFFICIALS SOLD FIRE INSURANCE".split(" ")
dLogUnigram = 0.0
for x in xrange(0,len(s)):
	print unigram[unigram.index(s[x])]
	dLogUnigram = dLogUnigram + math.log(uDict[s[x]])

print "dLogUnigram : ", dLogUnigram

s = "<s> THE NINETEEN OFFICIALS SOLD FIRE INSURANCE".split(" ")
dprob = 0.0
for x in xrange(1, len(s)):
        print s[x-1], unigram.index(s[x-1]),s[x], unigram.index(s[x])
        dprob = dprob + probBigram(unigram.index(s[x-1]),unigram.index(s[x]))
print "dLogBigram : ", dprob

data = []
s = "<s> THE NINETEEN OFFICIALS SOLD FIRE INSURANCE".split(" ")
maxProb = -100000000
lmax = 0
for y in xrange(1,1000):
	l = 0.0
	l = l + y/float(1000)
	prob = 1.0
	for x in xrange(1,len(s)):
		prob = prob * ( (1-l)*uDict[s[x]] + l*countBigram(unigram.index(s[x-1]),unigram.index(s[x])) ) 
	prob = math.log(prob)
	data.append([l, prob])
	#print "l = ", l, prob
	if prob > maxProb:
		maxProb = prob
		lmax = l

with open('test.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(["l", "prob"])	
    a.writerows(data)

print "l for max prob", lmax, maxProb
