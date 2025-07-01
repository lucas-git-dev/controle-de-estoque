import database

def menu():
    while True:
        print("\n=== SISTEMA DE ESTOQUE ===")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Atualizar produto")
        print("4. Deletar produto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            database.insert(nome, quantidade, preco)
            print("Produto adicionado com sucesso!")

        elif opcao == "2":
            produtos = database.read()
            if produtos:
                print("\nID | Nome | Quantidade | Preço")
                print("-" * 40)
                for prods in produtos:
                    print(f"{prods[0]} | {prods[1]} | {prods[2]} | R$ {prods[3]:.2f}")
            else:
                print("Nenhum produto cadastrado.")

        elif opcao == "3":
            id_produto = int(input("ID do produto a atualizar: "))
            nome = input("Novo nome: ")
            quantidade = int(input("Nova quantidade: "))
            preco = float(input("Novo preço: "))
            database.update(id_produto, nome, quantidade, preco)
            print("Produto atualizado com sucesso!")

        elif opcao == "4":
            id_produto = int(input("ID do produto a deletar: "))
            database.delete(id_produto)
            print("Produto deletado com sucesso!")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    database.create_table()
    menu()