def calcular_media_ponderada(A,B,pes1,pes2):
    media_ponderada = ((A*pes1)+(B*pes2))/(pes1+pes2)
    return media_ponderada

Nota1, Nota2 = float(input()), float(input())
peso1,peso2 = float(input()),float(input())
print(f'MEDIA = %.5f' % calcular_media_ponderada(Nota1, Nota2, peso1, peso2))