while True: 
    print('Welcome to Body Mass Index(BMI) Calculator ')
    weight = int(input('Please Enter Your Weight in kg : '))
    height = int(input('Please Enter Your Height in cm : '))
    bmi = (weight/height**2)*10000
    if bmi<25:
        print("You are NORMAL")
    elif 25<bmi<30:
        print("You are OVERWEIGHT")
    elif 30<=bmi<40:
        print("You are OBESE")
    else:
        print("You are EXTREMELY OBESE")
    choice = input("Do you want to Evaluate Another Person? Press Y for Yes, N for N0 --->")
    if choice.upper() =='N':
        print('Thanks for Using The Program. BYE...')
        break
