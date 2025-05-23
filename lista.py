MENU_DE_OPCOES = """
Olá! Bem-vindo ao programa de gerenciamento de produtos.

Você pode realizar as seguintes operações com a lista de produtos:

A - Adicionar produto
B - Remover produto
C - Pesquisar produtos
D - Sair do Programa
"""

def adicionar_produto(produtos):
    nome = input("Digite o nome do produto a ser adicionado: ")
    unidade_medida = input("Digite a unidade de medida do produto: ")
    quantidade = input("Digite a quantidade do produto: ")
    descricao = input("Digite a descrição do produto: ")
    produto = {
        'nome': nome,
        'unidade_medida': unidade_medida,
        'quantidade': quantidade,
        'descricao': descricao
    }
    produtos.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")

def remover_produto(produtos):
    produto = input("Digite o nome do produto a ser removido: ")
    for p in produtos:
        if p['nome'].lower() == produto.lower():
            produtos.remove(p)
            print(f"Produto '{produto}' removido com sucesso!")
            return
        elif not produtos:
            print("A lista de produtos está vazia.")
            return

def pesquisar_produtos(produtos):
    produto = input("Digite o nome do produto a ser pesquisado: ")
    for p in produtos:
        if p['nome'].lower() == produto.lower():
            print(f"Produto encontrado: {p}")
            return
    print(f"Produto '{produto}' não encontrado na lista.")

def sair_programa():
    print("Saindo do programa...")
    exit()

def main():
    produtos = []   
    
    while True:
        print(MENU_DE_OPCOES)
        print("Lista de produtos:", produtos) 
        opcao = input("Digite a opção desejada: ").strip().upper()

        if opcao == 'A':
            adicionar_produto(produtos)
        elif opcao == 'B':
            remover_produto(produtos)
        elif opcao == 'C':
            pesquisar_produtos(produtos)
        elif opcao == 'D':
            sair_programa()
        else:
            print("Opção inválida. Tente novamente.")
           
        
if __name__ == "__main__":
    main()
    