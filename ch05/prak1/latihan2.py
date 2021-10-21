#tidak ada nilai di bawah 60
#nilai mat harus di atas 70
nilai_bi = float(input("Masukkan nilai Bahasa Indonesia : "))
nilai_ipa = float(input("Masukkan nilai IPA : "))
nilai_mat = float(input("Masukkan nilai Matematika : "))
if(nilai_bi >= 60 and nilai_ipa >= 60 and nilai_mat > 70):
    print("Status kelulusan : ", "Lulus")
elif(nilai_bi < 60 or nilai_ipa < 60 or nilai_mat <= 70):
    print("Status kelulusan : ", "TIDAK LULUS")
else:
    print("Maaf input ada yang tidak valid")