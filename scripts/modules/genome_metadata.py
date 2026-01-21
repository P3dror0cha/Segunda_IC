#!/usr/bin/env python3

import pandas as pd
import json

def genome_metadata():
    """
    Carrega o JSON do arquivo e processa os genomas.
    
    Parâmetros:
    caminho_arquivo (str): Caminho para o arquivo JSON
    lista_ids (list): Lista de IDs para filtrar
    """
        
    with open("/home/pedro/antismash/scripts_python/aquatic_download.json", "r") as f:
        dados_json = json.load(f)

    
    with open("/home/pedro/antismash/scripts_python/aquatic_ids.txt", "r") as f:
        lista_ids = [linha.strip() for linha in f if linha.strip()]
    dados_processados = []
    
    for amostra in dados_json['data']:
        if amostra['id'] in lista_ids:
            linha = {'id': amostra['id']}
            if 'attributes' in amostra:
                linha.update(amostra['attributes'])
            dados_processados.append(linha)
    print(pd.DataFrame(dados_processados))
    df = pd.DataFrame(dados_processados)
    df.to_csv("tabela_ids_MGnify.csv", index=False)
    return pd.DataFrame(dados_processados)

df_metadata = genome_metadata()
