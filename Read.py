cook_book = {}
with open('recipes.txt', 'rt') as file:
    for l in file:
        food_key = l.strip()
        amount = int(file.readline())

        list_ingr = []
        for i in range(amount):
            ingred_str = file.readline()
            name_ingr, count, measure = ingred_str.split(' | ')
            dict_ingred = {'ingredient_name': name_ingr, 'quantity': int(count), 'measure': measure.strip()}

            list_ingr.append(dict_ingred)

        cook_book[f'{food_key}'] = list_ingr
        food_key = file.readline()

print(cook_book)


# 2. Функция, которая на вход принимает список блюд из cook_book и количество персон, для кого мы будем готовить

def get_shop_list_by_dishes (dishes, person_count):
    for iter in cook_book:
        if (iter == f'{dishes}'):
            a = (cook_book [f'{iter}'])
            for z in a:
                z['quantity'] *= person_count
                print(z)


get_shop_list_by_dishes('Фахитос', 10)





















