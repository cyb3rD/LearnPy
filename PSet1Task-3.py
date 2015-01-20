#s = 'azcbobobegghakl'
s = 'abcbcd'
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
        
print strAlphaArray



    