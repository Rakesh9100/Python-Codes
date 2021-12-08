#Hybrid inheritance : Two or more types of inheritance are combined together.

##Write a program to create a superclass named as College. Further create two
#child of it named as Faculty and Student.Finally create a class derived from
#both of then which should be named as subject.Assume suitable data members and
#member function to perform hybrid inheritance.

class college:
    def college_name(self):
        print("College name: LPU")

class faculty(college):
    def faculty_name(self):
        print("Faculty name: Sagar sir")

class student(college):
    def student(self,name,section):
        print("Student name:",name)
        print("student section:",section)

class subject(faculty,student):
    def subject_name(self):
        print("subject name: Python")

s1 = subject()
s1.student('Rakesh','K20BE')
s1.faculty_name()
s1.college_name()
