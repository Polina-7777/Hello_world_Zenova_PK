#!/bin/bash
echo "Создание 10 текстовых файлов..."
for i in {1..10}; do
    touch "test${i}.txt"
    echo "Создан файл: test${i}.txt"
done
echo "---"

echo "Удаление файлов в обратном порядке (от test10.txt до test1.txt)..."
counter=10
while [ $counter -ge 1 ]; do
    filename="test${counter}.txt"
echo "Удален файл: $filename"
counter=$((counter - 1))
done
echo "Все файлы удалены"
