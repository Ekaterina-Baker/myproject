#!/bin/bash
 
# Функция для расчета размера директории или файла
get_size() {
    local path=$1
    local size=$(du -sh "$path" | awk '{print $1}')
    echo $size
}
 
# Цикл по всем файлам и директориям в текущей директории
for file in .* *; do
    if [[ "$file" == ".." ]]; then
<------>continue
    fi
   size=$(get_size "$file")
    echo -e "$size\t$file"
done | sort -hr -k1
