#!/usr/bin/env python3

import requests

def download_genome_url(input, filtro=".fna"):
    """
    Lê um arquivo .txt OU uma lista de links e baixa apenas os arquivos que você quer filtrando pelo tipo de arquivo.
    
    Parâmetros:
    input: caminho do arquivo .txt contendo os links OU uma lista de links.
    filtro: extensão do arquivo a ser baixado. Default: ".fna"
    """
    if isinstance(input, str):
        with open(input, "r") as f:
            links = [linha.strip() for linha in f if linha.strip()]
    elif isinstance(input, list):
        links = [linha.strip() for linha in input if linha.strip()]
    else:
        raise TypeError("O input deve ser um caminho de arquivo (.txt) ou uma lista de links.")

    fna_links = [link for link in links if link.endswith(filtro)] 

    if not fna_links:
        print(f"Nenhum link {filtro} encontrado.") 
        return

    for link in fna_links:
        nome_arquivo = link.split("/")[-1]
        print(nome_arquivo)
        print(f"Baixando {nome_arquivo} ...")

        try:
            resposta = requests.get(link)
            resposta.raise_for_status()
            with open(f"/home/pedro/antismash/genomes/{nome_arquivo}", "wb") as f:
                f.write(resposta.content)
            print(f"Download concluído: {nome_arquivo}")
        except requests.RequestException as e:
            print(f"Erro ao baixar {nome_arquivo}: {e}")


download_genomes = download_genome_url("/home/pedro/antismash/scripts_python/links_download.txt")
