def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    import string
    coderDict = {}

    srcString = string.ascii_lowercase
    i = 0
    
    for c in srcString:
        if i+shift > 25:
            coderDict[c] = srcString[i+shift-26]
            coderDict[c.capitalize()] = srcString[i+shift-26].capitalize()
        else:
            coderDict[c] = srcString[i+shift]
            coderDict[c.capitalize()] = srcString[i+shift].capitalize()
        i += 1

    return coderDict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    encodedText = ""
    for c in text:
        if coder.has_key(c):
            encodedText += coder[c]
        else:
            encodedText += c
    print encodedText

def applyShift(text, shift):    
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))
    
applyShift('Bpqa qa i bmab.', 18)