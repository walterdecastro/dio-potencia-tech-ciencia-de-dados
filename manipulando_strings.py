import os
cls = lambda: os.system('cls')
# Alguns métodos da classe String

palavra = "PaLavRA"

# Maiúsculo - upper()
print(palavra.upper())

# Minúsculo - lower()
print(palavra.lower())

# Título - title() - deixa apenas a primeira letra da string em maiúsculo
print(palavra.title())

cls()

palavra = "    palavra    "

print("-" + palavra + "-")

# lstrip() - remove os espaços em branco da esquerda
print("-"+ palavra.lstrip() + "-")

# strip() - remove os espaços em branco de ambos os lados
print("-" + palavra.strip() + "-")

# rstrip() - remove os espaços em branco da direita
print("-" + palavra.rstrip() + "-")

cls()

palavra = " | Bem vindo(a) ao Python! | "

# center(número de caracteres total, "caracter") - centraliza a palavra preenchendo o resto da string com o caracter passado como parâmetro
console_size = os.get_terminal_size().columns
print(palavra.center(console_size, "-"))

# join(string) - separa a string passada como parâmetro por outra string ou caracter
#print("-".join(palavra))
print()

"""dados = [
    input("Digite o seu nome: "),
    int(input("Digite o seu cadastro: ")),
    input("Digite o seu departamento: ")
]

cls()"""

print(console_size)



























