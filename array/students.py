# Average marks
def average_marks(students):
    total = 0
    for s in students:
        total += s["marks"]
    return total / len(students)


# Highest marks
def highest_marks(students):
    top = students[0]
    for s in students:
        if s["marks"] > top["marks"]:
            top = s
    return top


# Count pass students (>=50)
def count_pass(students):
    count = 0
    for s in students:
        if s["marks"] >= 50:
            count += 1
    return count


# Distinction students (>=75)
def distinction_students(students):
    result = []
    for s in students:
        if s["marks"] >= 75:
            result.append(s["name"])
    return result


# Failed students (<35)
def failed_students(students):
    fail = []
    for s in students:
        if s["marks"] < 35:
            fail.append(s)
    return fail


# Sort all students (high → low)
def sort_students_desc(students):
    return sorted(students, key=lambda x: x["marks"], reverse=True)

# students data
students = [
    {"name": "Ranveer", "marks": 45},
    {"name": "Arjun", "marks": 78},
    {"name": "Rahul", "marks": 90},
    {"name": "Kiran", "marks": 32},
    {"name": "Vikram", "marks": 76},
    {"name": "Ajay", "marks": 28}
]

print("Average:", average_marks(students))

topper = highest_marks(students)
print("Topper:", topper["name"], "-", topper["marks"])

print("Pass count:", count_pass(students))

print("Distinction:", distinction_students(students))

print("\nAll Students (High → Low):")
sorted_all = sort_students_desc(students)
for s in sorted_all:
    print(s["name"], "-", s["marks"])