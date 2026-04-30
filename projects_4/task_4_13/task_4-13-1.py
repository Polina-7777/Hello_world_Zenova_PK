A = float(input("Введите число A: "))
B = float(input("Введите число B: "))
C = float(input("Введите число C: "))
D = float(input("Введите число D: "))

Min = A

if Min > B:
    Min = B

if Min > C:
    Min = C

if Min > D:
    Min = D

print("Наименьшее число (Min):", Min)