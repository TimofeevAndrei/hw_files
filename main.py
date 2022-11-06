# def cook_book():
#     with open('files/recipes.txt', 'rt', encoding="utf-8") as file:
#         c_book = {}
#         for line in file:
#             dish = line.strip()
#             ingredients_count = int(file.readline())
#             structure = []
#             for _ in range(ingredients_count):
#                 ing = file.readline().strip().split(' | ')
#                 ingredients, quantity, measure = ing
#                 structure.append({'ingredients': ingredients, 'quantity': quantity, 'measure': measure})
#             c_book.update({dish:structure})
#             file.readline()
#     return c_book
#         # print(c_book)
# def get_shop_list_by_dishes(dish_list, person_count):
#     cb = cook_book()
#     shop_list = {}
#     for dish in dish_list:
#         if dish in cb:
#             ing_list = cb.get(dish)
#             for x in ing_list:
#                 ing_list = list(x.values())
#                 name, measure, quantity = ing_list
#                 shop_list.update({name:{'measure': ing_list[2], 'quantity': int(ing_list[1])*int(person_count)}})
#     return print(shop_list)
#
#
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

def read_file(file_name):
    file_list = []
    with open(file_name, 'rt', encoding="utf-8") as file:
        count = int()
        for text in file.readlines():
            count += 1
        file.seek(0)
        data = file.read()
        file_list.append(count)
        file_list.append(file_name)
        file_list.append(data)
        # print(file_list)
        return file_list


# read_file('files/1.txt')


def new_file():
    files_dict = {}
    one_file = read_file('files/1.txt')
    two_file = read_file('files/2.txt')
    three_file = read_file('files/3.txt')
    files_dict.update({one_file[0]: {one_file[1]: one_file[2]}})
    files_dict.update({two_file[0]: {two_file[1]: two_file[2]}})
    files_dict.update({three_file[0]: {three_file[1]: three_file[2]}})



    print(files_dict)



new_file()




