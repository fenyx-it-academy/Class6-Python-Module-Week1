ad = input('Adiniz : ')
soyad = input('Soyadiniz : ')
no = input('Ogrenci numaraniz : ')

ders_1 = input('Ders 1 : ')
ders_1_vize = int(input('Ders 1 vize notunuz : '))
ders_1_final = int(input('Ders 1 final notunuz : '))

ders_2 = input('Ders 2 : ')
ders_2_vize = int(input('Ders 2 vize notunuz : '))
ders_2_final = int(input('Ders 2 final notunuz : '))

ders_3 = input('Ders 3 : ')
ders_3_vize = int(input('Ders 3 vize notunuz : '))
ders_3_final = int(input('Ders 3 final notunuz : '))

ders_4 = input('Ders 4 : ')
ders_4_vize = int(input('Ders 4 vize notunuz : '))
ders_4_final = int(input('Ders 4 final notunuz : '))

ders_1_ortalama = (ders_1_vize * 0.4) + (ders_1_final * 0.6)
ders_2_ortalama = (ders_2_vize * 0.4) + (ders_2_final * 0.6)
ders_3_ortalama = (ders_3_vize * 0.4) + (ders_3_final * 0.6)
ders_4_ortalama = (ders_4_vize * 0.4) + (ders_4_final * 0.6)

dersler_ortalama = [ders_1_ortalama, ders_2_ortalama, ders_3_ortalama, ders_4_ortalama]

print("Sayin {} {}, bu donem almis oldugunuz \n1. {}, \n2.{}, \n3.{} ve \n4.{} derslerinin yil sonu basari durumu asagida sirayla gosterilmistir.".format(ad, soyad, ders_1, ders_2, ders_3, ders_4))

for i in dersler_ortalama:
    if(i < 50):
        print("Kaldı")
    else:
        print("Geçti")
        