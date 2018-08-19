n = int(input())
vetor = list(map(int,input().split()))


def achar_valor(n,vet):
    for i in vet:
        if n < i:
            return f'não é o maior valor, o maior valor é {i}'
        else:
            return f'é o maior valor {n}'

print(achar_valor(n=n,vet=vetor))