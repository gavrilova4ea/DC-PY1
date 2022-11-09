def get_count_char(str_):
    dict_1 = {}
    for a in str_.lower():
        if a.isalpha():
            if a in dict_1:
                dict_1[a] += 1
            else:
                dict_1[a] = 1
    dolya(dict_1, str_)
    return dict_1


def dolya(dict_1, str_):
    dict_2 = {}
    for b, c in dict_1.items():
        dict_2[c] = round(c / len(str_) * 100, 2)

    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
