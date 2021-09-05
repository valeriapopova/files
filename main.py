from pprint import pprint


def prepare_dict(cook_book: str) -> dict:
    result : dict = dict()

    with open(cook_book) as file:
        for line in file:
            dishes = line.strip()
            records_quantity = int(file.readline())
            ingredients = []
            for food in range(records_quantity):
                ingredient_name, quantity, measure = file.readline().strip().split('|')
                ingredients.append(
                    {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure}
                )
            result[dishes] = ingredients
            file.readline()
    return result


result_dict = prepare_dict('data.txt')
pprint(result_dict)
print()

def get_shop_list_by_dishes(dishes, person_count=int):
    shop_list = {}
    d = result_dict
    for dish in dishes:
        for item in (d[dish]):
            dishes_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity':
                int(item['quantity']) * int(person_count)})])
            if shop_list.get(item['ingredient_name']):
                ingredients = (int(shop_list[item['ingredient_name']]['quantity']) +
                               int(dishes_list[item['ingredient_name']]['quantity']))
                shop_list[item['ingredient_name']]['quantity'] = ingredients
            else:
                shop_list.update(dishes_list)
    return shop_list


g = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
pprint(g)
print()





def new_file():
    files_list = ['1.txt', '2.txt', '3.txt']
    files_info = []
    for files_name in files_list:
        with open(files_name) as file:
            count = len(open(files_name).readlines())
            files_info.append([files_name, count, file.read().splitlines()])
    files_info.sort(key=lambda item: len(item[2]))

    return files_info


forth_file = new_file()
pprint(forth_file)







