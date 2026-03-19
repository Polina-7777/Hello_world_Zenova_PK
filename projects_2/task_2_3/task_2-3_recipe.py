name_of_substance = input("Введите название среды:")
concentration_of_agar = input("Введите концентрацию агара (%):")
sterilization_temperature = input("Температура стерилизации:")

with open("recipe.txt", "w", encoding = "utf-8") as file:
    file.write(f"Введите название питательной среды: {name_of_substance}\n")
    file.write(f"Ведите концентрацию агара (%): {concentration_of_agar}\n")
    file.write(f"Температура стерилизации: {sterilization_temperature}")
print("Файл 'recipe.txt' успешно сформирован!")