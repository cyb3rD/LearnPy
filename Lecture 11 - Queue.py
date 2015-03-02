class Queue(object):
	def __init__(self):
		self.vals=[]

	def insert(self, el):
		self.vals.append(el)

	def remove(self):
		try:
			return self.vals.pop()
		except IndexError:
			raise ValueError
		except ValueError:
		        print 'It did raise \'ValueError\'!'
		
