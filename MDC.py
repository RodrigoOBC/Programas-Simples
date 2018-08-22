def mdc(a,b):
    while(b != 0):
        b, a = a%b, b
    return a

print(mdc(30,60))