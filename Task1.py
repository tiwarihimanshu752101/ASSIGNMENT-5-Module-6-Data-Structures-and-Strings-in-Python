student_marks = {
    "ram":20,"mohan":30,
    "ravi":40,"aman":50,
    "abhi":49,"dilip":44
}

name= input("Enter the student's name:")
if name in student_marks:

    print("{}'s  marks is: {}".format(name,student_marks[name]))
else:
    print("student not found")