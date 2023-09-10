#print("\t\t<--- Vamos Treinar! --->\n")

# Operadores Aritméticos
"""primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
op = input("Digite o operador aritmético: ")
if op == "+":
    print(f"Soma: {primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}")
elif op == "-":
    print(f"Subtração: {primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero}")
elif op == "*":
    print(f"Multiplicação: {primeiro_numero} x {segundo_numero} = {primeiro_numero * segundo_numero}")
elif op == "/":
    print(f"Divisão: {primeiro_numero} / {segundo_numero} = {primeiro_numero / segundo_numero}")
else:
    print(f"Erro! Digite um operador válido")

print()"""
# Operadores de Comparação
"""saldo_conta = 23000
valor_saque = float(input("Digite o valor do saque: "))
print(f"Valor do saque: R$ {valor_saque}")
if valor_saque > saldo_conta:
    print("Valor de saque acima do saldo")
else:
    print(f"Valor sacado: R$ {valor_saque}, Saldo: R$ {saldo_conta - valor_saque}")"""

# Operadores de Atribuição
"""saldo = 500
print(saldo)
saldo += 200 # equivalente a saldo = saldo + 200
# saldo -= 100
# saldo *= 100
# saldo /= 100
# saldo %= 100
print(saldo)"""
# Operadores Lógicos
"""saldo = 23000
horas = 22 # 10 horas da noite
print("\t###################################")
print(f"\t##   SALDO: R$ {saldo}")
print("\t###################################")
saque = float(input("\tQual o valor do saque: "))
if saque > 1000 and horas > 18:
    print("Valor não permitido para o horário. Saque um valor mais baixo.")
else:
    print("\t###################################")
    print(f"\t##   SALDO: R$ {saldo - saque}")
    print("\t###################################")"""
# Operadores de Indentidade
"""beatle = "John"
beatle = "Paul"
print("Paul" is beatle)
print("Paul" is not beatle)"""

# Operadores de Associação

"""beatles = ["John", "Paul", "George", "Ringo"]
print("John" in beatles)# Retorna True se a string passada como parâmetro está contido na lista beatles
print("John" not in beatles)"""
