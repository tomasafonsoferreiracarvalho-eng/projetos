import math
def seno_hiper(x , n_termos):
    soma_mais = 0.0
    soma_menos = 0.0

    for n in range(n_termos):
        termo_mais = (x ** n) / math.factorial(n)
        termo_menos = ((-x) ** n) / math.factorial(n)

        soma_mais += termo_mais
        soma_menos += termo_menos
    resultado = 0.5 * (soma_mais - soma_menos)
    return resultado
def main():
    x = float(input('x= '))
    n_termos = int(input('n termos= '))
    resultado = seno_hiper(x, n_termos)
    print(resultado)
s = ''
while s!='sair':
    main()
    s = str(input('sair/continuar: '))