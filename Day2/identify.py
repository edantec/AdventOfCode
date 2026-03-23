import copy

def turn_to_list(n):
    list_n = []
    rest = copy.copy(n)
    list_n.append(rest%10)
    while rest // 10 > 0:
        rest = rest // 10
        list_n.append(rest%10)

    return list_n

def is_invalid_part1(n):
    ln = turn_to_list(n)
    if len(ln) % 2 != 0:
        return False 
    
    divide = len(ln) // 2
    if ln[:divide] == ln[divide:]:
        return True
    else:
        return False

def is_invalid_part2(n):
    ln = turn_to_list(n)
    max_div = len(ln)
    for j in range(2, max_div + 1):
        if len(ln) % j == 0:
            divide = len(ln) // j
            test_j = True
            for k in range(1,j):
                 if ln[:divide] != ln[k * divide:(k+1) * divide]:
                     test_j = False
                     break
            if test_j:
                return True
    return False
            

invalid_part1 = 0
invalid_part2 = 0
with open('data.txt', 'r') as file:
    for line in file:
        numbers = line.strip().split(',')
        for num in numbers:
            print("number " + num)
            full_list = num.split('-')
            int1, int2 = int(full_list[0]), int(full_list[1])
            for i in range(int1, int2+1):
                if is_invalid_part2(i):
                    invalid_part2 += i
                if is_invalid_part1(i):
                    invalid_part1 += i
        print("Sum of invalid numbers for part 1 is " + str(invalid_part1))
        print("Sum of invalid numbers for part 2 is " + str(invalid_part2))
        exit()
            
