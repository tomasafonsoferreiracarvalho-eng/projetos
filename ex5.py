num_alunos = int(input('num alunos= '))
while num_alunos<=0:
    num_alunos = int(input('num alunos= '))
notas = []
for n in range(num_alunos):
    nota = int(input(f'nota aluno{n+1}= '))
    while nota<0 and nota>20:
        nota = int(input(f'nota aluno{n+1}= '))
    notas.append(nota)
print('As notas são',notas)
soma = 0
for nota in notas:
    soma=+nota
media = soma / num_alunos
print('A media da turma é ',media)
acima_media = 0
for nota in notas:
    if nota>media:
        acima_media=+1
print('A cima da media estão ',acima_media)
frequencias = {}
for nota in notas:
    if nota in frequencias:
        frequencias[nota]+=1
    else:
        frequencias[nota]=1
moda = None
max_freq = 0
for nota, freq in frequencias.items():
    if freq>max_freq:
        max_freq = freq
        moda = nota
print('A moda das notas é ',moda)