def usuario():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: ")
    
    return nome, idade, telefone, email

def dados(nome, idade, telefone, email):
    print("\nDados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")

nome, idade, telefone, email = usuario()
dados(nome, idade, telefone, email)
