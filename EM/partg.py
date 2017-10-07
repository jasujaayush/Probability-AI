import math

def term2(xn):
	t1 = math.exp(2*xn)
	t2 = math.exp(-2*xn)
	v = (t1 - t2)/4
	return v

def converge(x):
	c2 = 2*x
	c1 = x
	while(abs(c1 - c2) > 0.000001):
		c2 = c1
		c1 = c1 - term2(c1)
		print c1

converge(-2)

#to find x0
for x in xrange(0,2000):
	print x/1000.0, converge(x/1000.0)

