import math

def derivative(xn):
	t1 = math.exp(xn)
	t2 = math.exp(-xn)
	v = (t1 - t2)/(t1 + t2)
	return v

def converge(x):
	c2 = 2*x
	c1 = x
	while(abs(c1 - c2) > 0.000001):
		c2 = c1
		c1 = c1 - derivative(c1)
		print c1

converge(-2)
converge(1)
