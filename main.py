from pprint import pprint

def preparing_dict(file):
    """Получаем удобный словарь для дальнейшей работы"""
    cook_book = {}
    with open(file) as file:
        for line in file:
            dish = line
            dish = dish.rstrip()
            amount_of_ingredients = int(file.readline())
            ingr_list = []
            for ingredient in range(amount_of_ingredients):
                ingredient_name, quantity, measure = file.readline().split('|')
                measure = measure.rstrip()
                ingr_list.append(
                    {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                )
            cook_book[dish]=ingr_list
            file.readline()
    return cook_book

cook_book = preparing_dict('recipes.txt')


def get_shop_list_by_dishes(*dishes, person_count):
    """Принимает блюда и количество персон, расчитывает необходимое количество ингредиентов"""

    new_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            list_of_ingredients = dict(ingridient)
            list_of_ingredients['quantity']= int(list_of_ingredients['quantity'])
            list_of_ingredients['quantity'] *= person_count
            if list_of_ingredients['ingredient_name'] not in new_list:
                new_list[list_of_ingredients['ingredient_name']] = list_of_ingredients
            else:
                new_list[list_of_ingredients['ingredient_name']]['quantity'] += list_of_ingredients['quantity']

    return new_list

dinner = get_shop_list_by_dishes('Омлет','Утка по-пекински',person_count=21)
pprint(dinner)
