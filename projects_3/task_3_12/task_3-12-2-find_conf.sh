#!/bin/bash
echo "Поиск файлов с расширением .conf в директории /etc (игнорирование регистра)..."
echo "---"
ls -l /etc | grep -i "\.conf$"
if [ $? -eq 0 ] && [ -n "$(ls -l /etc 2>/dev/null | grep -i '\.conf$')" ]; then
    echo "---"
    echo "Поиск успешно завершён. Файлы найдены."
else
    echo "---"
    echo "Файлы с расширением .conf не найдены в директории /etc."
fi
