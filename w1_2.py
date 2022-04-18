name=input("Student Name:")
surname=input("Student Surname:")
number=input("Student Number:")
courses=[]
for i in range(4):
    course_name=input("Corse 1 Name:")
    visa=int(input("Visa " + course_name +" point: "))
    final=int(input("Final " + course_name +" point: "))
    result=visa*0.4+final*0.6

    if result<50:
        print(course_name+ " Result is Failed")
    elif result>=50:
        print(course_name+ " Result is Passed")



