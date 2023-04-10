n = int(input())
a = 0
b = 1
for x in range(n):
    if x == n - 1:
        print(a)
    else:
        print(a, end = ' ')
    c = a + b
    a = b
    b = c
