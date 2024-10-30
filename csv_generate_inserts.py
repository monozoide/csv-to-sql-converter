import csv
import os

# Diretórios para os arquivos CSV e SQL
csv_dir_path = 'csv-files'
sql_dir_path = 'sql-files'

# Certifique-se de que o diretório de saída existe
os.makedirs(sql_dir_path, exist_ok=True)

# Função para escapar aspas simples e duplas nos valores
def escape_quotes(value):
    return value.replace("'", "''").replace('"', '\"')

# Iterar sobre todos os arquivos CSV no diretório
for csv_file_name in os.listdir(csv_dir_path):
    if csv_file_name.endswith('.csv'):
        # Nome da tabela baseado no nome do arquivo
        table_name = os.path.splitext(csv_file_name)[0]
        
        # Caminho completo para o arquivo CSV
        csv_file_path = os.path.join(csv_dir_path, csv_file_name)
        
        # Leitura do arquivo CSV e geração dos comandos INSERT
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            inserts = []
            for row in reader:
                values = ', '.join([f"'{escape_quotes(value)}'" for value in row.values()])
                inserts.append(f"INSERT INTO {table_name} ({', '.join(row.keys())}) VALUES ({values});")
        
        # Caminho completo para o arquivo SQL de saída
        sql_file_path = os.path.join(sql_dir_path, f"{table_name}.sql")
        
        # Escrevendo os comandos INSERT em um arquivo SQL
        with open(sql_file_path, 'w') as sqlfile:
            sqlfile.write('\n'.join(inserts))
        
        print(f"Script SQL para a tabela '{table_name}' gerado com sucesso!")