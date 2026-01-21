#!/usr/bin/env python3

import requests
import json 

def MGnify_search(max_pages):
    """
    Faz a pesquisa de vários IDs de amostras do MGnify. A pesquisa pode ser feita pelo catálogo de genomas do MGnify ou por bioma.
    
    Parâmetros:
    max_pages: número máximo de páginas a buscar.
    """
    print("Início do download dos ids")
    lista_ids = []
    lista_json = []

    for page in range(1, max_pages + 1):
        url = f"https://www.ebi.ac.uk/metagenomics/api/v1/biomes/root:Environmental:Aquatic:Marine/genomes?page={page}"
        resposta = requests.get(url)

        if resposta.status_code != 200:
            print(f"Erro {resposta.status_code} na página {page}")
            break

        dados_json = resposta.json()
        ids_atuais = [item["id"] for item in dados_json.get("data", [])]
        lista_json.extend(dados_json.get("data", []))
        lista_ids.extend(ids_atuais)

        print(f"Página {page}: {len(ids_atuais)} IDs encontrados")
      

    resultado_final_json = {"data": lista_json}
    
    with open("aquatic_download.json", "w") as i:
        json.dump(resultado_final_json, i, indent=4)

    with open("aquatic_ids.txt", "w") as f:
        for id_study in lista_ids:
            f.write(id_study + "\n")

    print(f"\nTotal de {len(lista_ids)} IDs coletados em {page} páginas.")
    print("fim do download dos ids")
    return resultado_final_json, lista_ids

resultado_final_json, lista_ids = MGnify_search(2)
