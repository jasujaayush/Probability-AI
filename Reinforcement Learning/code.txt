import csv
import math
import sys
import numpy as np

action1 = []
action2 = []
action3 = []
action4 = []
r = []
v = [0.0]*81
bp = [0]*81
gamma  =  0.9925
policy = []

for x in xrange(0,81):
	action1.append([0.0]*81)
	action2.append([0.0]*81)
	action3.append([0.0]*81)
	action4.append([0.0]*81)

with open("prob_a1.txt") as f:
    content = f.readlines()
for t in content:
	x = t.strip().split()
	s1 = int(x[0]) - 1
	s2 = int(x[1]) - 1
	prob = float(x[2])
	action1[s1][s2] = prob

with open("prob_a2.txt") as f:
    content = f.readlines()
for t in content:
	x = t.strip().split()
	s1 = int(x[0]) - 1
	s2 = int(x[1]) - 1
	prob = float(x[2])
	action2[s1][s2] = prob	

with open("prob_a3.txt") as f:
    content = f.readlines()
for t in content:
	x = t.strip().split()
	s1 = int(x[0]) - 1
	s2 = int(x[1]) - 1
	prob = float(x[2])
	action3[s1][s2] = prob	

with open("prob_a4.txt") as f:
    content = f.readlines()
for t in content:
	x = t.strip().split()
	s1 = int(x[0]) - 1
	s2 = int(x[1]) - 1
	prob = float(x[2])
	action4[s1][s2] = prob

with open("rewards.txt") as f:
    content = f.readlines()
for t in content:
	x = int(t.strip())
	r.append(x)

def probmat(policy):
	p = []
	g = .9925
	for s in xrange(0,81):
		p.append([0.0]*81)
	for s in xrange(0,81):
		for sdash in xrange(0,81):
			if policy[s] == 1:
				p[s][sdash] = -1.0*g*action1[s][sdash]
			if policy[s] == 2:
				p[s][sdash] = -1.0*g*action2[s][sdash]
			if policy[s] == 3:
				p[s][sdash] = -1.0*g*action3[s][sdash]
			if policy[s] == 4:
				p[s][sdash] = -1.0*g*action4[s][sdash]			
	for s in xrange(0,81):
		p[s][s] = p[s][s] + 1		
	return p	

def maxa(v,s):
	maximum = 0
	temp = 0
	tpolicy = 1
	for x in xrange(0,81):
		maximum = maximum + action1[s][x]*v[x]
		tpolicy = 1

	temp = 0	
	for x in xrange(0,81):
		temp = temp + action2[s][x]*v[x]	
	if temp > maximum:
		maximum = temp
		tpolicy = 2

	temp = 0	
	for x in xrange(0,81):
		temp = temp + action3[s][x]*v[x]	
	if temp > maximum:
		maximum = temp
		tpolicy = 3

	temp = 0	
	for x in xrange(0,81):
		temp = temp + action4[s][x]*v[x]	
	if temp > maximum:
		maximum = temp
		tpolicy = 4
	return maximum,tpolicy				


''' part a and b '''
for x in xrange(0,2000):
	temp = [0.0]*81
	for s in xrange(0,81):
		q,w = maxa(v,s)
		temp[s] = r[s] +  gamma * q
		bp[s] = w
	v = temp


for s in xrange(0,81):
	if v[s] > 0:
		print s+1, v[s], bp[s]


''' PART C : TO RUN THIS Comment out part a and b
for x in xrange(0,81):
		policy.append(4)

for i in xrange(0,15):
	print policy
	y = probmat(policy)
	m = np.array(y)	
	minverse = np.linalg.inv(m)
	v = minverse.dot(r)
	temp = [0.0]*81
	for s in xrange(0,81):
		q,w = maxa(v,s)
		temp[s] = r[s] +  gamma * q
		bp[s] = w
	diff = 0
	for	j in xrange(0,81):
		if bp[j] is not policy[j]:
			diff = diff + 1
	print diff	
	if diff == 0:
		print "Iteration :",i 	
		break
	policy = bp[:]

print policy	

# part 1 [EAST] >  NUmber of iterations = 5. Policy is same in 4th and 5th iteration
# part 2 [SOUTH]>  NUmber of iterations = 11. Policy is same in 10th and 11th iteration
'''