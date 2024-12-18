def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = []
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Неправильний формат рядка: {line.strip()}")
            return cats
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

cats_info = get_cats_info("cats.txt")
print(cats_info)
