import getpass, os

usuario = input("Digite o seu usuário: ").upper()
senha = getpass.getpass("Digite a sua senha: ")

if usuario == "PYUSR" and senha == "123":
    print("Usuário logado!")
    
else:
    print("Acesso negado! Verifique seu usuário e/ou a sua senha!")