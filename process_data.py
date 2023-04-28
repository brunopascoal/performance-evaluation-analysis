import pandas as pd
def process_data(df):
    
    columns_to_keep = [
        "semanaTermino", "id6", "id7", "id8", "id9", "id10", "id11", "id12", "id13", "id14", 
        "id15", "id16", "id17", "id18", "id19", "id20", "id21", "id22", "justificativa", 
        "comentarios", "nome", "avaliado", "cliente"
    ]

    df = df[columns_to_keep]

    df_assistants = df[df['id22'] == 'null']
    df_seniors = df[df['id22'] != 'null']


    lista_comum = [
    "Apresentar conhecimento técnico de Auditoria compatível com a descrição do cargo",
    "Apresentar conhecimento técnico de Contabilidade compatível com a descrição do cargo",
    "Capacidade de entendimento e interpretação das explicações (clientes/superiores)",
    "Cumprir o trabalho no tempo estabelecido",
    "Disponibilizar o trabalho com qualidade (metodologia, técnica, organização e apresentação)",
    "Buscar melhoria com base nas revisões e feedback anteriores",
    "Apresentar capacidade de comunicação oral e escrita",
    "Possuir habilidade crítica e analítica dos fatos, se resguardando sobre eventuais problemas identificados nos exames",
    "Eliminar todos os pontos de revisão identificados pelos superiores",
    "Dominar as ferramentas tecnológicas utilizadas para o desenvolvimento do trabalho",
    "Apresentar atitude de participação, iniciativa e disposição",
    "Apresentar bom relacionamento com os funcionários do cliente",
    "Apresentar bom relacionamento com os membros da equipe",
    "Apontar as horas utilizadas no projeto",
    ]

    lista_assistentes = lista_comum + ["Entregar os pontos quando identificado em tempo hábil ao responsável para inclusão no relatório"]
    lista_seniors = lista_comum + ["Avaliar os assistentes no fechamento do trabalho", "Revisar os papéis de trabalhos", "Elaborar o relatório em tempo hábil e com qualidade"]

    mapping_assistentes = {f'id{i}': lista_assistentes[i-6] for i in range(6, 6 + len(lista_assistentes))}
    mapping_seniors = {f'id{i}': lista_seniors[i-6] for i in range(6, 6 + len(lista_seniors))}
    

    # Renomeie as colunas de df_assistants e df_seniors
    df_assistants = df_assistants.rename(columns=mapping_assistentes)
    df_seniors = df_seniors.rename(columns=mapping_seniors)
    return df_assistants, df_seniors

def calc_avaliado_mean(df):
    avaliados = df['avaliado'].unique()
    medias_list = []

    for avaliado in avaliados:
        df_avaliado = df[df['avaliado'] == avaliado]
        
        # Selecione apenas as colunas relacionadas às notas
        colunas_notas = [col for col in df_avaliado.columns if col not in ['semanaTermino', 'justificativa', 'comentarios', 'nome', 'avaliado', 'cliente']]
        
        # Converta os valores para numéricos
        df_avaliado[colunas_notas] = df_avaliado[colunas_notas].apply(pd.to_numeric, errors='coerce')
        
        media = df_avaliado[colunas_notas].mean(numeric_only=True)
        
        for pergunta, valor in media.items():
            medias_list.append([avaliado, pergunta, valor])

    medias = pd.DataFrame(medias_list, columns=['avaliado', 'Pergunta', 'Nota Real'])
    return medias

        
def gerar_dataframe_avaliado(df_avaliado, pesos, notas):
    # Calcula o número de vezes que as listas pesos e notas devem ser repetidas
    repeat_count, remainder = divmod(len(df_avaliado), len(pesos))

    # Repete as listas pesos e notas e adiciona elementos extras se necessário
    extended_pesos = pesos * repeat_count + pesos[:remainder]
    extended_notas = notas * repeat_count + notas[:remainder]

    # Cria a coluna "Pesos" e atribui os pesos
    df_avaliado['Pesos'] = extended_pesos
    df_avaliado['Nota desejada'] = extended_notas

    df_avaliado['Ponto desejado'] = df_avaliado['Pesos'] * df_avaliado['Nota desejada'] 
    df_avaliado['Porcentagem Desejada'] =  df_avaliado['Ponto desejado']/df_avaliado['Ponto desejado'].sum() *100

    # Cria a coluna "Nota" e calcula multiplicando a "Nota Real" pelos "Pesos"
    df_avaliado['Ponto Real'] = df_avaliado['Nota Real'] * df_avaliado['Pesos']
    df_avaliado['Porcentagem Real'] = df_avaliado['Ponto Real']/df_avaliado['Ponto Real'].sum() *100
    return df_avaliado


