cobo = {'Омлет':
            [{'ingredients': 'Яйцо', 'quantity': '2', 'measure': 'шт'},
             {'ingredients': 'Молоко', 'quantity': '100', 'measure': 'мл'},
             {'ingredients': 'Помидор', 'quantity': '2', 'measure': 'шт'}],
        'Утка по-пекински':
            [{'ingredients': 'Утка', 'quantity': '1', 'measure': 'шт'},
             {'ingredients': 'Вода', 'quantity': '2', 'measure': 'л'},
             {'ingredients': 'Мед', 'quantity': '3', 'measure': 'ст.л'},
             {'ingredients': 'Соевый соус', 'quantity': '60', 'measure': 'мл'}],
        'Запеченный картофель':
            [{'ingredients': 'Картофель', 'quantity': '1', 'measure': 'кг'},
             {'ingredients': 'Чеснок', 'quantity': '3', 'measure': 'зубч'},
             {'ingredients': 'Сыр гауда', 'quantity': '100', 'measure': 'г'}],
        'Фахитос':
            [{'ingredients': 'Говядина', 'quantity': '500', 'measure': 'г'},
             {'ingredients': 'Перец сладкий', 'quantity': '1', 'measure': 'шт'},
             {'ingredients': 'Лаваш', 'quantity': '2', 'measure': 'шт'},
             {'ingredients': 'Винный уксус', 'quantity': '1', 'measure': 'ст.л'},
             {'ingredients': 'Помидор', 'quantity': '2', 'measure': 'шт'}]}

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
        # print(c_book)
def get_shop_list_by_dishes(dish_list, person_count):
    cb = cobo
    shop_list = {}
    for dish in dish_list:
        if dish in cb:
            ing_list = cb.get(dish)
            for x in ing_list:
                ing_list = list(x.values())
                name, measure, quantity = ing_list
                shop_list.update({name:{'measure': ing_list[2], 'quantity': int(ing_list[1])*int(person_count)}})
    print(shop_list)









get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)




