boy = int(input("Boyunuzu cm olarak giriniz : "))
kilo = float(input("Kilonuzu tam olarak giriniz : "))

bki= kilo /((boy/100)**2)


if bki < 25:
    print("Beden kitle indeksiniz Normal. Boyle devam edin.")
    
elif 25 <= bki < 30 :
    print("Beden kitle indeksiniz Fazla Kilolu. Bu gidis gidis degil. Bak soylemedi deme.")

elif 30 <= bki < 40 :
    print("Beden kitle indeksiniz Obez. Yavas ye bogulacan.")

else:
    print("Beden kitle indeksiniz Asiri Sisman. Olmusun aglayanin yok.")