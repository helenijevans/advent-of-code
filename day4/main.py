# PART 1
with open("input.txt", 'r', encoding='utf-8') as file:
    overlaps = 0
    for line in file:
        paired = line.strip().split(',')
        paired1 = paired[0].strip().split('-')
        paired2 = paired[1].strip().split('-')
        all_numbers = sorted(list(map(int, (paired1 + paired2))))
        lower_boundary = all_numbers[0]
        upper_boundary = all_numbers[-1]
        if f'{lower_boundary}-{upper_boundary}' in paired:
            overlaps += 1
print(overlaps)

# PART 2
with open("input.txt", 'r', encoding='utf-8') as file:
    overlaps = 0
    for line in file:
        paired = line.strip().split(',')
        paired1 = list(map(int, (paired[0].strip().split('-'))))
        paired2 = list(map(int, (paired[1].strip().split('-'))))
        if paired1[0] in range(paired2[0], paired2[1]+1) or paired1[1] in range(paired2[0], paired2[1]+1):
            overlaps += 1
        elif paired2[0] in range(paired1[0], paired1[1]+1) or paired2[1] in range(paired1[0], paired1[1]+1):
            overlaps += 1

print(overlaps)




