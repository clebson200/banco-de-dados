from Livros import carregar_livros, salvar_livros


def devolver_livro():

    livros = carregar_livros()

    codigo = input("Código do livro: ")

    for livro in livros:

        if livro["codigo"] == codigo:

            if not livro["emprestado"]:
                print("Este livro já está disponível.")
                return

            livro["emprestado"] = False

            if "usuario" in livro:
                del livro["usuario"]

            salvar_livros(livros)

            print("Livro devolvido com sucesso.")
            return

    print("Livro não encontrado.")