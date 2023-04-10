N = int(input())
for x in range(N):
    x, y = map(int, input().split())
    if y != 0:
        print(f'{x/y:.1f}')
    else:
        print('divisao impossivel')
        
