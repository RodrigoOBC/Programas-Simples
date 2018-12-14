def fibonacci(final) -> list:
    a = 1
    b = 1
    lista = [a,b]
    for cont in range(2,final):
        a,b = b,a+b
        lista.append(b)
    return lista

if __name__ == '__main__':
    print(fibonacci(10))