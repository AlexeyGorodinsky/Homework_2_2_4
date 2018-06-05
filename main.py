import chardet

from chardet.universaldetector import UniversalDetector


def top_words():

    detector = UniversalDetector()

    print('\n')
    filename = input('Введите названиен файла в формате "name.txt": ')
    n = int(input('Укажите, какое число наиболее часто встречающихся слов Вы хотите найти: '))
    word_l = int(input('Укажите минимальную длину слов, участвующих в "рейтинге" наиболее часто встречающихся: '))
    print('\n')

    with open(filename, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        code_type = detector.result['encoding']
        print('Файл {} выполнен в кодировке {}' .format(filename, code_type), '\n')

    with open(filename, encoding=code_type) as f:

        content = f.read()
        s = content.lower()
        s = s.replace('.', '')
        s = s.replace(',', '')
        s = s.replace('!', '')
        s = s.replace(':', '')
        s = s.replace(';', '')
        s = s.replace('?', '')
        all_words = s.split(' ')
        dic = {}

        for x in all_words:
            if (len(x) >= word_l):
                k = s.count(x)
                dic[x] = k
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        print('{} слов длиннее {} букв, наиболее часто встречающихся в {}: \n' .format(n, word_l, filename))
        q = 1
        for z in dic:
            if (q > n):
                break
            q = q + 1
            print(str(z))


c = top_words()
print(c)
