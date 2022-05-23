# # HOMEWORK_2
# User Name, Surname, Student Number, 4 course names, Visa and Final grades will be required.
# The sum of 40% of the midterm grade and 60% of the final grade will give the year-end average.
# If the average is less than 50, “FAILED” on the screen, 50 and above, “PASSED” will be printed on the screen.
# This printing process is in 4 lessons. will be done and the lessons will be written one after the other.

userName=input('Please enter an username: ')
surname=input('Please enter a surname: ')
studentNumber=int(input('Please enter student number: '))
courses= ['python','java','matlab','c++']
visaGrades = [0] * (4)
finalGrades = [0] * (4)


for x in range(len(courses)) :
            print("Visa Grade for " + courses[x])
            visa = input()
            visaGrades[x] = visa
            print("Final Grade for " + courses[x])
            finall = input()
            finalGrades[x] = finall
            x+= 1
            
i = 0
while (i < len(courses)) :
            average = float(visaGrades[i]) * 0.4 + float(finalGrades[i]) * 0.6
            if (average < 50) :
                print(courses[i] + ": Failed")
            else :
                print(courses[i] + ": Passed")
            i += 1