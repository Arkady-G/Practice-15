alpha_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alpha_en = 'abcdefghiklmnopqrstvxyzABCDEFGHIKLMNOPQRSTVXYZ'


def normalization(text):
    # Удаление знаков перевода строки и знаков препинания, разбиение на слова и создание предварительного списка слов
    text = text.replace('\n\n', ' ')
    text = text.replace('.', ' ')
    text = text.replace(' \n', ' ')
    text = text.replace('\n', ' ')
    text = text.replace(' - ', ' ')
    text = text.replace('"', ' ')
    text = text.replace(',', ' ')
    text = text.replace('!', ' ')
    text = text.replace(':', '')
    text = text.split(' ')
    return text


def definition_ru(text):
    output_ru = []

    for word_ru in text:  # определение слов на русском языке с заданным количеством букв и добавление в список
        for char in word_ru:
            if char in alpha_ru and char not in alpha_en and len(word_ru) > 4 and word_ru not in output_ru:
                output_ru.append(word_ru)

    return output_ru


def definition_en(text):  # определение слов на английском языке и добавление в список
    output_en = []

    for word_en in text:
        for char in word_en:
            if char in alpha_en and char not in alpha_ru and word_en not in output_en:
                output_en.append(word_en)

    return output_en


def sort_ru(datas_ru, data_norm):  # сортировка слов на русском языке по заданным условиям и добавление их в словарь
    data_ru = []

    for word_ru in datas_ru:
        count_ru = data_norm.count(word_ru)
        data_wru = (word_ru, count_ru)
        if data_wru not in data_ru:
            data_ru.append(data_wru)

    data_ru.sort(key=lambda x: x[1])
    data_ru = (data_ru[::-1])
    sort_data_ru = (data_ru[0:3])
    dict_data_ru = dict(sort_data_ru)

    return dict_data_ru


def sort_en(datas_en):  # сортировка слов на русском языке по заданным условиям и добавление их в словарь
    data_en = []
    for word_en in datas_en:
        word_len_en = len(word_en)
        data_wen = (word_en, word_len_en)
        if data_wen not in data_en:
            data_en.append(data_wen)

    sort_data_en = max(data_en, key=lambda x: x[1])
    sort_data_en = list(sort_data_en)
    dict_data_en = dict([sort_data_en])

    return dict_data_en


def main():
    MyFile_01 = open(r'file_input_ru_en.txt', 'r', encoding='UTF8')  # открытие файла
    words = MyFile_01.read()  # чтение текста
    words_norm = normalization(words)  # удаление лишних знаков и создание предварительного списка
    words_ru = definition_ru(words_norm)  # фильтрация слов на русском языке
    words_en = definition_en(words_norm)  # фильтрация слов на английском языке
    list_en = sort_en(words_en)
    list_ru = sort_ru(words_ru, words_norm)  # фильтрация русских слов по условию и создание словаря

    MyFile_02 = open('output.txt', 'w', encoding='UTF8')  # запись полученного словаря в новый файл
    MyFile_02.write(f'В тексте на русском языке три наиболее часто встречающихся слова:\n')
    for key, value in list_ru.items():
        MyFile_02.write(f'Слово "{key}" встречается {value} раз\n')
    MyFile_02.write(f'\nВ тексте на английском языке:\n')
    for key, value in list_en.items():
        MyFile_02.write(f'Самое длинное слово "{key}" имеет {value} букв\n')

    MyFile_02.close()  # закрытие файлов
    MyFile_01.close()


if __name__ == '__main__':
    main()
