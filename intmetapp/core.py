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

    # Pega apenas os 10 com maior numero de reads.
    output_df_out = output_df.nlargest(10, 'Info2')

    # Transforma o dataframe para dicionário que será exportado como JSON para o D3JS
    dfd3 = output_df_out.to_dict('r')
    
    # Retira maior porcentagem para ser parametro de tamanho do gráfico
    maxpercent = output_df_out['Info2'].iloc[0]
    return dfd3, maxpercent

def clark(fileinput, taxonomiclevel):
    # Clark não possui parametro de escolha de nivel taxonomico em sua output, logo valor é descartado.
    dummydata = taxonomiclevel

    # Leitura inicial de dados
    df_data = pd.read_csv(fileinput, low_memory=False, sep=',')

    # Adiciona cabecalho para cada coluna para o output Clark.

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
    # Segue a logica (Original:Saida_D3JS)
    output_df = output_df.rename(columns={'Info5': 'Info2', 'Info0': 'Info1'}, inplace=False)

    # Se deleta uma linha do final do arquivo do CLARK
    output_df = output_df[:-1]
    
    # É necessária a conversão de uma tabela pra numérica
    output_df["Info2"] = output_df["Info2"].apply(pd.to_numeric)

    # Pega apenas os 10 com maior numero de porcentagem.
    output_df_out = output_df.nlargest(10, 'Info2')
    
    # Retira maior porcentagem para ser parametro de tamanho do gráfico
    maxpercent = output_df_out['Info2'].iloc[0]
    
    # Transforma o dataframe para dicionário que será exportado como JSON para o D3JS
    dfd3 = output_df_out.to_dict('r')
    
    return dfd3, maxpercent

# DESCONSIDERAR METAMAPS, É NECESSÁRIO ATUALIZAR.
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

    # Pega apenas os 10 com maior numero de porcentagem. (Esse comando precisa ser adaptado ao metamaps)
    # output_df_out = output_df.nlargest(30, 'Sample')

    # Caso a output seja girada, substituir Index por true e header por false
    print(output_df)
    dfd3 = output_df.to_dict('r')
    
    return dfd3
