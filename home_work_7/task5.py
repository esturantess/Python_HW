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

class Rhythm:

    def __init__(self, user_list):
        self.user_list = user_list

    def counting_the_vowels_number(self, user_list):
        vowel_letters = ("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")
        return list(filter(lambda el: el in vowel_letters, user_list))

    def rhythm_test(self):
        new_list = []
        for i in range(len(self.user_list)):
            new_list.append(len(self.counting_the_vowels_number(self.user_list[i])))

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


user_poem = (input("Винни-Пух, введите своё стихотворение: ")).lower().split(" ")
Rhythm1 = Rhythm(user_poem)
Rhythm1.rhythm_test()
