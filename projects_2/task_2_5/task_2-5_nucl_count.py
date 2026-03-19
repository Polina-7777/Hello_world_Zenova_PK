dna = input("Введите последовательность ДНК: ")
dna_up = str.upper(dna)
count_A = dna_up.count("A")
count_T = dna_up.count("T")
count_G = dna_up.count("G")
count_C = dna_up.count("C")

print(f"Анализ последовательности ДНК\n Введите последовательность ДНК: {dna}\n Последовательность в верхнем регистре: {dna_up}\n Подсчёт нуклеотидов:\n A: {count_A}\n T: {count_T}\n G: {count_G}\n C: {count_C}")