#!/bin/bash
current_user="$USER"
if [ -z "$current_user" ]; then
    echo "Ошибка: не удалось определить текущего пользователя."
    exit 1
fi

echo "Поиск пользователя '$current_user' в файле /etc/passwd..."
grep "^${current_user}:" /etc/passwd

if [ $? -ne 0 ]; then
    echo "Пользователь '$current_user' не найден в файле /etc/passwd."
    exit 1
else
    echo "Поиск успешно завершён."
fi
