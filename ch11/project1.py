'''1.	Buatlah function diffDate(x) yang digunakan untuk menghitung 
selisih hari dari tanggal hari ini dengan tanggal 
x (dalam format string ‘YYYY-MM-DD’). Function tersebut mengembalikan 
(return) bilangan bulat yang merupakan selisih tanggal x dengan tanggal 
hari ini. Contoh:

Misalkan tanggal hari ini adalah tanggal ‘2018-12-26’, maka jika function 
dipanggil dengan diffDate(‘2018-12-30’) akan mengembalikan nilai 4.
'''

from datetime import*
def diffDate():
    print('-'*36)
    print('='*5,'Penghitung Selisih Waktu','='*5)
    print('-'*36)
    skrng = datetime.date(datetime.now())
    print('Sekarang tanggal : ',skrng)
    while True:
        pilihtanggal = input('Masukkan tanggal(yyyy-mm-dd) : ')
        try:
            pilihtanggals = pilihtanggal.split('-')
            if(int(pilihtanggals[1]) > 12 or int(pilihtanggals[1]) < 1):
                print('Input waktu salah')
                continue
            if(int(pilihtanggals[2]) > 31 or int(pilihtanggals[2]) < 1):
                print('Input waktu salah')
                continue
            tahunplhn = int(pilihtanggals[0])
            selisihtahun = skrng.year - tahunplhn
            bulanplhn = int(pilihtanggals[1])
            selisihbln = skrng.month - bulanplhn
            hariplhn = int(pilihtanggals[2])
            selisihhari = skrng.day - hariplhn
            if(selisihhari <= 0):
                selisihhari = ~selisihhari + 1
            if(selisihbln <= 0):
                selisihbln = ~selisihbln + 1
            if(selisihtahun <= 0):
                selisihtahun = ~selisihtahun + 1
            print('Selisih waktu tersebut dan waktu sekarang : ',selisihhari,'hari ',selisihbln,'bulan ',selisihtahun,'tahun')
        except TypeError:
            print('Input waktu salah')
        except IndexError:
            print('Input waktu salah')
        except ValueError:
            print('Input waktu salah')
        lagi = str(input('lagi(y/n)? : '))
        if(lagi == 'y' or lagi == 'Y'):
            True
        elif(lagi == 'n' or lagi == 'N'):
            break
        else:
            print('Input data salah')
            continue
    return 
diffDate()

