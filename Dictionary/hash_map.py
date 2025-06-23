students = {
    "Alice": 91,
    "Bob": 78,
    "Charlie": 85,
    "Diana": 95,
    "Evan": 62
}

for key, value in students.items():
    print(key, ": ", value)


count = 0
for key, value in students.items():
    if value > 80:
        count += 1

print(count)

sum = 0

for key, value in students.items():
    sum += value

avg = sum/len(students)
print(avg)

print("Top scorer is : ", max(students, key=students.get))