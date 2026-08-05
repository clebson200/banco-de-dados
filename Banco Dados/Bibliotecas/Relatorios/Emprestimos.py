from Livros import carregar_livros, salvar_livros


def emprestar_livro():

    livros = carregar_livros()

    codigo = input("Código do livro: ")

    for livro in livros:

        if livro["codigo"] == codigo:

            if livro["emprestado"]:
                print("Livro já emprestado.")
                return

            matricula = input("Matrícula do usuário: ")

            livro["emprestado"] = True
            livro["usuario"] = matricula

            salvar_livros(livros)

            print("Empréstimo realizado.")
            return

    print("Livro não encontrado.")