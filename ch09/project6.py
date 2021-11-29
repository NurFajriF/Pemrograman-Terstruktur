'''6.	Modifikasilah program dari hasil nomor 3, supaya diperoleh tabel sebagai berikut
Keterangan:
-	Nilai akhir diperoleh dari rumus (Nilai MID + 2 Nilai UAS)/3
-	Status nantinya hanya terdiri dari LULUS atau TIDAK LULUS. 
Dikatakan statusnya LULUS jika Nilai Akhirnya lebih atau sama dengan 60. Sedangkan jika kurang dari 60 maka TIDAK LULUS
'''
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print('==============================================================')
print('NIM	  NAMA	     N.MID	 N.UAS	  N.AKHIR  STATUS')
print('--------------------------------------------------------------')
for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(9),end='')
    print(nilai[i]['nama'].ljust(12),end='')
    print(str(nilai[i]['mid']).rjust(5),end='')
    print(str(nilai[i]['uas']).rjust(10),end='')
    nilaiakhir = (nilai[i]['mid'] + 2*nilai[i]['uas'])//3
    if(nilaiakhir >= 60 ):
        status = 'LULUS'
    elif(nilaiakhir <60):
        status = 'TIDAK LULUS'
    print(str(nilaiakhir).rjust(10),end='' )
    print(status.center(14))

print('--------------------------------------------------------------')

