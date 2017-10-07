import random
import csv

def f(bits):
	val = 0
	for x in xrange(0,10):
		val = val + (2**x)*bits[x]	
	return val

bits = []
numerator = []
data = []
const = 2.0/3.0
for x in xrange(0,10):
	bits.append(random.randint(0,1))
	numerator.append(0.0)

denominator = 0.0
oneCount = 0
for sample in xrange(0,10000000):
	for x in xrange(0,10):
        	bits[x] = random.randint(0,1)
	oneCount = oneCount + bits[1]
	fb = f(bits)
	numerator[0] = numerator[0] + const*(0.2**abs(128-fb))*int(bits[1] is 1)
	numerator[1] = numerator[1] + const*(0.2**abs(128-fb))*int(bits[3] is 1)
	numerator[2] = numerator[2] + const*(0.2**abs(128-fb))*int(bits[5] is 1)
	numerator[3] = numerator[3] + const*(0.2**abs(128-fb))*int(bits[7] is 1)
	numerator[4] = numerator[4] + const*(0.2**abs(128-fb))*int(bits[9] is 1)
	denominator = denominator + const*(0.2**abs(128-fb))
	if (sample > 10000 and sample%100 is 0):
		entry = [sample]
		for x in xrange(0,5):
        		entry.append(numerator[x]/denominator)
		data.append(entry)

for x in xrange(0,5):
        print (x+1)*2, numerator[x], denominator, numerator[x]/denominator


with open('test.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data)
#print oneCount, numerator, denominator, numerator/denominator
	


	
