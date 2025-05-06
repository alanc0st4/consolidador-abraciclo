import csv #importa biblioteca csv
import os #biblioteca pra interação com o sistema de arquivos
import pandas as pd #manipulação dos dados em tabela


pasta_csv = "C:\\abraciclo\\entrada" #define o caminho do arquivos csv
arquivo_saida = "C:\\abraciclo\\saida" #define o caminho do arquivo concatenado

dados_concatenados = [] #lista para armazenar todas as linhas dos arquivos CSV

primeiro_arquivo = True #primeira linha do arquivo seja copiada

for arquivo in os.listdir(pasta_csv): #loop que percorre todos os arquivos na pasta especificada
    if arquivo.endswith('.csv'): #verifica a extensão do arquivo
        caminho_arquivo = os.path.join(pasta_csv, arquivo) #Cria o caminho completo do arquivo, juntando o diretório da pasta com o nome do arquivo

        with open(caminho_arquivo, mode='r', newline='', encoding='utf-8') as csv_file: #abre o arquivo csv para leitura
            leitor = csv.reader(csv_file) #cria um objeto leitor
            if primeiro_arquivo:
                dados_concatenados.extend(leitor) #add todas as linhas do arquivo à lista
                primeiro_arquivo = False #indicando que os próximos arquivos não terão o cabeçalho incluído.
            else: #Se não for o primeiro arquivo, o código entra neste bloco para pular o cabeçalho.
                next(leitor) #para pular a primeira linha do arquivo (o cabeçalho).
                dados_concatenados.extend(leitor) #Adiciona as linhas restantes (sem o cabeçalho)

with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as csv_file: #Abre o arquivo de saída para escrita (mode='w'), com o encoding UTF-8.
    escritor = csv.writer(csv_file) #cria um objeyo escritor 
    escritor.writerows(dados_concatenados) #Escreve todas as linhas concatenadas no arquivo de saída.

print(f"Arquivos concatenados e salvos em {arquivo_saida}")

#ADICIONANDO O CABEÇALHO

input_file = "C:\\abraciclo\\saida\\arquivo_concatenado.csv" #o caminho para o arquivo concatenado que será lido.
output_file = "C:\\abraciclo\\saida\\output_with_header.csv" #caminho para o arquivo de saída

header =["Data do emplacamento",	"Número do chassi",	"Placa do veículo",	"Tipo documento do faturado	identificação do faturado (antiga denominação: CNPJ do vendedor)",	
         "UF do faturado",	"Tipo do documento do proprietário",	"UF de jurisdição",	"Código do município",	"DT 0901_Descrição", "UF",	"Ano de fabricação", "Ano modelo",	
         "Código da marca/modelo",	"DT 0901_1_Descrição",	"Código tipo de veículo",	"Código da espécie de veículo",	"Código do tipo de carroceria",	"Número da carroceria",	
         "Código da cor predominante",	"Código do combustível", "Potência", "Número de cilindradas do veículo", "Número de lugares", "Capacidade de carga", "Peso bruto total (PBT)",	
         "Capacidade máxima de tração (CMT)",	"Procedência",	"Código de situação do chassi",	"Número da caixa de câmbio", "Número de eixos",	"Número do eixo traseiro/diferencial",	
         "Número do terceiro eixo",	"Número do motor",	"Tipo de montagem",	"Tipo de documento da importadora",	"Número de identificação da importadora",	"Número da DI",	
         "Data de registro da DI",	"Código da unidade local da SRF",	"Data de última atualização",	"Código restrição 1",	"Código restrição 2",	"Código restrição 3",	"Código restrição 4",
         "Data limite da restrição tributária",	"Código da situação do veículo"]

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile: #Abre o arquivo de entrada para leitura e o arquivo de saída para escrita.
    reader = csv.reader(infile) #objeto reader
    writer = csv.writer(outfile) #objeto writer

    writer.writerow(header) #escreve o cabeçalho no arquivo de saída
    writer.writerows(reader) #escreve as linhas do arquivo original sem cabeçalho
print("Header added sucessfully")

#Manipulação com Pandas

input_file_collumns = "C:\\abraciclo\\saida\\output_with_header.csv" #define o caminho para o arquivo com o cabeçalho adicionado
output_file_collumns = "C:\\abraciclo\\saida\\output_with_header_and_collumns.csv" #caminho para o novo arquivo que será gerado

with open(input_file_collumns, "r") as f: #arquivo para leitura
    data = f.read() #too o conteúdo do arquivo armazenado na variável (data)

fields = data.split() #conteúdo dividido em uma lista de campos separados por espaços
df = pd.DataFrame([fields]) #cria um DataFrame a partir da lista fields

df.to_csv(output_file_collumns, index=False, header=False) #Salva o DataFrame df no arquivo CSV de saída, sem o índice e sem o cabeçalho.

print(f"Processed file saved as {output_file_collumns}")