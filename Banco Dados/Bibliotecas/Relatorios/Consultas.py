from Livros import carregar_livros


def listar_livros():

    livros = carregar_livros()

    print("\nLISTA DE LIVROS")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        status = "Emprestado" if livro["emprestado"] else "Disponível"

        print("-" * 40)
        print("Código:", livro["codigo"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Status:", status)


def pesquisar_livro():

    livros = carregar_livros()

    termo = input("Digite o título: ").lower()

    encontrou = False

    for livro in livros:

        if termo in livro["titulo"].lower():

            print("\nLivro Encontrado")
            print("Código:", livro["codigo"])
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])

            encontrou = True

    if not encontrou:
        print("Nenhum livro encontrado.")