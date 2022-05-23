# HOMEWORK_3
# Parameter showing whether a person's weight is normal for their height.
# It is called Body Mass Index. In short, a person's weight is equal to a person's height.
# If we divide it by its square, the body mass index is obtained.
# User's weight and height If the result by taking the length is below 25, NORMAL,
# if it is between 25-30 OVER WEIGHT,
# OBSE if 30-40,
# EXTREMELY OBSE if 40 and over print a warning

height = float(input("Please enter your height(meter): "))
weight = int(input("Please enter your weight(kg): "))
bodyMassIndex = weight/(height**2)
if bodyMassIndex<=25:
    print(bodyMassIndex, "NORMAL")
elif 25<bodyMassIndex<=30:
    print(bodyMassIndex, "OVER WEIGHT")
elif 30<bodyMassIndex<=40:
    print(bodyMassIndex, "OBSE")
elif bodyMassIndex>40:
    print(bodyMassIndex, "EXTREMELY OBSE")
    print("WARNING!!!")