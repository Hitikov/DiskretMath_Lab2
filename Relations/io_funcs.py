def read_matrix(matrix, power):
    for i in range(power):
        for j in range(power):
            print(str(matrix[i][j]) + "\t", end='')
        print()

def create_matrix(content, power):
    matrix = [[] for _ in range(power)]
    pos = 0

    for i in range(power):
        for j in range(power):
            matrix[i].append(int(content[pos]))
            pos += 1

    return matrix

def read_from_file(name):
    matrix = []

    with open('matrixes/' + name + '.txt') as f:
        for line in f:
            arr = list(map(int, line.split()))
            matrix.append(arr)

    power = len(matrix)
    return matrix, power

def write_in_file(name, matrix):
    with open('matrixes/' + name + '.txt', 'w') as f:
        for line in matrix:
            f.write(" ".join(map(str, line)) + '\n')


def show_result(res):

    match res[0]:
        case 2:
            print('Отношение антисимметричное')
        case 1:
            print('Отношение симметричное')
        case -1:
            print('Отношение асимметричное')
        case 0:
            print('Отношение не обладает симметрией')

    match res[1]:
        case 1:
            print('Отношение рефлексивное')
        case -1:
            print('Отношение антирефлексивное')
        case 0:
            print('Отношение не рефлексивное')

    match res[2]:
        case True:
            print('Отношение транзитивное')
        case False:
            print('Отношение не транзитивное')

    match res[3]:
        case True:
            print('Отношение полное')
        case False:
            print('Отношение не полное')