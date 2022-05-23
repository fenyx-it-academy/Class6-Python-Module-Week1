student_report = {}
while True:  # This makes the program to run until the break statement
    print('Welcome to Student Report Program ')
    student_name = input('Please Enter the Student Name : ')
    student_report['Name'] = student_name
    student_surname = input('Please Enter the Student Surname : ')
    student_report['Surname'] = student_surname
    student_number = int(input('Please Enter the Student Number : '))
    student_report['Number'] = student_number
    course1_name = input('Please Enter the Course 1 : ')
    student_report['First Course'] = course1_name
    course1_visa = int(input('Please Enter the Visa Grade of the First Course :'))
    student_report['Course1_visa'] = course1_visa
    course1_final = int(input('Please Enter the Final Grade of the First Course :'))
    student_report['Course1_final'] = course1_final
    course2_name = input('Please Enter the Course 2 : ')
    student_report['Second Course'] = course2_name
    course2_visa = int(input('Please Enter the Visa Grade of the Second Course :'))
    student_report['Course2_visa'] = course2_visa
    course2_final = int(input('Please Enter the Final Grade of the Second Course :'))
    student_report['Course2_final'] = course2_final
    course3_name = input('Please Enter the Course 3 : ')
    student_report['Third Course'] = course3_name
    course3_visa = int(input('Please Enter the Visa Grade of the Third Course :'))
    student_report['Course3_visa'] = course3_visa
    course3_final = int(input('Please Enter the Final Grade of the Third Course :'))
    student_report['Course3_final'] = course3_final
    course4_name = input('Please Enter the Course 4 : ')
    student_report['Fourth Course'] = course4_name
    course4_visa = int(input('Please Enter the Visa Grade of the Fourth Course :'))
    student_report['Course4_visa'] = course4_visa
    course4_final = int(input('Please Enter the Final Grade of the Fourth Course :'))
    student_report['Course4_final'] = course4_final
    for key,value in student_report.items():
        print(key,value)
    course1_average = ((course1_visa*40/100)+(course1_final*60/100))
    course2_average = ((course2_visa*40/100)+(course2_final*60/100))
    course3_average = ((course3_visa*40/100)+(course3_final*60/100))
    course4_average = ((course4_visa*40/100)+(course4_final*60/100))
    result={}
    if course1_average<50:
        result1 ='FAILED'
    else:
        result1 ='PASSED'
    result[course1_name]= result1
    if course2_average<50:
        result2 ='FAILED'
    else:
        result2 ='PASSED'
    result[course2_name]= result2
    if course3_average<50:
        result3 ='FAILED'
    else:
        result3 ='PASSED'
    result[course3_name]= result3
    if course4_average<50:
        result4 ='FAILED'
    else:
        result4 ='PASSED'
    result[course4_name]= result4
    for key,value in result.items():
        print(key,value)
    choice = input("Do you want to Enter Another Student? Press Y for Yes, N for N0 --->")
    if choice.upper() =='N':
        print('Thanks for Using The Program. BYE...')
        break
