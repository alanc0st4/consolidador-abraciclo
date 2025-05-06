import csv
import pandas as pd
import shutil
import os

pasta = "C:\\abraciclo\\entrada"  # onde estão os arquivos csv
pasta_destino = "C:\\abraciclo\\saida"  # caminho dos arquivos csv

#Conversão do arquivo para .csv
def converter_csv(pasta):  # conversão do arquivo .txt para .csv

    dir = os.listdir(pasta)  # variável dir que armazena a lista de arquivos do diretório

    for arquivo in dir: #para cada arquivo no diretório 
        caminho_completo = os.path.join(pasta, arquivo)  # caminho completo do arquivo pasta + nome do arquivo

        novo_nome = arquivo + ".csv"  # novo nome do arquivo.csv
        caminho_novo = os.path.join(pasta, novo_nome) #cria um novo caminho com o nome do arquivo

        os.rename(caminho_completo, caminho_novo)  #renomeia o arquivo
        shutil.move(caminho_novo, pasta_destino)  # move o arquivo para a pasta de destino (saida)

#Concatenando os arquivos csv
def concatenar_arquivos(pasta_destino):
    arquivos = os.listdir(pasta_destino) #lista todos os arquivos da pasta destino

    arquivos_concatenados = pd.DataFrame() #dataframe vazio para inserção dos dados 

    for arquivo in arquivos: #para cada arquivo na lista de arquivos 
        caminho_completo = os.path.join(pasta_destino, arquivo) # caminho completo do arquivo

        df = pd.read_csv(caminho_completo, delimiter=";")  # leitura do arquivo csv

        #concatenando arquivos_concatenados + o dataframe vazio
        arquivos_concatenados = pd.concat([arquivos_concatenados, df], ignore_index=True)
    
    #transforma os novo arquivo em csv 
    arquivos_concatenados.to_csv("arquivos_abraciclo_concat.csv", index=False) 


# converter arquivo para csv
converter_csv(pasta)
concatenar_arquivos(pasta_destino)

