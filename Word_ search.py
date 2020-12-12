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

    for word in text:  # определение слов на русском языке с заданным количеством букв и добавление в список
        if 10 > len(word) > 4:
            for char in word:
                if char in alpha_ru and char not in alpha_en and word not in output_ru:
                    output_ru.append(word)

    return output_ru


def definition_en(text):
    output_en = []

    for word in text:
        for char in word:
            if char in alpha_en and char not in alpha_ru and word not in output_en:
                output_en.append(word)

    return output_en


def main():
    MyFile_01 = open(r'C:\Users\RIENZA\Основы Python\file_input_ru_en.txt', 'r', encoding='UTF8')  # открытие файла
    words = MyFile_01.read()  # чтение текста
    words = normalization(words)  # удаление лишних знаков и создание предварительного списка
    words_ru = definition_ru(words)
    words_en = definition_en(words)
    print(words_en)

    MyFile_02 = open('output.txt', 'w', encoding='UTF8')
    MyFile_02.write('Список слов в тексте на русском языке с количеством букв более 4 и менее 10: \n\n')
    # MyFile_02.write(str(output_ru))  # запись в файл списком

    for word_ru in words_ru:  # запись в файл (построчно, столбиком)
        MyFile_02.write(word_ru)
        MyFile_02.write('\n')

    MyFile_02.write('\n\nСамое длинное слово в тексте на английском языке: \n\n')

    MyFile_02.close()
    MyFile_01.close()


if __name__ == '__main__':
    main()
