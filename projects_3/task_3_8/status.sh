#!/bin/bash
echo "Пользователь: $(whoami)"
echo "Текущее время: $(date +"%H:%M:%S")"
echo "Путь: $PWD"
echo "Аргументов: $#"
