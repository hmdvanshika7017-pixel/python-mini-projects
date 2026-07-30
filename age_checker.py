# Age Checker - Day 1 of 100 Days of Python

name = input("Apna naam likho: ")
age = int(input("Apni age likho: "))

if age >= 18:
    print(f"{name}, tum vote de sakte ho!")
else:
    print(f"{name}, tum abhi chote ho. {18-age} saal baad vote de paoge.")