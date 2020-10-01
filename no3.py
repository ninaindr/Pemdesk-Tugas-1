print("==============Penghitungan BMI==============")

tinggi=float(input("Masukkan tinggi badan (dalam satuan m (misal 164 cm jadi 1.64) : "))
berat=float(input("Masukkan berat badan (dalam satuan kg) : "))
bmi=berat/(tinggi*tinggi)
print ("hasil hitungan : " ,bmi)

if bmi < 18.5:
    print("Berat badan kurang")
elif 18.5 <= bmi <= 22.9:
    print("Berat badan normal")
elif 23 <= bmi <= 30:
    print("Berat badan berlebih (cenderung obesitas)")
else:
    print("Obesitas")
