def count_words(text, words):
    
    count = 0
    textWordList = text.lower().split()
    for textWord in textWordList:
        for word in words:
            if textWord.startswith(word):
                count +=1
                break            
    if not(:

#if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
#    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
#    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
#                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

print count_words("Bananas, give me bananas!!!", {"banana", "bananas"})
