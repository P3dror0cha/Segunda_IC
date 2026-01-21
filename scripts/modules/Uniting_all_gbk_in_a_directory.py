import glob
import os
import shutil

# Diretório de origem e destino
source_pattern = "/home/pedro/antismash/resultados/MGYG*/MGYG*region*.gbk"
dest_dir = "/home/pedro/antismash/resultados/all_BGCs"

# Garante que o diretório de destino existe
os.makedirs(dest_dir, exist_ok=True)

# Encontra todos os arquivos .gbk
gbk_files = glob.glob(source_pattern)

print(f"{len(gbk_files)} arquivos encontrados.")

for file_path in gbk_files:
    filename = os.path.basename(file_path)
    dest_path = os.path.join(dest_dir, filename)

    # Copia o arquivo (mantém o original)
    shutil.copy2(file_path, dest_path)

print("Cópia finalizada.")
