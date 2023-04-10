A1 = int(input())
A2 = int(input())
A3 = int(input())

minutosGastosA1 = A2 * 2 + A3 * 4
minutosGastosA2 = A1 * 2 + A3 * 2
minutosGastosA3 = A1 * 4 + A2 * 2
    
minutosLista = [minutosGastosA1, minutosGastosA2, minutosGastosA3]
minutosLista.sort()
print(minutosLista[0])    
