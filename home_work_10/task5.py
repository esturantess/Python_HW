"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def convert_from_bytes_to_str(args):
    new_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in new_ping.stdout:
        answer = chardet.detect(line)
        result = line.decode(answer['encoding']).encode('utf-8')
        result = result.decode('utf-8')
        print(result)


ping_list = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for el in ping_list:
    convert_from_bytes_to_str(el)
