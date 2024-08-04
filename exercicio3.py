def cadastrar_produto():
    produto = {}
    produto['codigo'] = input("Digite o código do produto: ")
    produto['nome'] = input("Digite o nome do produto: ")
    produto['quantidade'] = int(input("Digite a quantidade do produto: "))
    produto['preco'] = float(input("Digite o preço do produto: "))
    
    return produto

def exibir_produto(produto):
    print("\nInformações do Produto:")
    print(f"Código: {produto['codigo']}")
    print(f"Nome: {produto['nome']}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Preço: R${produto['preco']:.2f}")
    valor_total = produto['quantidade'] * produto['preco']
    print(f"Valor Total da Compra: R${valor_total:.2f}")

produto = cadastrar_produto()
exibir_produto(produto)
