import pandas as pd


#Separando os dados 

#"nome do campo": (início, fim) delimitando o número de caracteres/bytes de cada coluna 
header_renavam = { 
    "Data do Emplacamento": (0, 8),
    "Número do Chassi": (8, 29),
    "Placa do Veículo": (29, 36),
    "Tipo Documento do Faturado": (36, 37),
    "Identificação do Faturado (antiga denominação: CNPJ do Vendedor)": (37, 51),
    "UF do Faturado": (51, 53),
    "Tipo do Documento do Proprietário": (53, 54),
    "UF de Jurisdição": (54, 56),
    "Código do Município": (56, 60),
    "Ano de Fabricação": (60, 64),
    "Ano Modelo": (64, 68),
    "Código da Marca/Modelo": (68, 74),
    "Código do Tipo de Veículo": (74, 76),
    "Código da Espécie de Veículo": (76, 78),
    "Código do Tipo de Carroceria": (78, 81),
    "Número da Carroceria": (81, 102),
    "Código da Cor Predominante": (102, 104),
    "Código do Combustível": (104, 106),
    "Potência": (106, 109),
    "Número de Cilindradas do Veículo": (109, 113),
    "Número de lugares": (113, 116),
    "Capacidade de Carga": (116, 121),
    "Peso Bruto Total (PBT)": (121, 126),
    "Capacidade Máxima de Tração (CMT)": (126, 131),
    "Procedência": (131, 132),
    "Código de Situação do Chassi": (132, 133),
    "Número da Caixa de Câmbio": (133, 154),
    "Número de Eixos": (154, 156),
    "Número do Eixo Traseiro/Diferencial": (156, 177),
    "Número do Terceiro Eixo": (177, 198),
    "Número do Motor": (198, 219),
    "Tipo de Montagem": (219, 220),
    "Tipo de Documento da Importadora": (220, 221),
    "Número de Identificação da Importadora": (221, 235),
    "Data de Registro da DI": (245, 253),
    "Código da Unidade Local da SRF": (253, 260),
    "Data de Última Atualização": (260, 268),
    "Código Restrição 1": (268, 270),
    "Código Restrição 2": (270, 272),
    "Código Restrição 3": (272, 274),
    "Código Restrição 4": (274, 276),
    "Data Limite da Restrição Tributária": (276, 284),
    "Código de Situação do Veículo": (284, 285),
}

with open("arquivos_abraciclo_concat.csv", mode= "r", encoding="utf-8") as arquivo:
    #inclui a linha na lista e pula as linhas vazias
    linhas = [linha.strip() for linha in arquivo if linha.strip()]  

# Extrai os campos com base no layout
dados = []  # lista vazia
for linha in linhas:
    registro = {}

    for campo, (inicio, fim) in header_renavam.items():
        valor = linha[inicio:fim].strip()  # separa os registros de acordo com os bytes/caracteres
        registro[campo] = valor
    dados.append(registro)

# Cria o DataFrame
df = pd.DataFrame(dados)

# Exporta para CSV sem notação científica
df.to_csv("consolidados_abraciclo.csv", index=False, encoding="utf-8")

