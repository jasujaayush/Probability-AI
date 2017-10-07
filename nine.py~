import operator

def remove(letters, allowedSetSoFar):
	newSet = allowedSetSoFar
	letters = filter(None, letters)
	for letter in letters:
		if(letter in newSet):
			print "letter",letter
			x = newSet.find(letter)
			newSet = newSet[:x] + newSet[x+1:]
	return newSet

def TopFifteen():
	print ".............Top FifTeen................."
	i = 1;
	for x in sorted_word_prob:
		print i,x
        	i = i+1
        	if i is 16:
        	        break
	print "........................................."

def BottomFifteen():
	print "............Bottom Fifteen..............."
	increasing_word_prob = sorted(word_prob.items(), key=operator.itemgetter(1))
	i = 1
	for x in increasing_word_prob:
        	print i,x
        	i = i+1
        	if i is 16:
               		break	
	print "........................................."

def ProbLetterGivenWord(letter, positions, word):
	for x in positions:
		if word[x] is letter:
			return 1
	return 0;

def ProbabilityOfConstraints(constraints):
	prob = 0.0
	temp = 0.0
	for word in words:
		temp = (word_prob[word]*ProbConstraintsGivenWord(word,constraints))
		prob = prob + temp
	return prob
	
def IsLetterAllowed(letter, constraint):
	return letter in constraint

def ProbConstraintsGivenWord(word, constraints):
	i = 0
	while(i is not 5):
		if (word[i] not in constraints[i]):
			return 0;
		i = i+1
	return 1;

def ProbWordGivenConstraints(word, constraints):
	prob = 0.0
	temp = 0.0
	temp = word_prob[word]
	temp = temp*ProbConstraintsGivenWord(word, constraints)
	temp = temp/ProbabilityOfConstraints(constraints)
	#IsLetterAllowed(word[0], constraint[0])
	prob = temp
	return prob	

def LettersInWord(letters, word):
	for index, value in letters.iteritems():
		if word[index] is value:
			return 1
	return 0; 

def Probability(letters, constraints):
	prob = 0.0
	temp = 0.0
	for word in words:
		temp = ProbWordGivenConstraints(word, constraints)*LettersInWord(letters, word)
		prob = prob + temp
	return prob

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
f = open('words.txt', 'r')
list = f.readlines()
words = []
word_count = {}
word_prob = {}
total_words = 0;
tempCount = 0
for x in list:
	tempCount = int(x.strip().split(' ')[1])
	word = x.strip().split(' ')[0]
	words.append(word)
	if word in word_count:
		word_count[word] = word_count[word] + tempCount
	else:
		word_count[word] = tempCount
	total_words = total_words + tempCount

for key,value in word_count.iteritems():
	word_prob[key] = float(value)/total_words

sorted_word_prob = sorted(word_prob.items(), key=operator.itemgetter(1), reverse = True)
#TopFifteen()
#BottomFifteen()
constraints = {}
letters = {}
print "Enter incorrect guesses separated by comma (ex: A,Z,T). If nothing, press enter"
x = raw_input()
removeLetters = x.split(',') #['A', 'D', 'I', 'E', 'I', 'O', 'S']
#print removeLetters
print "Enter existing alphabets with index (ex: 1 A,4 Z)"
x = raw_input()
existing_letters = filter(None, x.strip().split(','))
#print existing_letters
for t in existing_letters:
	index = int(t.split()[0])
	alphabet = t.split()[1]
	constraints[index] = alphabet
	removeLetters.append(alphabet)

string = remove(removeLetters, alphabets)
#print string
print removeLetters
for i in xrange(0,5):
	if i not in constraints:
		constraints[i] = string
		letters[i] = 'X' #garbage 

print constraints
iterator = 0
while iterator is not 26:
	l = alphabets[iterator]
	iterator = iterator + 1
	for key, value in letters.iteritems():
		letters[key] = l
	#print letters
	#print LettersInWord(letters, "ALOOO")
	print l, Probability(letters, constraints)
	
