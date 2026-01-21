#!/usr/bin/env python3

from Bio import SeqIO
from glob import glob
import pandas as pd

def dataframe_from_gbk(gbk_file):
    """
    Transforma um arquivo gbk em um dataframe.
    
    Parâmetros:
    gbk_file (str): Path para os arquivos em formato gbk.
    """
    records = []
    for file in gbk_file:
        for record in SeqIO.parse(file, "genbank"):
            for feature in record.features:
                feature_data = {
                    'record_id': record.id,
                    'feature_type': feature.type,
                    'location': str(feature.location),
                }
                feature_data.update(feature.qualifiers)
                records.append(feature_data)
    return pd.DataFrame(records)
