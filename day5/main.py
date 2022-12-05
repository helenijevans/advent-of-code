# PART 1
import re

graph_exists = False
for line in reversed(list(open("input_graph.txt"))):
    read = line.rstrip()
    if not graph_exists:
        for group in read.strip().split():
            globals()['group%s' % group] = []
        graph_exists = True
    else:
        crates = read.split()
        for i in range(0, len(crates)):
            if crates[i] != "[]":
                globals()['group%s' % (i+1)].append(crates[i])

"""
For Part 2 to work, the rest of the Part 1 lines need to be commented out (the above is the initial graph setup)
"""
# with open("input.txt", 'r', encoding='utf-8') as file:
#     for line in file:
#         instructions = re.findall('\d+', line)
#         no_of_crates = instructions[0]
#         start_stack = instructions[1]
#         end_stack = instructions[2]
#         for i in range(0, int(no_of_crates)):
#             move_crate = globals()['group%s' % start_stack].pop()
#             globals()['group%s' % end_stack].append(move_crate)
#
# result = []
# for i in range(1,10):
#     result.append((globals()['group%s' % i].pop()))
# print("".join(re.findall('[A-Z]', "".join(result))))

# PART 2
with open("input.txt", 'r', encoding='utf-8') as file:
    for line in file:
        instructions = re.findall('\d+', line)
        no_of_crates = instructions[0]
        start_stack = instructions[1]
        end_stack = instructions[2]
        transfer_stack = []
        for i in range(0, int(no_of_crates)):
            transfer_crate = globals()['group%s' % start_stack].pop()
            transfer_stack.append(transfer_crate)
        for i in range(0, int(no_of_crates)):
            transfer_crate = transfer_stack.pop()
            globals()['group%s' % end_stack].append(transfer_crate)


result = []
for i in range(1,10):
    result.append((globals()['group%s' % i].pop()))
print("".join(re.findall('[A-Z]', "".join(result))))
