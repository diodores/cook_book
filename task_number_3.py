import os

def select_files():
    """Отбирает нужные файлы с директории"""
    total_list = []
    directory_files = os.listdir()
    for file in directory_files:
        if file == '1.txt' or file == '2.txt' or file == '3.txt':
            total_list.append(file)
    return total_list


def sorting_files(total_list):
    """ Сортирует файлы по количеству строк"""
    total_dict = {}
    for file in total_list:
        with open(file) as f:
            a = f.readlines()
            total_dict[file] = len(a)
    sorted_size = sorted(total_dict.items(), key=lambda item: item[1])
    return sorted_size


def merger(sorted_size):
    """Извлекает данные из файлов и объединяет их в списке"""
    dict_new = []
    for i in sorted_size:
        file = i[0]
        with open(file) as f:
            a = f.read()
            dict_new.append(a)
    return dict_new


def writing_to_file(dict_a):
    """Создает файл и записывает в него данные"""
    my_file = open('new_fail.txt', 'w')
    my_file.close()
    for i in dict_a:
        with open('new_fail.txt', 'a') as document:
            document.write(i)


def main():
    """Основной модуль программы"""

    total_list = select_files()
    sorted_size = sorting_files(total_list)
    for i in sorted_size:
        print(f'файл {i[0]}\n строка , всего строк в файле {i[-1]}\n')
    dict_a = merger(sorted_size)
    writing_to_file(dict_a)



main()