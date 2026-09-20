students = ["Harini", "Anu", "Ravi", "Kiran"]

student_iterator = iter(students)

try:
    print("First Element:", next(student_iterator))
    print("Second Element:", next(student_iterator))
    print("Third Element:", next(student_iterator))
    print("Fourth Element:", next(student_iterator))
    print("Fifth Element:", next(student_iterator))

except StopIteration:
    print("Iterator has no more elements.")
