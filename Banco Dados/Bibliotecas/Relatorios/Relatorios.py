from Livros import carregar_livros


def relatorio():

    livros = carregar_livros()

    total = len(livros)
    emprestados = 0

    for livro in livros:
        if livro["emprestado"]:
            emprestados += 1

    disponiveis = total - emprestados

    print("\n" + "=" * 40)
    print("RELATÓRIO DA BIBLIOTECA")
    print("=" * 40)
    print("Total de livros:", total)
    print("Livros disponíveis:", disponiveis)
    print("Livros emprestados:", emprestados)
    print("=" * 40)