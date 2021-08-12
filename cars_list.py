import os
import time

opcao = 1
while (opcao != 5):
    os.system('cls')
    print("1. Adicionar carros na lista;")
    print("2. Alterar dados de um carro;")
    print("3. Listar carros cadastrados;")
    print("4. Excluir um carro da lista;")
    print("5. Sair do programa.")
    opcao = input("Seleciona uma opção do menu: ")
    if (opcao == '1'):
        break
    elif (opcao == '2'):
        break
    elif (opcao == '3'):
        break
    elif (opcao == '4'):
        break
    elif (opcao == '5'):
        break
    else:
        print("Digite um valor válido!")
        time.sleep(3)