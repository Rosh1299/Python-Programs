'''
WAP to create multidimenssional array for 3 students for english, maths and science and
print the total of English, Maths and Science for every student

Example:

            English      Maths      Science       Total_Marks

ABC          50            50         50               150

XYZ          80            80         80               240

PQR 	     90            90         90               270
'''


result = []
for i in range(1, 4):
    student_list = []
    student = input(f"Enter student-{i} name:")
    print("Enter your marks:")
    english = int(input("English:"))
    maths = int(input("Maths:"))
    science = int(input("Science:"))
    total_marks = english+maths+science
    student_list.append(student)
    student_list.append(english)
    student_list.append(maths)
    student_list.append(science)
    student_list.append(total_marks)

    result.append(student_list)


print("Student Name\tEnglish\tMaths\tScience\tTotal Marks")
for i in range(len(result)):
    print(result[i][0], "\t\t", result[i][1], "\t", result[i]
          [2], "\t", result[i][3], "\t", result[i][4])
