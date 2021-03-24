
"""
Question 5:-->
A school decided to replace the desks in three
￼
coderclassroom.Each desk sits two students.Given the number of students
in each class, print the smallest possible number of desks that can be purchased.
The program should read the integers: the number of students in each of the three classes a,b and c respectively.
"""

student_Class_A = int(input("Enter the number of students in class A :"))
student_Class_B = int(input("Enter the number of students in class B :"))
student_Class_C = int(input("Enter the number of students in class C :"))
stu_per_desk = 2
total_student = (student_Class_A+student_Class_B+student_Class_C)

desk_to_buy = total_student//stu_per_desk
remaning_stu = total_student % stu_per_desk

print(f"The smallest possible number of desks to be purchased is {desk_to_buy}.")
print(f"{remaning_stu} student will not fit in desk.")














