import math

def term2(xn):
	v = 0;
	for x in xrange(1,11):
		t1 = math.exp(2*xn + 2.0/float(x))
		v = v + (t1 - 1)/(t1 + 1)
	return v/10.0

def converge(x):
	c2 = 2*x
	c1 = x
	while(abs(c1 - c2) > 0.000001):
		c2 = c1
		c1 = c1 - term2(c1)
		print c1

#converge(-2)
converge(1)

