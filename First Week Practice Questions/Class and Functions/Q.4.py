# Python program to crate two empty classes, Student and Marks. Now create some
# instances and check whether they are instances of the said classes or not. Also,
# check whether the said classes are subclasses of the built-in object class or not.

class Student:
    pass


class Marks:
    pass


student_1 = Student()
marks_1 = Marks()
print("Instance or Not?", isinstance(student_1, Student))
print("Instance or Not?", isinstance(marks_1, Student))
print("Instance or Not?", isinstance(marks_1, Marks))

print("Subclass or Not?", issubclass(Student, object))
print("Subclass or Not?", issubclass(Marks, object))
