import numpy as np
from scipy.linalg import solve

with open('nasdaq01.txt') as v:
        k1 = v.read().splitlines()
l1 = []
for x in k1:
        l1.append(float(x))

print len(l1)

with open('nasdaq00.txt') as v:
        k = v.read().splitlines()
l = []
for x in k:
	l.append(float(x))

print len(l)
eq = []
for x in xrange(0,4):
	eq.append([0,0,0,0,0])

for i in xrange(4,len(l)):
	for y in xrange(0,5):
		for z in xrange(0,4):
			eq[z][y] = eq[z][y] + l[i-y]*l[i-z-1]

A = []
b = []
for x in xrange(0,4):
	print eq[x]
	A.append(eq[x][1:5])	
	b.append(eq[x][0])

c = solve(A, b)
print c
	
mspe = 0.0
n = 0
for x in xrange(4, len(l)):
	n = n+1
	temp = 0.0
	for y in xrange(1,5):
		temp = temp + l[x-y]*c[y-1]
	temp = abs(temp - l[x])
	#print temp
	mspe = mspe + temp**2
mspe = mspe/n
print mspe

mspe = 0.0
n = 0
for x in xrange(4, len(l1)):
	n = n+1
        temp = 0.0
        for y in xrange(1,5):
                temp = temp + l1[x-y]*c[y-1]
        temp = abs(temp - l1[x])
	#print temp
        mspe = mspe + temp**2

mspe = mspe/n
print mspe
