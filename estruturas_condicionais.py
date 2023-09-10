"""import os
clear = lambda: os.system('cls')
print("\n----------------------------------------------------------------\n")

nome_aluno = input("Digite o seu nome: ").upper()
clear()
print(f"OLÁ {nome_aluno}, SEJA BEM VINDO(A)!\n")
notas = [
    float(input("Digite a nota do 1º bimestre: ")),
    float(input("Digite a nota do 2º bimestre: ")),
    float(input("Digite a nota do 3º bimestre: ")),
    float(input("Digite a nota do 4º bimestre: "))
]

media = 0
for nota in notas:
    media += nota
    
media = media / 4

print()
clear()
if media >= 6:
    print(f"Parabéns {nome_aluno}, a sua nota final foi {media}, você foi aprovada(o)!")
else:
    print(f"Que pena {nome_aluno}, sua nota final foi {media}, você reprovou!")



print("\n----------------------------------------------------------------\n")"""


