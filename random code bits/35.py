import csv
import numpy as np
import math
from scipy.linalg import solve

testData = []
testData5 = []
data = []
value = []

with open('train3.txt') as v:
        k = v.read().splitlines()
for x in k:
	t = x.strip().split(' ')
	l = []
	for y in t:
		l.append(float(y))
	data.append(l)
	value.append(0) #0 means 3

with open('train5.txt') as v1:
        k1 = v1.read().splitlines()
for x in k1:
        t = x.strip().split(' ')
	l = []
        for y in t:
                l.append(float(y))
        data.append(l)
        value.append(1) #1 means 5


with open('test3.txt') as v:
        k = v.read().splitlines()
for x in k:
        t = x.strip().split(' ')
        l = []
        for y in t:
                l.append(float(y))
        testData.append(l)

with open('test5.txt') as v:
        k = v.read().splitlines()
for x in k:
        t = x.strip().split(' ')
        l = []
        for y in t:
                l.append(float(y))
        testData5.append(l)


def sigmoid(t,w):
	v = 0.0
	for i in xrange(0,len(l)):
		v = v + t[i]*w[i]
	v = 1/(1+math.exp(-v))
	return v

def scaleVector(x, y):
	value = []
	for i in xrange(0, len(x)):
		value.append(x[i]*y)
	return value

def addVectors(x, y):
        value = []
        for i in xrange(0, len(x)):
                value.append(x[i]+y[i])
        return value

def gradient(y,w,x):
	g = []
	for i in xrange(0,64):
		g.append(0.0)
	for i in xrange(0,len(y)):
		temp = sigmoid(x[i],w)
		value = y[i] - temp
		sV = scaleVector(x[i], value)
		g = addVectors(g,sV)
	return g

w = []
n = .000075
for i in xrange(0,64):
                w.append(0.0)

iteration = 1
testc = 0
while(True):
	g = gradient(value,w,data)
	s = scaleVector(g,n)
	w = addVectors(w, s)
	#print g
	c = 0
	testc5 = 0 
	testc = 0
	likelihood = 0
	for i in xrange(0,len(data)):
                temp = sigmoid(data[i],w)
		if temp < 0.5 and i < 700:
			c = c + 1
		elif temp > 0.5 and i > 700:
			c = c + 1
		likelihood = likelihood + math.log(temp)
	print "training : ", iteration, c , likelihood
	iteration = iteration + 1
	for i in xrange(0,len(testData)):
                temp = sigmoid(testData[i],w)
                if temp < 0.5:
                        testc = testc + 1
        print "test3 : ", len(testData), testc
	for i in xrange(0,len(testData5)):
                temp = sigmoid(testData5[i],w)
                if temp > 0.5:
                        testc5 = testc5 + 1
        print "test5 : ", len(testData5), testc5
	if iteration % 50 == 0:
		plotdata = []
		with open('data35.csv', 'a') as fp:
			plotdata.append([iteration, likelihood, (1-float(c)/1400)*100])
    			a = csv.writer(fp, delimiter=',')
    			a.writerows(plotdata)
		f1 = open('W.txt', 'w+')
		print >> f1, iteration , '\n'
		for k in xrange(0,8):
			print >> f1, w[k*8: (k+1)*8]
		print >> f1, '\n'


