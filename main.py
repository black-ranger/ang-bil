'''
Mengkonversi angka menjadi bilangan.
Alur :
	1. Menginput hanya berupa angka saja
	2. Mengiris reserve index tiap 3 angka (memisah antara satuan, ribuan, dan jutaan)
	3. Mengkonversi karakter angka menjadi bilangan
	4. Output berupa kalimat rapi
'''
from modules import *

ang = Iris()
ang.masukan()
print(ang.am)
ang.potong()

cek()
print(ang.st)