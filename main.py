'''
Mengkonversi angka menjadi bilangan.
Alur :
	1. Menginput hanya berupa angka saja
	2. Mengiris reserve index tiap 3 angka (memisah antara satuan, ribuan, dan jutaan)
	3. Mengkonversi karakter angka menjadi bilangan
	4. Output berupa kalimat rapi
'''
from modules import *

ang = Convert()
ang.masukan()
ang.potong()
#print(ang.jt)
#print(ang.rb)
#print(ang.st)
if len(ang.st) == 1:
	ang.st[-1] = bil_satuan[ang.st[-1]]
#	print(ang.st)
elif len(ang.st) == 2:
	if ang.st[-2] != 1:
		ang.st[-2] = bil_satuan[ang.st[-2]] + ' puluh'
		if ang.st[-1] != 0:
			ang.st[-1] = bil_satuan[ang.st[-1]]
		else:
			ang.st.pop(-1)
#		print(ang.st)
	else:
		if ang
		ang.st[-1]
else:
	print('failed')
for i in ang.st:
	print(i, end=' ')