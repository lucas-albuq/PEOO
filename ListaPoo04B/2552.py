while True:
    try:
        N, M = map(int, input().split())
        a = [list(map(int, input().split())) for _ in range(N)]

        for i in range(N):
            for j in range(M):
                sum = 0
                if a[i][j] == 1:
                    print(9, end="")
                else:
                    if j > 0:
                        sum += a[i][j - 1]
                    if j < M - 1:
                        sum += a[i][j + 1]
                    if i > 0:
                        sum += a[i - 1][j]
                    if i < N - 1:
                        sum += a[i + 1][j]
                    print(sum, end="")
            print()
    except EOFError:
        break
