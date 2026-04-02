#!/bin/bash
echo "Нечётные числа от 1 до 20 (остановка на числе 15):"
for i in {1..20}; do
if [ $i -eq 15 ]; then
        echo "Встречено число 15 — остановка работы скрипта."
        break
fi
if [ $((i % 2)) -eq 0 ]; then
continue
fi
echo "$i"
done
