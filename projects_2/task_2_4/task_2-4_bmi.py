weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))
bmi = weight / (height ** 2)

print(f"Введите вес: {weight}(кг)\n Введите рост: {height}(м)\n Отчет о состоянии здоровья\n Рост:\t{height}\n Вес:\t{weight}\n Индекс массы тела: {bmi:.2f}")