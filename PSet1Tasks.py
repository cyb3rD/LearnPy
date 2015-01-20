s = 'azcbobobegghakl'
target = 'bob'
lenSource = len(s)
lenTarget = len(target)
curPos = 0
cntFounded = 0
iteration = 0

# Task 2 BEGIN
# Main idea:
# 1.Take slice from curPos symbol to lenTarget
# 2. Compare with target
# 	if <> then:
#		incremet counter
#		move curPos to next symbol 
# 		and repeat steps 1 .. 2
#

#while curPos < lenSource:
#	if s[curPos:lenTarget+iteration] == target:
#		cntFounded += 1
#	curPos += 1
#	iteration += 1

#print "Number of times " + str(target) + "occurs is: " + str(cntFounded)
# Task 2 END


#Task 3
strAlphaOrder = ''
# find symbol position in alphabet
def findPosInAlpha (curSymbol):
	alphabet = 'abcdefghijklmnopqrstuywxyz'
	curPos = 0
	for symbol in alphabet:
		if symbol == curSymbol:
			return curPos
		curPos += 1
#get next symbol
def getNextSymbol (index, strSource):
	return strSource[index+1]

index = 0
nextIndex = 0
curPos = 0
lenStrAlpha = 0
iteration = 0
# TEST: print findPosInAlpha('d')
while curPos < lenSource:
	for symbol in s:
		if ord(symbol) < ord(getNextSymbol(curPos,s)):
			strAlphaOrder += symbol

		curPos += 1

print strAlphaOrder
