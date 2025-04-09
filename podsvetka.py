# task 1
name = input("Введіть ім'я: ")
surname = input("Введіть прізвище: ")
age = float(input("Введіть вік: "))
city = input("Введіть місто: ")

print(f"{name:<10} {surname}, {age:.2f} років, місто: {city:>15}")


#task 2

products = [
    ["Хліб", 24.5, 2],
    ["Молоко", 32.0, 1],
    ["Сир", 210.75, 3],
]

print("{:<20}{:>10}{:^8}".format("Назва товару", "Ціна", "К-сть"))
for item in products:
    print("{:<20}{:>10.2f}{:^8}".format(item[0], item[1], item[2]))

#task 3

students = [
    ["Іван", 89.25, 95],
    ["Оля", 76.5, 88],
    ["Андрій", 92.0, 100],
]

print("Звіт про успішність студентів\n")
print("{:<10}{:>15}{:>20}".format("Ім'я", "Середній бал", "Відвідуваність (%)"))

for s in students:
    print("{:<10}{:>15.2f}{:>20}".format(s[0], s[1], s[2]))

avg_grade = sum(s[1] for s in students) / len(students)
print("\n{:<10}{:>15.2f}".format("Середній бал:", avg_grade))

