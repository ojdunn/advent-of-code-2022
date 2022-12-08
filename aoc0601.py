#! python3
from collections import deque

f = open("input/input06.txt")
signal = f.read()  # get signal alpha text as one long string
# PART 1
# unique_chars = 4
# PART 2
unique_chars = 14
# queue of max length <unique_chars>
q = deque(signal[:unique_chars], unique_chars)
i = unique_chars
while len(set(q)) != unique_chars:
    q.append(signal[i])
    i += 1

print(i)
