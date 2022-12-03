# PART 1
priorities = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
    "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
}

with open("input.txt", 'r', encoding='utf-8') as file:
    sum = 0
    for line in file:
        sizeOfOneDepartment = int(len(line.strip()) / 2)
        first = line[:sizeOfOneDepartment]
        second = line[sizeOfOneDepartment:]
        common_element = "".join(list(set(first) & set(second)))
        if common_element not in priorities.keys():
            sum += 26
        sum += priorities[common_element.lower()]
print(sum)

# PART 2
with open("input.txt", 'r', encoding='utf-8') as file:
    sum = 0
    group = []
    for line in file:
        characters = line.strip()
        if len(group) < 3:
            group.append(set(characters))
            if len(group) == 3:
                common_element = "".join(list(set(group[0]) & set(group[1]) & set(group[2])))
                print(common_element)
                if common_element not in priorities.keys():
                    sum += 26
                sum += priorities[common_element.lower()]
                group.clear()
print(sum)

