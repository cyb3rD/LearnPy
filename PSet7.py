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
		self.word = word

	def isWordIn(text):
		myText = ''
		result = false
		for w in text.split():
			for s in string.punctuation:
				if s in w:
					myText += w.replace(s, ' ')
		if self.word in myText:
			result = True
		return result

# TitleTrigger
class TitleTrigger(WordTrigger):
	def evaluate(self,word,title):
		WordTrigger(word)
		return WordTrigger.isWordIn(title)
# SubjectTrigger
class SubjectTrigger(WordTrigger):
	def evaluate(self, word, subject):
		WordTrigger(word)
		return WordTrigger.isWordIn(subject)

# SummaryTrigger
class SummaryTrigger(WordTrigger):
	def evaluate(self, word, summary):
		WordTrigger(word)
		return WordTrigger.isWordIn(summary)



