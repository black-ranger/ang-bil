class Convert:
	def __init__(self, am=[]):
		self.am = am

	def masukan(self):
		self.am = str(self.am)
		while self.am.isdigit()==False:
			self.am = input('Masukkan Angka Saja :\n')
			if self.am.isdigit()==False:
				continue
			else:
				self.am = list(map(int, self.am))
				return self.am

	def potong(self):
		if type(self.am) != list:
			self.am = list(map(int, self.am))
		for i in self.am[::-1]:
			if len(st.am) < 3:
				st.am.append(i)
			elif len(rb.am) < 3:
				rb.am.append(i)
			else:
				jt.am.append(i)

#st, rb, jt = st[::-1], rb[::-1], jt[::-1]

#	def potong(self):
#		self.am = list(map(int, self.am))
#		for i in self.am[::-1]:
#			if len(self.st) < 3:
#				self.st.append(i)
#			elif len(self.rb) < 3:
#				self.rb.append(i)
#			else:
#				self.jt.append(i)
#		self.st, self.rb, self.jt = self.st[::-1], self.rb[::-1], self.jt[::-1]
		
#		def index1(self):
			
tes = Convert()
st = Convert()
rb = Convert()
jt = Convert()

print(tes.am)
tes.masukan()
tes.potong()
print(st.am)
print(rb.am)