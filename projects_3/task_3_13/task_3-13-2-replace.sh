#!/bin/bash
FILE="sequences.txt"
sed -i 's/ /\t/g' "$FILE"
echo "Замена пробелов на табуляции в файле $FILE выполнена успешно."
echo "Первые 4 строки после замены:"
head -n 4 "$FILE"
