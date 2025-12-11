#while
tentativas = 0
while tentativas<3:
    print('tente novamente')
    tentativas = tentativas +1
senha = ''
while senha !='123456':
    senha = (input('Digite a senha correta: '))
print('Bem-vindo ao sistema')
nome = ''
while nome == '':
    nome = input('nome: ')
print(f'Olá {nome}')
print('='*20)
horario=0
while horario <=17:
    print(horario)
    horario +=1
print('hora de ver o por do sol')
print('='*20)
usuario = ''
senha = ''
tentativas = 0
while (usuario!='Tomás' or senha!='senha123') and tentativas<3:
    usuario = input('user: ')
    senha = input('senha: ')
    tentativas +=1
if usuario == 'Tomás' and senha == 'senha123':
    print('entrada com sucesso')
else:
    print('aguardar')


        