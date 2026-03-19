count_of_whole_capsules = int(input("Введите общее количество капсул: "))
capacity_of_one_package = int(input("Введите вместимость одной упаковки: "))

count_of_fulled_packeges = count_of_whole_capsules // capacity_of_one_package
count_of_remaining_capsules = count_of_whole_capsules % capacity_of_one_package

print(f"Введите общее количество произведенных капсул: {count_of_whole_capsules}\n Введите количество капсул в одной упаковке: {capacity_of_one_package}\n Отчет фасовочного цеха\n Полных упаковок:\t{count_of_fulled_packeges}\n Остаток капсул:\t{count_of_remaining_capsules}")