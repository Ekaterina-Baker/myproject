import os

print("Файлы и директории в текущей директории:")

results = []
for file in os.listdir('.'):
    if os.path.isfile(file):
        try:
            size = os.path.getsize(file)
            if size < 1024:
                size_str = f"{size} Б"
            elif size < 1024 ** 2:
                size_str = f"{size / 1024:.2f} КБ"
            elif size < 1024 ** 3:
                size_str = f"{size / 1024 ** 2:.2f} МБ"
            else:
                size_str = f"{size / 1024 ** 3:.2f} ГБ"
            results.append((size, f"Файл: {file}"))
        except OSError:
            results.append((0, f"Файл: {file} (не доступен)"))
    elif os.path.isdir(file):
        total_size = 0
        for root, dirs, files in os.walk(file):
            for f in files:
                try:
                    total_size += os.path.getsize(os.path.join(root, f))
                except OSError:
                    pass
        size = total_size
        if size < 1024:
            size_str = f"{size} Б"
        elif size < 1024 ** 2:
            size_str = f"{size / 1024:.2f} КБ"
        elif size < 1024 ** 3:
            size_str = f"{size / 1024 ** 2:.2f} МБ"
        else:
            size_str = f"{size / 1024 ** 3:.2f} ГБ"
        results.append((size, f"Директория: {file}"))

results.sort(reverse=True)

for size, description in results:
    if size < 1024:
        size_str = f"{size} Б"
    elif size < 1024 ** 2:
        size_str = f"{size / 1024:.2f} КБ"
    elif size < 1024 ** 3:
        size_str = f"{size / 1024 ** 2:.2f} МБ"
    else:
        size_str = f"{size / 1024 ** 3:.2f} ГБ"
    print(f"{description}, размер: {size_str}")

