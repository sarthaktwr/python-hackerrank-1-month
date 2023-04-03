from collections import Counter

a = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 5]

for i in a:
    if (a.count(i)) == 1:
        print(i)