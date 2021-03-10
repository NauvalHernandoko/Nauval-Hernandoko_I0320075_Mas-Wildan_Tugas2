#menampilkan informasi program

print("50.5 fahrenheit berapa celcius?")

#input suhu dalam fahrenheit
F = float(input("Masukkan suhu(fahrenheit): "))

#melakukan konversi suhu ke celcius
C = 5 * (F-32) / 9

#menampilkan hasil konversi ke layar
print("Fahrenheit: " ,F)
print("Celcius:" ,C)