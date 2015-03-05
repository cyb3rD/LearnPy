#======================
# Part 1
# Data structure design
#======================

# Problem 1

# NewsStory

class NewsStory(object):
	def __init__(self, guid, title, subject, summary, link):
		self.newsGuid = guid
		self.newsTitle = title
		self.newsSubject = subject
		self.newsSummary = summary
		self.newsLink = link

	def getGuid(self):
		return self.newsGuid
	def getTitle(self):
		return self.newsTitle
	def getSubject(self):
		return self.newsSubject
	def getLink(self):
		return self.newsLink
	def getSummary(self):
		return self.newsSummary
#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# WordTrigger
class WordTrigger(Trigger):
	def __init__(self, word):
		self.word = word.lower() # word for search in text

	def isWordIn(self, text):
		txtPunctuation = string.punctuation
		
		for p in txtPunctuation:
			text = text.replace(p, ' ')
		
		text = text.lower().split(' ')

		return self.word in text
		
# TitleTrigger
class TitleTrigger(WordTrigger):
	def evaluate(self,story):
		#WordTrigger(word)
		return self.isWordIn(story.getTitle())
# SubjectTrigger
class SubjectTrigger(WordTrigger):
	def evaluate(self, story):
		#WordTrigger(word)
		return self.isWordIn(story.getSubject())

# SummaryTrigger
class SummaryTrigger(WordTrigger):
	def evaluate(self, story):
		#WordTrigger(word)
		return self.isWordIn(story.getSummary())

class NotTrigger(Trigger):
 
    def __init__(self, t1):
        self.t1 = t1
 
    def evaluate(self, story):
        return not self.t1.evaluate(story)
 
 
class AndTrigger(Trigger):
 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
 
    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)
 
        
class OrTrigger(Trigger):
 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
 
    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)

class PhraseTrigger(Trigger):
 
    def __init__(self, phrase):
        self.phrase = phrase
 
    def isPhraseIn(self,text):
        return self.phrase in text
 
    def evaluate(self, story):
        if self.isPhraseIn(story.getTitle()):
            return True
        if self.isPhraseIn(story.getSummary()):
            return True
        if self.isPhraseIn(story.getSubject()):
            return True
        return False

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.
 
    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")
 
    Modifies triggerMap, adding a new key-value pair for this trigger.
 
    Returns: None
    """
    # TODO: Problem 11
    if triggerType == "TITLE":
        triggerMap[name] = TitleTrigger(params[0])
 
    elif triggerType == "SUBJECT":
        triggerMap[name] = SubjectTrigger(params[0])
 
    elif triggerType == "SUMMARY":
        triggerMap[name] = SummaryTrigger(params[0])
 
    elif triggerType == "NOT":
        triggerMap[name] = NotTrigger(triggerMap[params[0]])
 
    elif triggerType == "AND":
        triggerMap[name] = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
 
    elif triggerType == "OR":
        triggerMap[name] = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
 
    elif triggerType == "PHRASE":
        triggerMap[name] = PhraseTrigger(' '.join(params))
 
    return triggerMap[name]
