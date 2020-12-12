alpha_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-'
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
    text = text.replace(':', '')
    text = text.split(' ')
    return text


def definition_ru(text):
    output_ru = []
    for word in text:  # определение слов с заданным количеством букв и добавление этих слов в новый список
        if 10 > len(word) > 5:
            for char in word:
                if char in alpha_ru and word not in output_ru:
                    output_ru.append(word)

    return output_ru


def main():
    MyFile = open(r'C:\Users\RIENZA\Основы Python\file_input_ru_en.txt', 'r', encoding='UTF8')  # открытие файла
    words = MyFile.read()  # чтение текста
    words = normalization(words)  # удаление лишних знаков и создание предварительного списка
    words = definition_ru(words)

    # print(words)

    MyFile_02 = open('output.txt', 'w', encoding='UTF8')
    # # MyFile_02.write(str(output))  # запись в файл списком

    for element in words:  # запись в файл (построчно, столбиком)
        MyFile_02.write(element)
        MyFile_02.write('\n')
    MyFile_02.close()

    MyFile.close()


if __name__ == '__main__':
    main()