oyuncu_1 = input("1. Oyuncu Adiniz : ")
oyuncu_2 = input("2. Oyuncu Adiniz : ")


oyuncu_1_skor = 0
oyuncu_2_skor = 0

tur = 1

while tur < 11 :
    
    oyuncu_1_tercih = input("1. oyuncunun tercihi (T - K - M) : ") 
    oyuncu_2_tercih = input("2. oyuncunun tercihi (T - K - M) : ") 
    
    if oyuncu_1_tercih == 'T' and oyuncu_2_tercih == 'M' :
        print(oyuncu_1 + ", " + str(tur) + ". eli kazandi")
        tur += 1
        oyuncu_1_skor += 1
    elif oyuncu_1_tercih == 'T' and oyuncu_2_tercih == 'K' :
        print(oyuncu_2 + ", " + str(tur) + ". eli kazandi")
        tur += 1
        oyuncu_2_skor += 1
    elif oyuncu_1_tercih == 'K' and oyuncu_2_tercih == 'M' :
        print(oyuncu_2 + ", " + str(tur) + ". eli kazandi")
        tur += 1
        oyuncu_2_skor += 1
    elif oyuncu_1_tercih == 'K' and oyuncu_2_tercih == 'T' : 
        print(oyuncu_1 + ", " + str(tur) + ". eli kazandi")
        tur += 1
        oyuncu_1_skor += 1
    elif oyuncu_1_tercih == 'M' and oyuncu_2_tercih == 'K' :
        print(oyuncu_1 + ", " + str(tur) + ". eli kazandi")
        tur += 1
        oyuncu_1_skor += 1
    elif oyuncu_1_tercih == 'M' and oyuncu_2_tercih == 'T' :
        print(oyuncu_2 + ", " + str(tur) + ". eli kazandi")
        tur += 1
        oyuncu_2_skor += 1
    else:
        print("Tercihler ayni. Tekrar edin")

else:
    print("Oyun bitti")
    if oyuncu_1_skor > oyuncu_2_skor:
        print("{} kazandi. Skor {} - {}".format(oyuncu_1, oyuncu_1_skor, oyuncu_2_skor))
    elif oyuncu_2_skor > oyuncu_1_skor:
        print("{} kazandi. Skor {} - {}".format(oyuncu_2, oyuncu_2_skor, oyuncu_1_skor))
    else:
        print("Oyun berabere.")   