#!/bin/bash
echo "=== Анализ использования дискового пространства ==="
echo "Файловая система | Процент заполнения"
echo "----------------|-----------------"
df -h | awk '
NR > 1 {  
    filesystem = $1
    usage_percent = $5

    sub(/%/, "", usage_percent)

    printf "%-15s | %s\n", filesystem, $5

    if (usage_percent > 90) {
        printf "ПРЕДУПРЕЖДЕНИЕ: Файловая система %s заполнена на %s! Требуется внимание!\n", filesystem, $5
    }
}
'
