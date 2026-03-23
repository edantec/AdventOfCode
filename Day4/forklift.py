import numpy as np
import copy

def turn_to_list(n):
    list_n = []
    rest = copy.copy(n)
    list_n.append(rest%10)
    while rest // 10 > 0:
        rest = rest // 10
        list_n.insert(0, rest%10)

    return list_n

def turn_to_number(ln):
    number = 0
    size = len(ln)
    for l in range(size):
        number += ln[l] * np.power(10, size - l - 1)
    
    return number

def create_matrix(ln):
    lines = len(ln)
    matrix = []
    for l in range(lines):
        string = ln[l]
        cols = len(string)
        lcol = []
        for c in range(cols):
            if string[c] == '@':
                lcol.append(1)
            else:
                lcol.append(0)
        matrix.append(lcol)
    return matrix

def is_accessible(xx, l, c):
    ngb = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            else:
                if xx[l+i][c+j] == 1 or xx[l+i][c+j] == 2:
                    ngb += 1
    if ngb < 4:
        xx[l][c] = 2
        return True
    else:
        return False

def count_accessible(ln):
    start = 1
    end = 136
    count = 0
    for l in range(start, end):
        for c in range(start, end):
            if ln[l][c] == 1:
                if is_accessible(ln, l, c):
                    count += 1
    return count

def remove_accessible(ln):
    start = 1
    end = 136
    for l in range(start, end):
        for c in range(start, end):
            if ln[l][c] == 2:
                ln[l][c] = 0

smat = []
total = 0
with open('data.txt', 'r') as file:
    smat.append('.'*137)
    for line in file:
        numbers = line.strip()
        if numbers != '':
            #print("line is " + str(numbers))
            nn = '.'+numbers+'.'
            smat.append(nn)
    smat.append('.'*137)
    ln = create_matrix(smat)
    while True:
        cc = count_accessible(ln)
        if cc == 0:
            break
        else:
            print("There are " + str(cc) + " removable")
            total += cc
            remove_accessible(ln)
    print("Answer for part 2 is " + str(total))
            
