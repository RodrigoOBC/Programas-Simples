N = int(input())
x = 0
if(1 <= N <= 10**4):
  while (x < N):
    letra = input()
    if (1 <= len(letra) <=10**3):
      numeros_cii = []
      numeros_finais = []
      resposta = str()
      j = 0
      count = 0
      for i in letra:
        numeros_cii.append(ord(i))

      for i in numeros_cii:
        if ((i!=32) and (26<= i >= 64)):
          numeros_finais.append(i + 3)
        else:
          numeros_finais.append(i)
      for i in numeros_finais[::-1]:
        if ((i!=32) and (count > (len(numeros_finais)/2)-1)):
          resposta = resposta + chr(i-1)
        else:
          resposta = resposta + chr(i)
        count = count + 1
      print(resposta)
      x = x + 1
