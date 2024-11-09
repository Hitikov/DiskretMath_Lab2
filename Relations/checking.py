def get_higher_power(matrix, power):
    matrix_new = [[] for _ in range(power)]

    for i in range(power):
        for j in range(power):
            res = 0
            for k in range(power):
                res += matrix[i][k] * matrix[k][j]

            matrix_new[i].append(res)

    return matrix_new

def check_all (matrix, power):
    matrix_new = get_higher_power(matrix, power)

    symmetry = True
    anti_found = False
    asymmetry = True

    res_symmetry = 0

    reflexivity = True
    antireflexivity = True
    res_reflexivity = 0

    transitivity = True
    fullness = True

    for i in range(power):
        for j in range(power):
            if symmetry or asymmetry:
                if i == j:
                    if matrix[i][i] == 1:
                        anti_found = True

                if matrix[i][j] == 1 and i != j:
                    if matrix[j][i] == 1:
                        asymmetry = False
                    else:
                        symmetry = False

            if reflexivity or antireflexivity:
                if matrix[i][i] == 1:
                    antireflexivity = False
                if matrix[i][i] == 0:
                    reflexivity = False

            if transitivity:
                if matrix[i][j] == 0 and matrix_new[i][j] != 0:
                    transitivity = False

            if fullness:
                if matrix[i][j] == 0 and matrix[j][i] == 0 and i != j:
                    fullness = False

    if symmetry:
        res_symmetry = 1
    if asymmetry:
        res_symmetry = -1
    if asymmetry and anti_found:
        res_symmetry = 2

    if reflexivity:
        res_reflexivity = 1
    if antireflexivity:
        res_reflexivity = -1

    return res_symmetry, res_reflexivity, transitivity, fullness

def check_symmetry (matrix, power):
    symmetry = True
    antisymmetry = True

    for i in range(power):
        for j in range(power):
            if matrix[i][j] == 1:
                if matrix[j][i] == 1:
                    antisymmetry = False
                else:
                    symmetry = False

    if symmetry:
        return 1
    if antisymmetry:
        return -1
    return 0

def check_reflexivity (matrix, power):
    reflexivity = True
    antireflexivity = True

    for i in range(power):
        if matrix[i][i] == 1:
            antireflexivity = False
        if matrix[i][i] == 0:
            reflexivity = False

    if reflexivity:
        return 1
    if antireflexivity:
        return -1
    return 0

def check_transitivity (matrix, power):
    matrix_new = get_higher_power(matrix, power)

    for i in range(power):
        for j in range(power):
            if matrix[i][j] == 0 and matrix_new[i][j] != 0:
                return False

    return True

def check_fullnes (matrix, power):

    for i in range(power):
        for j in range(i+1):
            if matrix[i][j] == 0 and matrix[j][i] == 0:
                return False

    return True