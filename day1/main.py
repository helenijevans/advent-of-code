# PART 1
with open("input.txt", 'r', encoding='utf-8') as file:
    maximum = 0
    count = 0
    for line in file:
        if line == "\n":
            maximum = max(count, maximum)
            count = 0
        else:
            count += int(line)
print(maximum)

# PART 2
with open("input.txt", 'r', encoding='utf-8') as file:
    top3 = [0,0,0]
    count = 0
    for line in file:
        if line == "\n":
            if count > top3[0]:
                top3[0], top3[1], top3[2] = count, top3[0], top3[1]
            elif count > top3[1]:
                top3[1], top3[2] = count, top3[1]
            elif count > top3[2]:
                top3[2] = count
            count = 0
        else:
            count += int(line)
print(sum(top3))