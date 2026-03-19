required_volume_of_solution = int(input("Введите нужный объем раствора (мл): "))

required_mass_fraction_of_salt1 = required_volume_of_solution * 0.009
required_mass_fraction_of_salt2 = round(required_mass_fraction_of_salt1, 2)

with open("recipe2.txt", "w", encoding = "utf-8") as file:
    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n")
    file.write(f"Общий объем: {required_volume_of_solution} мл\n")
    file.write(f"Масса соли = {required_mass_fraction_of_salt2} г \n")
    file.write(f"Объем воды: {required_volume_of_solution}")