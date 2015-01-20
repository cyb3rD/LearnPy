s = 'azcbobobegghakl'
#s = 'abcbcd'
lenS = len(s)
index = 0
strAlpha = s[index]
strAlphaArray = ''

while index < lenS:
    if index+1 == lenS:
        strAlphaArray += strAlpha
        break
    if ( ord(s[index]) <= ord(s[index+1]) ):
        strAlpha += s[index+1]
        index += 1
    else:
        index += 1
        strAlphaArray += (strAlpha + ' ')
        strAlpha = s[index]
        
#print strAlphaArray

splitStrAlpha = strAlphaArray.split()
#print splitStrAlpha

result = splitStrAlpha[0]
for st in splitStrAlpha:
    if len(st) > len(result):
        result = st
        
print 'Longest substring in alphabetical order is: ' + result

    