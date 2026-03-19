name_of_worker = input("ФИО исследователя: ")
date = input("Дата: ")
name_of_experiment = input("Название эксперимента: ")
final_result = input("Вывод: ")

with open("journal.txt", "w", encoding = "utf-8") as file:
    file.write(f"Электронный лабораторный журнал\n")
    file.write(f"ФИО исследователя: {name_of_worker}\n")
    file.write(f"Дата: {date}\n")
    file.write(f"Название эксперимента:  {name_of_experiment}\n")
    file.write(f"Вывод: {final_result}\n")