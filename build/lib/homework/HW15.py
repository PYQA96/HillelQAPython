import csv
import json

# Запис у файл та виведення вмісту
with open("example.txt", "w") as file:
    file.write("Це перший рядок.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Додавання другого рядка
with open("example.txt", "a") as file:
    file.write("Це другий рядок.\n")

# Виведення всіх рядків
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Зчитування користувацьких рядків
with open("example.txt", "a") as file:
    while True:
        user_input = input("Введіть рядок (або 'exit' для завершення): ")
        if user_input.lower() == 'exit':
            break
        file.write(user_input + "\n")

# Зчитування CSV та виведення вмісту
with open('SampleCSVFile_11kb.csv', newline='') as csvfile:

    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(', '.join(row))

# Зчитування JSON та виведення вмісту
with open('sample2.json') as jsonfile:
    data = json.load(jsonfile)
    print(json.dumps(data, indent=2))
