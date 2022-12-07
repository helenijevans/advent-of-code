# PART 1
from pathlib import Path
from collections import Counter

# Changing initial approach to use Path objects as checking for lists didn't work
# First time using path objects so documenting 🎉🎉
# https://docs.python.org/3/library/pathlib.html
# I used recursive lists initially but this gave incorrect results when I realised that directory names weren't unique
root = Path('/')
directory_sizes = Counter()

for line in list(open("input.txt")):
    io = line.strip().split()
    if io[0] == '$':
        if io[1] == 'cd':
            if io[2] == '/':
                current_dir = root
            elif io[2] == '..':
                current_dir = current_dir.parent  # .parent looks at everything before the last '/'
            else:
                current_dir = current_dir/io[2] # adds a '/' and then sets the path to the new dir
    elif io[0] != 'dir':
        size = int(io[0])
        directory_sizes[current_dir] += size
        # after we add the size for the current directory - add it on to the parents size
        # .parents method produces a list of all the parent directory paths
        for parent in current_dir.parents:
            directory_sizes[parent] += size
directory_size_list = sorted(list(directory_sizes.values()), reverse=True)
print(sum(directory_size for directory_size in directory_size_list if directory_size <= 100000))

# PART 2
needed_space = 30000000 - (70000000 - directory_size_list[0])
min_max = None
for size in directory_size_list:
    if min_max is None:
        min_max = size
    elif size >= needed_space:
        min_max = min(min_max, size)
    else:
        break
print(min_max)