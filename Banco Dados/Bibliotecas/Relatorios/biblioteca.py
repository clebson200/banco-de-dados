import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "Relatorio"))

from Livros import cadastrar_livro
from Usuario import cadastrar_usuario, listar_usuarios
from Consultas import listar_livros, pesquisar_livro
from Emprestimos import emprestar_livro
from Devolucao import devolver_livro
from Relatorios import relatorio


while True:

    print("\n")
    print("=" * 50)
    print(" SISTEMA DE BIBLIOTECA ")
    print("=" * 50)

    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Cadastrar Usuário")
    print("4 - Listar Usuários")
    print("5 - Emprestar Livro")
    print("6 - Devolver Livro")
    print("7 - Pesquisar Livro")
    print("8 - Relatório")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        cadastrar_usuario()

    elif opcao == "4":
        listar_usuarios()

    elif opcao == "5":
        emprestar_livro()

    elif opcao == "6":
        devolver_livro()

    elif opcao == "7":
        pesquisar_livro()

    elif opcao == "8":
        relatorio()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")