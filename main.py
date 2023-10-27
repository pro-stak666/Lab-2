import csv


# flag = 0
# output = open('result.txt', 'w')
# search = input('Search for: ')
# with open('civic.csv', 'r', encoding='windows-1251') as csvfile:
#     table = reader(csvfile, delimiter=';')
#     for row in table:
#         lower_case = row[2].lower()
#         index = lower_case.find(search.lower())
#         if index != -1:
#             print(row[2])
#             flag = 1
#             output.write(f'{row[0]}. {row[2]}. Цена {row[8]} рублей.\n')
#
#     if flag == 0:
#         print('Nothing found.')
#
# output.close()

def task_1():
    """выводит колличество книг с длинной названия более 30"""

    with open('books.csv', 'r', encoding='windows-1251') as f:
        data = csv.reader(f, delimiter=';')
        count_str_len_more_30 = -1
        for row in data:
            if count_str_len_more_30 == -1:
                count_str_len_more_30 = 0
                continue
            count_str_len_more_30 += 1 if len(row[1]) > 30 else 0
        print(count_str_len_more_30)


def task_2(author='Марина Крамер'):
    """реализовывает поиск книг по автору с ограничением от 2018 года"""
    with open('books.csv', 'r', encoding='windows-1251') as f:
        data = [i for i in csv.reader(f, delimiter=';')]
        del data[0]
        data = [i for i in data if int(i[6].split('.')[-1].split()[0]) >= 2018 and i[3] and i[4]]


        def my_find(auth, book):
            if auth.lower() in book[3].lower() or auth.lower() in book[4].lower():
                return True
            elif book[4].lower().split()[0] in auth.lower():
                return True
            return False


        result = []
        for row in data:
            if my_find(author, row):
                result.append(row)

        if result:
            print(f'Вот список книг, что удалось найти по автору: \033[1m{result[0][4]}/{result[0][3]}\u001b[0m')
            for i in enumerate(result, 1):
                print(i[0], i[1][1], i[1][3])
        else:
            print(f'К сожаления по автору \033[1m{author}\u001b[0m ничего не нашлось')


def task_3():
    """создает файл с 20 рандомными книгами"""
    from random import randint

    ran_int = [randint(1, 9410) for _ in range(20)]
    with open('books.csv', 'r', encoding='windows-1251') as f:
        data = [i for i in csv.reader(f, delimiter=';')]
        result = []
        for i in ran_int:
            result.append(f'{data[i][4]}. {data[i][1]} — {data[i][6]}')
        with open('links.txt', 'w', encoding='utf-8') as f:
            f.writelines(f'{str(i[0])} {i[1]}\n' for i in enumerate(result, 1))


def task_4():
    """выводит словарь с заданным условием"""
    from pprint import pprint
    with open('currency.xml', 'r', encoding='windows-1251') as f:
        data = f.readlines()
        s = ''
        for i in data:
            s += i
        dic = {}
        names = []
        char_code = []
        chet = 1
        for i in s.split('Name>'):
            if chet % 2 == 0:
                names.append(i[:-2])
            chet += 1
        chet = 1
        for i in s.split('CharCode>'):
            if chet % 2 == 0:
                char_code.append(i[:-2])
            chet += 1
        for i in range(len(names)):
            dic[names[i]] = char_code[i]

        pprint(dic)


def dop_task_1():
    """Выводит все теги без повторений"""
    with open('books.csv', 'r', encoding='windows-1251') as f:
        res = set([i[2] for i in csv.reader(f, delimiter=';')])
        res.remove('Тип')
        print(*res, sep=', ')


def dop_task_2():
    """Выводит 20 самых популярных книг"""
    # я не знаю, что считать популярным, поэтому возьму самые дорогие
    # не зря же они такие дорогие
    with open('books.csv', 'r', encoding='windows-1251') as f:
        data = [i for i in csv.reader(f, delimiter=';')]
        del data[0]
        data.sort(key=lambda x: float(x[7]))
        for i in enumerate(data[-20:], 1):
            # номер, название, автор, цена
            print(f'{i[0]} "{i[1][1]}", {i[1][4]} — {i[1][7]} руб.')