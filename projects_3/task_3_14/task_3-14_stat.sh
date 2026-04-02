#!/bin/bash
FILE="students.txt"
echo "=== Статистика оценок ==="
sum=$(awk '{sum += $2} END {print sum}' "$FILE")
echo "Сумма всех оценок: $sum"
average=$(awk '{sum += $2; count++} END {printf "%.2f", sum/count}' "$FILE")
echo "Средняя оценка: $average"
max=$(awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' "$FILE")
echo "Максимальная оценка: $max"
