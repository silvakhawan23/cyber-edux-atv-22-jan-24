import os


def cadastrar(cadastros):
    info = input("Digite seu nome, email e a turma (separados por espaços): ")
    nome, email, turma = info.split()
    if not cadastros:
        rga = 1
    else:
        rga = max(cadastros.keys()) + 1
    cadastros[rga] = (nome, email, turma)


def listar(cadastros):
    for rga in cadastros.keys():
        print(rga, ':', cadastros[rga])


def buscar(cadastros):
    rga = int(input("Digite o RGA para a busca: "))
    if rga in cadastros.keys():
        print(cadastros[rga])
    else:
        print("RGA não cadastrado")


def salvar(cadastros):
    filename = input("Nome do arquivo para salvar: ")
    with open(filename, 'w') as f:
        f.write(str(cadastros))


def carregar(cadastros):
    filename = input("Nome do arquivo para carregar: ")
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            texto = f.read()
            return eval(texto)
    else:
        print('Arquivo inexistente')
        return None


def menu():
    cadastros = {}
    while True:
        print("\nMenu:")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Salvar")
        print("5. Carregar")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar(cadastros)
        elif opcao == "2":
            listar(cadastros)
        elif opcao == "3":
            buscar(cadastros)
        elif opcao == "4":
            salvar(cadastros)
        elif opcao == "5":
            cadastros = carregar(cadastros)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
