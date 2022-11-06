def cook_book():
    with open('files/recipes.txt', 'rt', encoding="utf-8") as file:
        c_book = {}
        for line in file:
            dish = line.strip()
            ingredients_count = int(file.readline())
            structure = []
            for _ in range(ingredients_count):
                ing = file.readline().strip().split(' | ')
                ingredients, quantity, measure = ing
                structure.append({'ingredients': ingredients, 'quantity': quantity, 'measure': measure})
            c_book.update({dish:structure})
            file.readline()
    return c_book
        # print(c_book)
def get_shop_list_by_dishes(dish_list, person_count):
    cb = cook_book()
    shop_list = {}
    for dish in dish_list:
        if dish in cb:
            ing_list = cb.get(dish)
            for x in ing_list:
                ing_list = list(x.values())
                name, measure, quantity = ing_list
                shop_list.update({name:{'measure': ing_list[2], 'quantity': int(ing_list[1])*int(person_count)}})
    return print(shop_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)




