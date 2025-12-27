# 1) Solcita ao usuãrio que digite seu nome
nome_usuario = input("Insira seu nome")

if nome_usuario.isdigit():
    print("Você digitou seu nome errado")
    exit()

if len(nome_usuario) == 0:
    print("Você não digitou nada")
    exit()

if nome_usuario.isspace():
    print("você só colocou space")
    exit()

