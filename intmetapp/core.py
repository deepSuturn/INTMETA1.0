import pandas as pd
import re
import sys
import os

def kraken(fileinput, taxonomiclevel):
    # Leitura inicial de dados
    df_data = pd.read_csv(fileinput, header=None, low_memory=False, sep='\t')

    # Adiciona cabecalho para cada coluna para o output KRAKEN.

    # Info0 se refere a PORCENTAGEM
    # Info1 se refere ao numero de Reads correspondentes a taxonomia
    # Info2 se refere ao numero de Reads correspondentes DIRETAS a taxonomia
    # Info3 se refere ao filo, reino, etc...
    # Info4 se refere ao ID do NCBI
    # Info5 se refere ao nome cientifico.

    df_data.columns = ['Info0', 'Info1', 'Info2', 'Info3', 'Info4', 'Info5']

    # Separa somente os correspondentes a filo, reino, etc...
    df_data2 = df_data.loc[df_data['Info3'] == taxonomiclevel.upper()]

    # Retira espacamento da output KRAKEN
    df_data2 = df_data2.replace(' ', '', regex=True)

    # Novo dataframe somente com dados de nome e numero de reads (Info1)
    output_df = df_data2[['Info5', 'Info0']].copy()

    # Substituição dos cabecalhos para melhor visualizacao no D3.JS
    # Segue a logica (Original:Saida_D3JS)

    output_df = output_df.rename(columns={'Info0': 'Info2', 'Info5': 'Info1'}, inplace=False)

    # Descomentar codigo para girar o dataframe caso for necessario em outra formatacao de visualizacao
    # output_df = output_df.transpose()

    # Pega apenas os 30 com maior numero de reads.
    output_df_out = output_df.nlargest(10, 'Info2')
    # output_df_out.reset_index(drop=True, inplace=True)


    # Caso a output seja girada, substituir Index por true e header por false
    dfd3 = output_df_out.to_dict('r')
    maxpercent = output_df_out['Info2'].iloc[0]
    return dfd3, maxpercent

def clark(fileinput, taxonomiclevel):
    # Leitura inicial de dados
    dummydata = taxonomiclevel
    df_data = pd.read_csv(fileinput, low_memory=False, sep=',')

    # Adiciona cabecalho para cada coluna para o output Metamaps.

    # Info0 se refere ao Nome
    # Info1 se refere ao TaxID
    # Info2 se refere a linhagem
    # Info3 se refere ao numero de reads correspondentes a taxonomia
    # Info4 se refere a proporção em % sobre o numero de sequencias totais.
    # Info5 se refere a proporção de % em sequencias classificadas

    df_data.columns = ['Info0', 'Info1', 'Info2', 'Info3', 'Info4', 'Info5']

    # Novo dataframe somente com dados de nome e numero de reads (Info1)
    output_df = df_data[['Info0', 'Info5']].copy()

    # Substituição dos cabecalhos para melhor visualizacao no D3.JS
    output_df = output_df.rename(columns={'Info5': 'Info2', 'Info0': 'Info1'}, inplace=False)

    # Descomentar codigo para girar o dataframe caso for necessario em outra formatacao de visualizacao
    # Se deleta uma linha do final do arquivo do CLARK
    output_df = output_df[:-1]
    
    # É necessária a conversão de uma tabela pra numérica
    output_df["Info2"] = output_df["Info2"].apply(pd.to_numeric)

    # Pega apenas os 30 com maior numero de reads.
    output_df_out = output_df.nlargest(10, 'Info2')
    
    # Retira maior porcentagem
    maxpercent = output_df_out['Info2'].iloc[0]

    # Caso a output seja girada, substituir Index por true e header por false
    print(output_df_out)
    dfd3 = output_df_out.to_dict('r')
    
    return dfd3, maxpercent

def metamaps(fileinput, taxonomiclevel):
    # Leitura inicial de dados
    df_data = pd.read_csv(fileinput, header=None, low_memory=False, sep='\t')

    # Adiciona cabecalho para cada coluna para o output Metamaps.

    # Info0 se refere ao Nome
    # Info1 se refere ao TaxID
    # Info2 se refere ao filo, reino, etc...
    # Info3 se refere ao tamanho do genoma
    # Info4 se refere ao numero de reads correspondentes a taxonomia
    # Info5 se refere ao numero de reads correspondentes DIRETAS a taxonomia
    # Info6 Abundancia

    df_data.columns = ['Info0', 'Info1', 'Info2', 'Info3', 'Info4', 'Info5', 'Info6']

    # Separa somente os correspondentes a filo, reino, etc...
    df_data2 = df_data.loc[df_data['Info2'] == taxonomiclevel.lower()]

    # Novo dataframe somente com dados de nome e numero de reads (Info1)
    output_df = df_data2[['Info0', 'Info4']].copy()

    # Substituição dos cabecalhos para melhor visualizacao no D3.JS
    output_df = output_df.rename(columns={'Info4': 'Info2', 'Info0': 'Info1'}, inplace=False)

    # Descomentar codigo para girar o dataframe caso for necessario em outra formatacao de visualizacao
    # output_df = output_df.transpose()

    # Pega apenas os 30 com maior numero de reads. (Esse comando precisa ser adaptado ao metamaps)
    # output_df_out = output_df.nlargest(30, 'Sample')

    # Caso a output seja girada, substituir Index por true e header por false
    print(output_df)
    dfd3 = output_df.to_dict('r')
    
    return dfd3