#program validasi username dan password

username="nina"
password="1234"

for i in range(3):
    uname = input("Masukkan Username : ")
    pas = input("Masukkan Password : ")
    j=3
    if(uname==username and pas==password):
        print("Anda berhasil masuk")
        break
    else:
        print("maaf username dan password anda salah")
        continue
print("Silahkan coba lagi nanti")
