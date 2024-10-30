import json
import os

# Diretórios para os arquivos JSON e SQL
json_dir_path = 'json-files'
sql_dir_path = 'sql-files'

# Certifique-se de que o diretório de saída existe
os.makedirs(sql_dir_path, exist_ok=True)

# Função para escapar aspas simples e duplas nos valores
def escape_quotes(value):
    if isinstance(value, bool):
        return value
    if value is None:
        return 'null'  # Handle NULL values
    return value.replace("'", "''").replace('"', '\"').replace("`", "\`")

# Iterar sobre todos os arquivos JSON no diretório
for json_file_name in os.listdir(json_dir_path):
    if json_file_name.endswith('.json'):
        # Nome da tabela baseado no nome do arquivo
        table_name = os.path.splitext(json_file_name)[0]
        
        # Caminho completo para o arquivo JSON
        json_file_path = os.path.join(json_dir_path, json_file_name)
        
        # Leitura do arquivo JSON e geração dos comandos INSERT
        with open(json_file_path, 'r') as jsonfile:
            data = json.load(jsonfile)
            inserts = []
            for row in data:
                values = ', '.join([
                    f"{escape_quotes(value)}" if isinstance(value, bool) or value is None else f"'{escape_quotes(str(value))}'"
                    for value in row.values()
                ])
                columns = ', '.join([f'"{col}"' for col in row.keys()])
                inserts.append(f"INSERT INTO {table_name} ({columns}) VALUES ({values});")
        
        # Caminho completo para o arquivo SQL de saída
        sql_file_path = os.path.join(sql_dir_path, f"{table_name}.sql")
        
        # Escrevendo os comandos INSERT em um arquivo SQL
        with open(sql_file_path, 'w') as sqlfile:
            sqlfile.write('\n'.join(inserts))
        
        print(f"Script SQL para a tabela '{table_name}' gerado com sucesso!")