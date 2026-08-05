import json
import os

ARQUIVO_LIVROS = "livros.json"


def carregar_livros():
    if os.path.exists(ARQUIVO_LIVROS):
        with open(ARQUIVO_LIVROS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_livros(livros):
    with open(ARQUIVO_LIVROS, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)


def cadastrar_livro():
    livros = carregar_livros()

    print("\nCADASTRO DE LIVRO")

    codigo = input("Código: ")
    titulo = input("Título: ")
    autor = input("Autor: ")

    livro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "emprestado": False
    }

    livros.append(livro)
    salvar_livros(livros)

    print("Livro cadastrado com sucesso!")