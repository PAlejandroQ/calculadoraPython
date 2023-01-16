import sys
def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    assert b!=0, "DIVISION ENTRE 0!!!"
    return a/b
if __name__ == '__main__':
    assert len(sys.argv)==3, "Deben ser 2 numeros!!!"
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f'{a}+{b} = {sumar(a,b)}')
    print(f'{a}-{b} = {restar(a,b)}')
    print(f'{a}*{b} = {multiplicar(a,b)}')
    print(f'{a}/{b} = {dividir(a,b)}')
