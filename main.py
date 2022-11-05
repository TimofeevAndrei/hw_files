with open('files/cook_book.txt', 'rt', encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredients_count = int(file.readline())
        structure = []
        for _ in range(ingredients_count):
            ing = file.readline().strip().split(' | ')
            ingredients, quantity, measure = ing
            structure.append({'ingredients': ingredients, 'quantity': quantity, 'measure': measure})
        cook_book.update({dish:structure})
        file.readline()
    print(cook_book)