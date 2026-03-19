operator_name = input("Введите имя оператора: ")
pressure_sensor_value = input("Введите текущее занчение давления (Па): ")

with open("sensor_log.txt", "w", encoding = "utf-8") as file:
    file.write(f"Введите имя оператора: {operator_name}\n")
    file.write(f"Введите текущее занчение давления (Па): {pressure_sensor_value}\n")
print("Данные успешно сохранены в sensor_log.txt")