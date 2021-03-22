class Masuk:
	def __init__(self, am=''):
		self.am = am

	def masukan(self):
		while self.am.isdigit()==False:
			self.am = input('Masukkan Angka Saja :\n')
			if self.am.isdigit()==False:
				continue
			else:
				return self.am

class Iris(Masuk):				
	def __init__(self, am='', st=[], rb=[], jt=[]):
		self.am = am
		self.st = st
		self.rb = rb
		self.jt = jt

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

def cek():
	print('oyee')