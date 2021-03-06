import csv
import math
import sys

def getLMatrix(a, b, observation):
	talpha = []
	#basecase
	for i in xrange(0,len(pie)):
		temp = []
		base = math.log(pie[i]) + math.log(b[i][observation[0]])
		temp.append(base)
		talpha.append(temp)
		
	for t in xrange(1, len(observation)):
		print t
		for j in xrange(0,len(pie)):
			v = talpha[0][t-1] + math.log(a[0][j])
			temp = 0
			for i in xrange(0, len(talpha)):
				temp = talpha[i][t-1] + math.log(a[i][j])
				if temp > v:
					v = temp
			v = v + math.log(b[j][observation[t]])
			talpha[j].append(v)
	return talpha

def getState(a, b, observation, alpha):
	tbeta = []
	T = len(observation) - 1	
	#basecase
	ST = 0
	v = alpha[0][T]
        for x in xrange(0,len(alpha)):		
                temp = alpha[x][T]
                if temp > v:
			ST = x
			v = alpha[x][T]
	tbeta.append(ST)	

	for t in xrange(len(observation)-2, -1, -1):
		j = tbeta[0] 
		S = 0
                v = alpha[0][t+1] + math.log(a[0][j])
                for i in xrange(0, len(alpha)):
                        temp = alpha[i][t+1] + math.log(a[i][j])
			if temp > v:
				S = i
				v = temp	
		tlist = [S]
                tbeta = tlist + tbeta
        return tbeta

with open("observations.txt") as f:
    content = f.readlines()
observation = []
for x in content[0].strip().split(" "):
	observation.append(int(x))


with open("initialStateDistribution.txt") as f:
    content = f.readlines()
pie = []	
for x in content:
	pie.append(float(x))

with open("emissionMatrix.txt") as f:
    content = f.readlines()
b = []
for x in content:
	temp = []
	for y in x.strip().split("\t"):
		temp.append(float(y))
	b.append(temp)

with open("transitionMatrix.txt") as f:
    content = f.readlines()
a = []
for x in content:
        temp = []
        for y in x.strip().split(" "):
                temp.append(float(y))
        a.append(temp)

	
alpha = getLMatrix(a, b, observation)
for x in xrange(0,26):
	print alpha[x][0]
beta = getState(a, b, observation, alpha)
