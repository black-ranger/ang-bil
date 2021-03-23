class Convert:
	def __init__(self, am='', st=[], rb=[], jt=[]):
		self.am = am
		self.st = st
		self.rb = rb
		self.jt = jt

	def masukan(self):
		while self.am.isdigit()==False:
			self.am = input('Masukkan Angka Saja :\n')
			if self.am.isdigit()==False:
				continue
			else:
				return self.am

	def potong(self):
		self.am = list(map(int, self.am))
		for i in self.am[::-1]:
			if len(self.st) < 3:
				self.st.append(i)
			elif len(self.rb) < 3:
				self.rb.append(i)
			else:
				self.jt.append(i)
		self.st, self.rb, self.jt = self.st[::-1], self.rb[::-1], self.jt[::-1]
		
#		def index1(self):
			

def cek():
	print(coba)