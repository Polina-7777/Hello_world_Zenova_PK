#!/bin/bash
OLD_PATH="/var/lib/mysql/data"
NEW_PATH="/mnt/ssd/mysql"
FILE="settings.php"
sed -i "s|$OLD_PATH|$NEW_PATH|g" "$FILE"

echo "Замена пути в файле $FILE выполнена:"
echo "Старый путь: $OLD_PATH"
echo "Новый путь: $NEW_PATH"
