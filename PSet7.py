'''
Problem Set 6: RSS Feed Classes
'''
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


