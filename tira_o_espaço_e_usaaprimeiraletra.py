N = int(input())
X = int(0)
count = 0
resultado = str()
while(X < N):
  nomes = input()
  nomes = nomes.lower()
  nomes= nomes.split()
  TEXTO = "abcdefghijklmnopqrstuvwxyz"
  for j in range (0,len(nomes)) :
    for i in nomes[j]:
      if i in TEXTO:
        if count == 0:
          resultado = resultado + i
      count = count + 1  
    count = 0
  print(resultado)
  resultado = ''
  X = X + 1
