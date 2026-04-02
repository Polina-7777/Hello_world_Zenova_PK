#!/bin/bash
FILE="data.csv"
echo "=== Названия товаров ==="
awk -F',' '{print $2}' "$FILE"
echo ""
echo "=== Товары дороже 20 ==="
awk -F',' '$3 > 20 {print $2 ": $" $3}' "$FILE"
echo ""
echo "=== Общая стоимость ==="
total=$(awk -F',' '{sum += $3} END {print sum}' "$FILE")
echo "Общая стоимость всех товаров: \$${total}"
