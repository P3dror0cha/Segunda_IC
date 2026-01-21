#!/usr/bin/env python3

import pandas as pd
import regex as re

def cluster_blast_to_df(arquivo):

    dados = []

    with open (arquivo, "r", encoding="utf-8") as f:
        text = f.read()

    parts = re.split(r"Details:ClusterBlast scores for", text)

    reg_cluster_id = re.compile(r"(\S+)\n")
    reg_bgc = re.compile(r">>\s*(\d+)\.\s*(BGC\d+\.\d+)")
    reg_source = re.compile(r"Source:\s*(.+)")
    reg_type = re.compile(r"Type:\s*(.+)")
    reg_score = re.compile(r"Cumulative BLAST score:\s*([\d.]+)")
    reg_blasthits = re.compile(r"Table of Blast hits.*?\n((?:[^\n]+\n)+?)(?=\n|$)")

    for part in parts:
        id_match = reg_cluster_id.search(part)
        if not id_match:
            continue
        cluster_id = id_match.group(1).strip()
        sub_blocos = re.split(r">>\s*\d+\.\s*", part)
        if len(sub_blocos) < 2:
            continue

        for sub in sub_blocos[1:]:
            bgc_match = re.search(r"(BGC\d+\.\d+)", sub)
            if not bgc_match:
                continue
            bgc_id = bgc_match.group(1)

            source_match = reg_source.search(sub)
            source = source_match.group(1).strip() if source_match else None

            type_match = reg_type.search(sub)
            bgc_type = type_match.group(1).strip() if type_match else None

            score_match = reg_score.search(sub)
            cumulative_score = float(score_match.group(1)) if score_match else None

            hits_match = reg_blasthits.search(sub)
            hits = []
            if hits_match:
                linhas = hits_match.group(1).strip().split("\n")
                for l in linhas:
                    partes = l.split()
                    if len(partes) >= 6:
                        hits.append({
                            "query_gene": partes[0],
                            "subject_gene": partes[1],
                            "%identity": partes[2],
                            "blast_score": partes[3],
                            "%coverage": partes[4],
                            "evalue": partes[5]
                        })

            dados.append({
                "Cluster_ID": cluster_id,
                "BGC": bgc_id,
                "Source": source,
                "Type": bgc_type,
                "Cumulative_BLAST_Score": cumulative_score,
                "Blast_Hits": hits
            })

    df = pd.DataFrame(dados)
    print(df.head())

cluster_blast_to_df("/home/pedro/antismash/resultados/todos_knownclusterblast.txt")
