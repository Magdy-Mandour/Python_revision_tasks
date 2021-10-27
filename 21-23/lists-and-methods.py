# ------------------------------------------------------------
# Assignments For Lessons 21 To 23
# https://elzero.org/python-assignments-lesson-from-21-to-23/
# ------------------------------------------------------------


# Task 1
friends1 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print("#" * 20)
print("###### Task 1 ######")
print("#" * 20)

print(friends1[:1])  # This Is Wrong => Return List Element
print(friends1[0])
print(friends1.pop(0))  # This Is New Solution
print(friends1[-1])
print(friends1.pop())

# Task 2

friends2 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print("#" * 20)
print("###### Task 2 ######")
print("#" * 20)

print(friends2[1::2])  # ['Ahmed', 'Ali']
print(friends2[::2])  # ['Osama', 'Sayed', 'Mahmoud']

# Task 3

friends3 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print("#" * 20)
print("###### Task 3 ######")
print("#" * 20)

print(friends3[1:4])
print(friends3[-2:])


# Task 4

friends4 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print("#" * 20)
print("###### Task 4 ######")
print("#" * 20)

friends4[-2:] = ["Elzero", "Elzero"]
print(friends4)


# Task 5

print("#" * 20)
print("###### Task 5 ######")
print("#" * 20)

friends5 = ["Osama", "Ahmed", "Sayed"]

friends5.insert(0, "Mandour")
friends5.append("Magdy")

print(friends5)


# Task 6

friends6 = ['Fadia', 'Osama', 'Ahmed', 'Sayed', 'Salwa']

print("#" * 20)
print("###### Task 6 ######")
print("#" * 20)

friends6 = friends6[2:]

print(friends6)  # ['Ahmed', 'Sayed', 'Salwa']

friends6 = friends6[:-1]

print(friends6)  # ['Ahmed', 'Sayed']

# Task 7

friends7 = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

print("#" * 20)
print("###### Task 7 ######")
print("#" * 20)

friends7.extend(employees)
friends7.extend(school)

print(friends7)  # ['Ahmed', 'Sayed', 'Samah', 'Eman', 'Ramy', 'Shady']

# Task 8

friends8 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print("#" * 20)
print("###### Task 8 ######")
print("#" * 20)

friends8.sort()

print(friends8)  # ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']

friends8.sort(reverse=True)

print(friends8)  # ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

# Task 9

friends9 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print("#" * 20)
print("###### Task 8 ######")
print("#" * 20)

print(len(friends9))  # 6

# Task 10

print("#" * 21)
print("###### Task 10 ######")
print("#" * 21)

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])
