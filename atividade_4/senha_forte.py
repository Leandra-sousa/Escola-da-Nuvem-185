"""Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'."""

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break

    # Verifica o tamanho da senha
    contador = 0
    for caractere in senha:
        contador += 1

    # Verifica se tem pelo menos um número
    numero = False
    for caractere in senha:
        if caractere in '0123456789':
            numero = True
            break

    # Avalia se a senha é forte
    if contador >= 8 and numero:
        print("Senha forte!")
        break
    else:
        print("Senha fraca. Ela deve ter pelo menos 8 caracteres e conter pelo menos um número. Tente novamente.")