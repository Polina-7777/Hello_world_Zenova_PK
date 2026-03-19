pH = float(input("Введите значение pH: "))
if pH == 7:
    print("Нейтральная среда")
elif pH < 7:
    print("Кислая среда")
else:
    print("Щелочная среда")