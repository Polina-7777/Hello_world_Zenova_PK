#!/bin/bash
echo "Введите массу в килограммах:"
read weight
echo "Введите рост в метрах:"
read height
bmi=$(echo "scale=2; $weight / ($height * $height)" | bc -l)
bmi_int=$(printf "%.0f" "$bmi")
echo "Результаты расчёта:"
echo "Масса: $weight кг"
echo "Рост: $height м"
echo "Индекс массы тела (BMI): $bmi_int"
