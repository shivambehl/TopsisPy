import os
import sys
import numpy as np
import pandas as pd


def floater(a):  # .astype() can be used but is not reliable
    b = []
    for i in a:
        try:
            ix = []
            for j in i:
                ix.append(float(j))
        except:
            ix = float(i)
            pass
        b.append(ix)
    b = np.array(b)
    return b


def normalize(matrix, r, n, m):
    for j in range(m):
        sq = np.sqrt(sum(matrix[:, j]**2))
        for i in range(n):
            r[i, j] = matrix[i, j]/sq
    return r


def weight_product(matrix, weight):
    r = matrix*weight
    return r


def calc_ideal_best_worst(sign, matrix, n, m):
    ideal_worst = []
    ideal_best = []
    for i in range(m):
        if sign[i] == 1:
            ideal_worst.append(min(matrix[:, i]))
            ideal_best.append(max(matrix[:, i]))
        else:
            ideal_worst.append(max(matrix[:, i]))
            ideal_best.append(min(matrix[:, i]))
    return (ideal_worst, ideal_best)


def euclidean_distance(matrix, ideal_worst, ideal_best, n, m):
    diw = (matrix - ideal_worst)**2
    dib = (matrix - ideal_best)**2
    dw = []
    db = []
    for i in range(n):
        dw.append(sum(diw[i, :])**0.5)
        db.append(sum(dib[i, :])**0.5)
    dw = np.array(dw)
    db = np.array(db)
    return (dw, db)


def performance_score(distance_best, distance_worst, n, m):
    score = []
    score = distance_worst/(distance_best + distance_worst)
    return score


def topsis(a, w, sign):
    a = floater(a)
    # print(a)
    n = len(a)
    # print(n)
    # print(len(a[0]))
    m = len(a[0])
    # print('n:', n, '\nm:', m)
    r = np.empty((n, m), np.float64)
    r = normalize(a, r, n, m)
    t = weight_product(r, w)
    (ideal_worst, ideal_best) = calc_ideal_best_worst(sign, t, n, m)
    (distance_worst, distance_best) = euclidean_distance(
        t, ideal_worst, ideal_best, n, m)
    score = performance_score(distance_best, distance_worst, n, m)
    return (np.argmax(score), score)
    # returns a tupple with index of best data point as first element and score array(numpy) as the other


def cli_output():
    if len(sys.argv) != 4:
        print('Wrong Number of args')
        print('Input should be like - \n '
              'python [package name] [path of csv as string] [list of weights as string] [list of sign as string]')
    else:
        file_path = sys.argv[1]
        try:
            if os.path.exists(file_path):
                print('Path exist')
        except OSError as err:
            print(err.reason)
            exit(1)

        df = pd.read_csv(file_path, header=None)
        a = df.values
        arg2 = sys.argv[2]
        arg3 = sys.argv[3]
        w = arg2.strip('][').split(', ')
        w = list(map(float, w))
        s = arg3.strip('][').split(', ')
        s = list(map(int, s))
        res = topsis(a, w, s)
        print(res)


if __name__ == '__main__':
    cli_output()
