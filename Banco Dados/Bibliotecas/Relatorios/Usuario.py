import json
import os

ARQUIVO_USUARIOS = "usuarios.json"


def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)


def cadastrar_usuario():
    usuarios = carregar_usuarios()

    print("\nCADASTRO DE USUÁRIO")

    matricula = input("Matrícula: ")
    nome = input("Nome: ")

    usuario = {
        "matricula": matricula,
        "nome": nome
    }

    usuarios.append(usuario)
    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")


def listar_usuarios():
    usuarios = carregar_usuarios()

    print("\nUSUÁRIOS")

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(usuario["matricula"], "-", usuario["nome"])