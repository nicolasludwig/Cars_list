import os
import time

class Carros:
    modelo=""
    marca=""
    cor=""
    ano=0
    def __init__(self,modelo,marca,cor,ano):
        self.modelo=modelo
        self.marca=marca
        self.cor=cor
        self.ano=ano
    def printa(self):
        print(self.modelo)

def menu():
    opcao = 1
    while (opcao != 6):
        os.system('cls')
        print("1. Adicionar carros na lista;")
        print("2. Alterar dados de um carro;")
        print("3. Listar todos os carros cadastrados;")
        print("4. Listar os dados de um carro específico;")
        print("5. Excluir um carro da lista;")
        print("6. Sair do programa.")
        opcao = input("Seleciona uma opção do menu: ")
        if (opcao == '1'):
            addCarro()
        elif (opcao == '2'):
            alteraCarro()
        elif (opcao == '3'):
            break
        elif (opcao == '4'):
            break
        elif (opcao == '5'):
            break
        elif (opcao == '6'):
            break
        else:
            print("Digite um valor válido!")
            time.sleep(3)

def addCarro():
    os.system('cls')
    flag=0
    while (flag < 1):
        mod=input("Modelo: ")
        if len(listCarros)>0:
            for i in range(0,len(listCarros)):
                if listCarros[i].modelo==mod:
                    print("Este modelo já está na lista, digite outro!")
                    break
                elif (i+1)==len(listCarros):
                    flag=1
        else:
            flag=1
    mar=input("Marca: ")
    cor=input("Cor: ")
    ano=input("Ano: ")
    car=Carros(mod,mar,cor,ano)
    listCarros.append(car)
    os.system('cls')
    print ("Adicionado na lista:\nModelo:",car.modelo,"\nMarca:",car.marca,"\nCor:",car.cor,"\nAno:",car.ano)
    print ("Tamanho da lista:",len(listCarros))
    input("\n*** ENTER PARA VOLTAR AO MENU ***")

def alteraCarro():
    os.system('cls')
    try:
        num=input("Digite o número do carro que deseja alterar: ")
        if int(num) <= len(listCarros):
            print("O que deseja alterar?")
            print("1. Modelo")
            print("2. Marca")
            print("3. Cor")
            print("4. Ano")
            opcao=input("Digite: ")
            if (opcao == '1'):
                opcao=input("Novo modelo: ")
                listCarros[int(num)-1].modelo=opcao
            elif (opcao == '2'):
                opcao=input("Nova marca: ")
                listCarros[int(num)-1].marca=opcao
            elif (opcao == '3'):
                opcao=input("Nova cor: ")
                listCarros[int(num)-1].cor=opcao
            elif (opcao == '4'):
                opcao=input("Novo ano: ")
                listCarros[int(num)-1].ano=opcao
            print("Dados alterados com sucesso!")
        else:
            print("Número do carro inexistente!")
    except:
        print("Digite apenas números!")
    input("\n*** ENTER PARA VOLTAR AO MENU ***")

listCarros=[]
menu() #Executa o menu em loop

    