# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:13:41 2024

@author: Rafael Wruck
GitHub rafawruck
"""



def ler_arquivo_txt(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        return "Arquivo não encontrado."
    except Exception as e:
        return f"Ocorreu um erro: {e}"

caminho = 'C:/Users/215511/Documents/Trabalho/2024/9 - Nível/dados.txt'
conteudo = ler_arquivo_txt(caminho)
print(conteudo)

