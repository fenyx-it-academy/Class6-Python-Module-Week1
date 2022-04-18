weight=float(input("Please write your weight:"))
height=float(input("Please write your height:"))
bodyMassIndex=weight/(height**2)
if bodyMassIndex<25:
    print("NORMAL")
elif 25<=bodyMassIndex<30:
    print("OVER WEIGHT")
elif 30<=bodyMassIndex<40:
    print("OBSE")
else:
    print("EXTREMELY OBSE")