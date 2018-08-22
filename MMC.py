def mdc(a,b):
    while(b !=0):
        b, a = a % b, b

    return a

def mmc(A,B):
    resposta = (A * B )// mdc(A,B)

    return resposta

print(mmc(50,100))