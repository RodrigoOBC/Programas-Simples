def fibonacci(final):
    if final <= 2:
        return 1
    else:
        return fibonacci(final - 1) + fibonacci(final - 2)


if __name__ == '__main__':
    print(fibonacci(100))