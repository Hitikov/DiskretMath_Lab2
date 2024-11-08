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
    f = open('matrixes/' + name)
    content = f.read()
    f.close()

    content = content.split("\n")

    power = int(content[0])

    matrix = [[] for _ in range(power)]
    pos = 1

    for i in range(power):
        for j in range(power):
            matrix[i].append(int(content[pos]))
            pos += 1

    return matrix, power

def write_in_file(name, matrix, power):
    f = open('matrixes/' + name, 'w')

    f.write(str(power) + '\n')

    for i in range(power):
        for j in range(power):
            f.write(str(matrix[i][j]) + '\n')

    f.close()

def show_result(res):

    match res[0]:
        case 1:
            print('Отношение симметричное')
        case -1:
            print('Отношение антисимметричное')
        case 0:
            print('Отношение асимметричное')

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