N = int(input())
x = 0
RESULT = int()
resposta = ''
while (x < N):
  alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  palavra = input()
  palavra = palavra.upper()
  num = int(input())
  for i in palavra:
    if i in alfabeto:
      RESULT = RESULT + alfabeto.find(i) - num
      resposta += alfabeto[RESULT]
      RESULT = 0
  print(resposta)
  resposta = ''
  x = x +  1
  
