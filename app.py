import pymysql
import pandas as pd
import streamlit as st
import altair as alt
from database import create_connection, get_data
from process_data import process_data, calc_avaliado_mean, gerar_dataframe_avaliado



def exibir_tabela_grafico_streamlit(df, titulo):
    st.title(titulo)

    avaliados = df['avaliado'].unique()
    for avaliado in avaliados:
        st.header(f"Avaliado: {avaliado}")
        df_avaliado = df[df['avaliado'] == avaliado]
        st.dataframe(df_avaliado[['Pergunta', 'Nota Real', 'Pesos', 'Ponto Real', 'Porcentagem Real']])
        
        # Crie um dataframe com as colunas desejadas e um rótulo "Tipo"
        df_notas = df_avaliado[['Pergunta', 'Nota Real', 'Nota desejada']].melt(id_vars='Pergunta', var_name='Tipo', value_name='Nota')
        
        grafico = (
            alt.Chart(df_notas)
            .mark_bar()
            .encode(
                x=alt.X("Pergunta:O", sort=None, axis=alt.Axis(title=None)),
                y=alt.Y("Nota:Q", axis=alt.Axis(title="Nota")),
                color=alt.Color("Tipo:N", scale=alt.Scale(scheme="category10")),
                tooltip=['Pergunta', 'Tipo', 'Nota']
            )
            .properties(width=600, height=400)
            .facet(column="Tipo:N")
        )

        st.altair_chart(grafico, use_container_width=True)


def main():
    connection = create_connection()
    pesos_assistentes = [3, 3, 2, 3, 3, 3, 2, 2, 2, 1, 3, 3, 1, 1, 2]
    notas_assistentes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

    pesos_seniores = [3,3,3,3,3,2,3,3,3,3,3,2,2,3,3,3,3]
    notas_seniores = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

    try:
        df = get_data(connection)
        df_assistants, df_seniors = process_data(df)
        medias_assistants = calc_avaliado_mean(df_assistants)
        medias_seniors = calc_avaliado_mean(df_seniors)
        df_senior_completo = gerar_dataframe_avaliado(medias_seniors, pesos_seniores, notas_seniores)
        df_assistant_completo = gerar_dataframe_avaliado(medias_assistants, pesos_assistentes, notas_assistentes)
        df_senior_completo.to_excel(r"C:\Users\bruno\Downloads\Geral seniors.xlsx", index=False)
        df_assistant_completo.to_excel(r"C:\Users\bruno\Downloads\Geral_assistants.xlsx", index=False)
        
      
    finally:
        connection.close()


    return df_senior_completo, df_assistant_completo


if __name__ == "__main__":
    df_senior_completo, df_assistant_completo = main()
    # Adicionar botão de rádio no painel lateral para alternar entre avaliações
    opcao = st.sidebar.radio("Escolha o tipo de avaliação:", ("Avaliações Assistentes", "Avaliações Seniors"))

    if opcao == "Avaliações Assistentes":
        exibir_tabela_grafico_streamlit(df_senior_completo, "Avaliações Assistentes")
    elif opcao == "Avaliações Seniors":
        exibir_tabela_grafico_streamlit(df_assistant_completo, "Avaliações Seniors")
