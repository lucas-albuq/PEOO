num = list(map(int, input().split()))
num.sort()
A, B = num
if B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
