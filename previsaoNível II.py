# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:41:59 2024

@author: Rafael Wruck
GitHub rafawruck
"""
import os
import matplotlib.pyplot as plt
from datetime import datetime

# Função para abrir ou criar um arquivo com a data atual se ele não existir
def abrir_arquivo_txt(caminho_arquivo):
    # Se o arquivo não existir, crie-o com a data atual
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            arquivo.write(f"Arquivo criado em: {data_atual}\n")
            print(f"Arquivo criado com sucesso: {caminho_arquivo}")
    else:
        print(f"Abrindo arquivo: {caminho_arquivo}")

    # Ler o conteúdo do arquivo
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(f"Conteúdo do arquivo:\n{conteudo}")
    
    return conteudo

# Função para gerar um gráfico a partir dos dados do arquivo
def gerar_grafico_dados(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print("Arquivo não encontrado. Não há dados para gerar o gráfico.")
        return

    # Ler os dados do arquivo e tentar convertê-los em números
    dados = []
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            try:
                # Tentando converter as linhas em números
                dado = float(linha.strip())
                dados.append(dado)
            except ValueError:
                # Ignorando linhas que não podem ser convertidas
                continue
    
    # Verificando se há dados para gerar o gráfico
    if dados:
        plt.plot(dados)
        plt.title("Gráfico dos Dados do Arquivo")
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.show()
    else:
        print("Nenhum dado numérico encontrado no arquivo para gerar o gráfico.")

# Função de menu
def menu():
    caminho_arquivo = '04_10_2024.txt'
    
    while True:
        print("\nMenu:")
        print("1. Abrir ou criar arquivo TXT")
        print("2. Gerar gráfico com os dados do arquivo")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            abrir_arquivo_txt(caminho_arquivo)
        elif opcao == '2':
            gerar_grafico_dados(caminho_arquivo)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do menu
menu()