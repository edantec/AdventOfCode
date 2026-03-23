dial = 50 # Initial state of the dial
nbr_zero_part1 = 0  # Count for number of time the dial points at 0
nbr_zero_part2 = 0  # Count for number of time the dial passes 0
print("dial is " + str(dial))
with open('data.txt', 'r') as file:
    for line in file:
        cmd = line.strip()
        if cmd != '':
            direction = cmd[0]
            clicks = int(cmd[1:])
            turnclock = clicks // 100
            rest = clicks % 100
            nbr_zero_part2 += turnclock
            if direction == 'L':
                dial -= rest
                if dial <= 0:
                    if dial + rest != 0:
                        nbr_zero_part2 += 1
                    if dial < 0:
                        dial = 100 + dial 
                    if dial == 0:
                        nbr_zero_part1 += 1
            elif direction == 'R':
                dial += rest
                if dial >= 100:
                    dial = dial - 100
                    nbr_zero_part2 += 1
                if dial == 0:
                        nbr_zero_part1 += 1
    print("nbr zero part 1 = " + str(nbr_zero_part1))
    print("nbr zero part 2 = " + str(nbr_zero_part2))
            
