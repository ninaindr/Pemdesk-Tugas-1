#mencari nilai minimal dan maksimal

def angkamin(angka1):
    minimal=9999999
    for y in angka1:
        if y<minimal:       #proses pencarian angka min
            minimal=y
    return minimal

def angkamax(angka2):
    maksimal=0
    for x in angka2:
        if x>maksimal:      #proses pencarian angka max
            maksimal=x
    return maksimal

jumlahangka=[] #list untuk menampung inputan
angka=int(input("masukkan banyaknya nilai yang diinginkan : "))
for n in range(angka):
    nilai=int(input("masukkan nilai : "))
    jumlahangka.append(nilai)
print("Nilai Minimal : ", angkamin(jumlahangka))
print("Nilai Maksimal : ", angkamax(jumlahangka))

