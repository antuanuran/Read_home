cook_book = {}
list_ingr = []
with open('recipes.txt', 'rt') as file:
    for l in file:
        food_key = l.strip()
        amount = int(file.readline())
        for i in range(amount):
            ingred_str = file.readline()
            name_ingr, count, measure = ingred_str.split(' | ')
            dict_ingred = {'ingredient_name': name_ingr, 'quantity': count, 'measure': measure.strip()}

            list_ingr.append(dict_ingred)

        cook_book[f'{food_key}'] = f'{list_ingr}'
        list_ingr.clear()
        food_key = file.readline()

print(cook_book)

















"""
f = open('test.txt')
res = f.readlines()
print(res)
f.close()

f = open('test.txt')
res = f.read()
print(res)
f.close()

# ************************

f2 = open('folder/123/test3.txt')
res2 = f2.read()
print(type(res2))
print(res2)

# **************************

f2 = open(r'D:\_PYTHON\файлы\fol\test4.txt')
res2 = f2.read()
print(res2)

# ***************************

f2 = open('testik.txt', encoding='utf8')
res2 = f2.read()
print(res2)

# *****************************

f2 = open(r'D:\_PYTHON\файлы\fol\test4.txt')

with open ('test.txt', 'w') as a:
    a.write('10')
    a.write('1112')

with open ('test.txt', 'w') as a:
    a.writelines(['10\n', '12\n', '13'])

with open ('test.txt', 'a') as a:
    a.writelines(['\nпривет'])

"""





