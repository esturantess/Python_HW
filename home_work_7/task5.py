# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


# def counting_the_vowels_number(user_list):
#     vowel_letters = ("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")
#     counter = 0
#     for i in range(len(user_list)):
#         for j in range(len(user_list[i])):
#             if (user_list[i])[j] in vowel_letters:
#                 counter += 1
#         user_list[i] = counter
#         counter = 0
#     return user_list
#
#
# def rhythm_test(user_list):
#     if len(user_list) == 1:
#         print("Парам пам-пам")
#
#     for k in range(len(user_list) - 1):
#         if user_list[k] != user_list[k + 1]:
#             print("Пам парам")
#             break
#         elif k + 1 == len(user_list) - 1:
#             print("Парам пам-пам")
#             break
#
#
# user_poem = (input("Винни-Пух, введите своё стихотворение: ")).split(" ")
#
# rhythm_test(counting_the_vowels_number(user_poem))

def counting_the_vowels_number(user_list):
    vowel_letters = ("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")
    return list(filter(lambda el: el in vowel_letters, user_list))


def rhythm_test(user_list):
    new_list = []
    for i in range(len(user_list)):
        new_list.append(len(counting_the_vowels_number(user_list[i])))

    if len(new_list) == 1:
        print("Парам пам-пам")

    for j in range(len(new_list) - 1):
        if new_list[j] == new_list[j + 1]:
            if j + 1 == len(new_list) - 1:
                print("Парам пам-пам")
                break
            else:
                continue
        else:
            print("Пам парам")
            break


user_poem = (input("Винни-Пух, введите своё стихотворение: ")).split(" ")
rhythm_test(user_poem)
