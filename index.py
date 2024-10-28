import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os

GOOGLE_API_KEY = st.secrets["general"]["GOOGLE_API_KEY"]

os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0)

template = '''
Você é um analista financeiro e consultor especializado em investimentos.
Sua tarefa é elaborar um relatório financeiro detalhado sobre a empresa "{empresa}" referente ao período {periodo}, utilizando dados disponíveis na internet e em sua base de dados.

Instruções:
O relatório deve ser escrito em {idioma}.
Inclua a seguinte análise:
{analise}
Estrutura e Requisitos:
Introdução:

Breve resumo da empresa (histórico, setor, principais produtos/serviços).
Objetivo do relatório e contexto relevante para o período analisado.
Desempenho Financeiro:

Demonstrativos financeiros (DRE, Balanço Patrimonial, Fluxo de Caixa).
Análise de indicadores-chave (rentabilidade, liquidez, alavancagem, etc.).
Análise de Mercado:

Condições econômicas e tendências do setor.
Comparação com concorrentes e benchmarks relevantes.
Riscos e Oportunidades:

Identificação de fatores externos e internos que podem impactar o desempenho futuro.
Conclusão e Recomendações:

Principais insights obtidos da análise.
Sugestões para investidores e previsões estratégicas.
Formatação e Estilo:
Utilize Markdown para criar tabelas, listas e outros elementos de formatação que melhorem a organização visual e a clareza do relatório.
Certifique-se de apresentar insights relevantes e fundamentar suas conclusões com base nos dados analisados.
'''

prompt_template = PromptTemplate.from_template(template=template)

empresas = ['Google', 'Apple', 'Intel', 'Nvidia', 'Meta']
trimestres = ['Q1', 'Q2', 'Q3', 'Q4']
anos = [2021, 2022, 2023, 2024]
idiomas = ['Português', 'Inglês', 'Espanhol', 'Francês', 'Alemão']
analises = [
    "Análise do Balanço Patrimonial",
    "Análise do Fluxo de Caixa",
    "Análise de Tendências",
    "Análise de Receita e Lucro",
    "Análise de Posição de Mercado"
]

st.title('Gerador de Relatórios Financeiros:')

empresa = st.sidebar.selectbox('Selecione a empresa:', empresas)
trimestre = st.sidebar.selectbox('Selecione o trimestre:', trimestres)
ano = st.sidebar.selectbox('Selecione o ano:', anos)
periodo = f"{trimestre} {ano}"
idioma = st.sidebar.selectbox('Selecione o idioma:', idiomas)
analise = st.sidebar.selectbox('Selecione a análise:', analises)

if st.sidebar.button('Gerar Relatório'):
    prompt = prompt_template.format(
        empresa=empresa,
        periodo=periodo,
        idioma=idioma,
        analise=analise
    )

    response = llm.invoke(prompt)

    st.subheader('Relatório Gerado:')
    st.write(response.content)
