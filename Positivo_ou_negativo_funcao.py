def positivo_negativo(valor):
    if valor > 0:
        return 'P'
    elif valor < 0:
        return 'N'


if __name__ == '__main__':
    print(positivo_negativo(float(input())))