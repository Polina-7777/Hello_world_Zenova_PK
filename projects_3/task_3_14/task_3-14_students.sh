#!/bin/bash
FILE="students.txt"
echo "=== Имена студентов ==="
awk '{print $1}' "$FILE"
echo ""
echo "=== Оценки студентов ==="
awk '{print $2}' "$FILE"
echo ""
echo "=== Номер строки и имя ==="
nl -v1 -ba "$FILE" | while read line; do
    line_num=$(echo "$line" | awk '{print $1}')
    student_name=$(echo "$line" | awk '{print $2}')
    echo "$line_num: $student_name"
done
