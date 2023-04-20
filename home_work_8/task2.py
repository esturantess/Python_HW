# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

text_file = open("secret_file.txt", encoding='utf-8')
content = text_file.readlines()
print("Количество строк в файле: ", len(content))
for i in range(len(content)):
    print(f"В строке {i + 1}", len(content[i].split()), "слов(а).")
text_file.close()

