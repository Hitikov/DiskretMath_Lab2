from checking import check_all
from io_funcs import *
import os.path

def main():
    continue_check = True
    matrix = []
    power = 0
    matrix_chosen = False

    while continue_check:
        print()
        if matrix_chosen:
            print('Матрица отношений выбрана')
        else:
            print('Матрица отношений не выбрана')

        print('Выберете команду:'
              '\n1. Вывод матрицы отношений'
              '\n2. Проверка отношений'
              '\n3. Чтение матрицы отношений из файла'
              '\n4. Сохранение матрицы отношений в файле'
              '\n5. Создание матрицы отношений'
              '\n9. Остановка програмы')

        navig = int(input())

        match navig:
            case 1:
                if matrix_chosen:
                    read_matrix(matrix, power)
                else:
                    print('Матрица не выбрана')

            case 2:
                if matrix_chosen:
                    res = check_all(matrix, power)
                    show_result(res)
                else:
                    print('Матрица не выбрана')

            case 3:
                print('Введите название файла')
                name = input()

                if os.path.exists('matrixes/' + name + '.txt'):
                    res = read_from_file(name)

                    matrix = res[0].copy()
                    power = res[1]

                    matrix_chosen = True
                else:
                    print('Файла с таким именем не существует')

            case 4:
                if matrix_chosen:
                    print('Введите название файла')
                    name = input()

                    if os.path.exists('matrixes/' + name):
                        print('Файл с таким именем существует')
                    else:
                        write_in_file(name, matrix)

                else:
                    print('Матрица не выбрана')

            case 5:
                print('Введите количество элементов:')
                power = int(input())

                if power > 0:
                    matrix_new = []
                    matrix_chosen = True

                    print('Построчно введите значения отношений')
                    for _ in range(power):
                        for _ in range(power):
                            value = int(input())
                            matrix_new.append(value)

                    matrix = create_matrix(matrix_new, power).copy()

                else:
                    print('Не корректное количество элементов:')

            case 9:
                continue_check = False

main()