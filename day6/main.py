# PART 1 & PART 2 Code
from collections import deque

marker = deque()


def packet_processing(marker_length):
    with open("input.txt", 'r', encoding='utf-8') as file:
        marker_at_char = 0
        while True:
            char = file.read(1)
            marker.append(char)
            marker_at_char += 1
            if len(marker) == marker_length:
                if len(set(marker)) == marker_length:
                    return marker_at_char
                marker.popleft()


# PART 1 ANSWER
print(packet_processing(marker_length=4))
# PART 2 ANSWER
print(packet_processing(marker_length=14))

