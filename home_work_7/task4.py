# Задание 4.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31 22
# 37 43
# 51 86
#
# 3 5 32
# 2 4 6
# -1 64 -8
#
# 3 5 8 3
# 8 3 7 1
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        matrix_rows_number = len(self.matrix_list)
        return f'{[print(*self.matrix_list[i]) for i in range(matrix_rows_number)]}'

    def __add__(self, other):
        new_matrix = []
        matrix_row = []
        counter = 0
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[0])):
                if counter == len(self.matrix_list[0]):
                    new_matrix.append(matrix_row)
                    matrix_row = [(self.matrix_list[i])[j] + (other.matrix_list[i])[j]]
                    counter = 1
                else:
                    matrix_row.append((self.matrix_list[i])[j] + (other.matrix_list[i])[j])
                    counter += 1
        new_matrix.append(matrix_row)
        return new_matrix


Matrix1 = Matrix([[1, 2], [2, 1], [6, 7]])
Matrix2 = Matrix([[4, 3], [2, 7], [1, 9]])
str(Matrix1)
print()
str(Matrix2)
print()
str(Matrix(Matrix1.__add__(Matrix2)))
