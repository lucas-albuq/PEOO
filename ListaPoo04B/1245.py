while True:
    try:
        x = int(input())
        peD = {}
        peE = {}
        pares = 0
        for _ in range(x):
            num, pe = input().split()
            num = int(num)
            if pe == 'D':
                if peD.get(num):
                    peD[num] +=1
                else:
                    peD[num] = 1    
            elif pe == 'E':
                if peE.get(num):
                    peE[num] +=1
                else:
                    peE[num] = 1   
        for _  in peD:
            if peE.get(_):
                if peD[_] <= peE[_]:
                    pares += peD[_]
                else:
                    pares += peE[_]
        print(pares)                
    except EOFError:
        break    
