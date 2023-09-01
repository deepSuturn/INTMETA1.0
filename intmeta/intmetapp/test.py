import pandas as pd


def centrifuge(fileinput, taxonomiclevel):

    # Leitura inicial de dados
    df_data = pd.read_csv(fileinput, header=[0], low_memory=False, sep='\t')
    # ----------------------------------------------------------------------
    # Dataframe #1 - Porcentagens totais
    # ----------------------------------------------------------------------
    # Cabecalho para cada coluna para o output KRAKEN 1 E KRAKEN 2.

    # Info0 se refere ao Nome Cientifico
    # Info1 se refere ao taxID
    # Info2 se refere ao filo, reino, etc...
    # Info3 se refere ao tamanho do genoma
    # Info4 se refere ao numero de reads
    # Info5 se refere ao numero de reads unicas.
    # Info6 se refere a abundancia
    # Info7 se refere a porcentagem

    df_data.columns = ['Info0', 'Info1', 'Info2', 'Info3', 'Info4', 'Info5', 'Info6']
    # Consegue numero total de reads para referencia de porcentagem
    totalreads = df_data['Info4'].sum()
    for index, row in df_data.iterrows():
        x = row['Info4'] * 100
        y = x / totalreads
        y = round(y, 2)
        df_data.at[index, 'Info4'] = y
        print(y)
    print(totalreads)
    # Separa somente os correspondentes a filo, reino, etc...
    # df_data = df_data.loc[df_data['Info2'] == taxonomiclevel.lower()]

    return df_data


print(centrifuge('../../OutputsModel/SRR4414933_FASTQ-CENTRIFUGE-OUTPUT.tsv', 'genus'))
