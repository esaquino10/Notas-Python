# Importando a biblioteca datetime para obter a data e hora atuais
import datetime

# Função para adicionar uma nota
def adicionar_nota(notas, nota):
    data = datetime.datetime.now()  # Obtém a data e hora atuais
    nota = f"{data}: {nota}"  # Formata a nota com a data e hora
    notas.append(nota)  # Adiciona a nota à lista de notas
    print("Nota adicionada com sucesso!")

# Função para exibir todas as notas
def exibir_notas(notas):
    print("Notas:")
    for nota in notas:
        print(nota)

# Função principal
def main():
    notas = []  # Lista vazia para armazenar as notas

    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar nota")
        print("2 - Exibir notas")
        print("3 - Sair")
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            nota = input("Digite a nota: ")
            adicionar_nota(notas, nota)
        elif escolha == "2":
            exibir_notas(notas)
        elif escolha == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
