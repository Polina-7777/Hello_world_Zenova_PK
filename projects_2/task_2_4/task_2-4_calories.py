weight_of_protein_in_product = int(input("Введите массу белков в продукте (г):"))
weight_of_lipids_in_product = int(input("Ведите массу жиров в продукте (г):"))
weight_of_carbohydrates_in_product = int(input("Ведите массу углеводов в продукте (г):"))

cal = (weight_of_protein_in_product * 4) + (weight_of_lipids_in_product * 9) + (weight_of_carbohydrates_in_product * 4)
print(f"{cal}")