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

def find_max_rank(ln, size):
    max1 = ln[0]
    rank1 = 0
    if size > len(ln):
        print("error! List size too small")
        return -1
    # Find higher digit 
    for l in range(1,len(ln)-size+1):
        if ln[l] > max1:
            max1 = ln[l]
            rank1 = l
    return rank1

def find_joltage_part2(ln):
    previous_rank = 0
    list_max = []
    for s in range(12, 0, -1):
        #print("looking from rank " + str(previous_rank))
        rank = find_max_rank(ln[previous_rank:], s)
        list_max.append(ln[previous_rank+rank])
        previous_rank = previous_rank + rank + 1
    
    return turn_to_number(list_max)

def find_joltage_part1(ln):
    previous_rank = 0
    list_max = []
    for s in range(2, 0, -1):
        #print("looking from rank " + str(previous_rank))
        rank = find_max_rank(ln[previous_rank:], s)
        list_max.append(ln[previous_rank+rank])
        previous_rank = previous_rank + rank + 1
    
    return turn_to_number(list_max)

joltage_part1 = 0
joltage_part2 = 0
with open('data.txt', 'r') as file:
    for line in file:
        numbers = line.strip()
        if numbers != '':
            nn = turn_to_list(int(numbers))
            joltage_part2 += find_joltage_part2(nn)
            joltage_part1 += find_joltage_part1(nn)
    print("Full joltage for part 1 is " + str(joltage_part1))
    print("Full joltage for part 2 is " + str(joltage_part2))
            
