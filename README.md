# README: Gerador de Relatório Financeiro usando LangChain e Streamlit

## Descrição do Projeto
Este projeto é uma aplicação web simples desenvolvida com **Streamlit** e **LangChain** para gerar relatórios financeiros detalhados de empresas, utilizando o modelo de IA **Google Generative AI**. O usuário pode selecionar a empresa, o período, a análise desejada e o idioma. O relatório é gerado dinamicamente e apresentado na interface, utilizando Markdown para estilização quando possível.

## Link do Projeto
https://geradorrelatorios-victimnn.streamlit.app/
---

## Funcionalidades
- **Seleção de Empresa:** Empresas pré-definidas (Google, Apple, Intel, Nvidia e Meta).
- **Período Personalizável:** Seleção de trimestre e ano.
- **Análise Financeira:** Tipos de análises, como:
  - Balanço Patrimonial
  - Fluxo de Caixa
  - Tendências de Mercado
  - Receita e Lucro
  - Posição de Mercado
- **Idioma:** O relatório pode ser gerado em múltiplos idiomas (Português, Inglês, Espanhol, Francês, e Alemão).
- **Integração com Google Generative AI:** Geração automática de conteúdo a partir de prompts configurados.

---

## Pré-requisitos
- **Python 3.8+**
- **Streamlit**: Biblioteca para construção de aplicações web.
- **LangChain**: Framework para orquestrar modelos de linguagem.
- **Google Generative AI**: É necessário fornecer uma chave de API válida.
- **config.yaml**: Arquivo de configuração contendo a chave da API.
---

## Funcionamento do Código

### Importações
```python
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os
import yaml
```
Essas bibliotecas permitem criar a interface web e interagir com o modelo generativo do Google.

### Carregamento da Configuração
```python
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
os.environ['GOOGLE_API_KEY'] = config['GOOGLE_API_KEY']
```
Aqui, a chave de API é carregada do arquivo `config.yaml` e definida como uma variável de ambiente.

### Configuração do Modelo e Prompt
```python
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0)

template = '''
Você é um analista financeiro.
Escreva um relatório financeiro detalhado para a empresa "{empresa}" para o período {periodo}.
O relatório deve ser escrito em {idioma} e incluir a seguinte análise:
{analise}
Certifique-se de fornecer insights e conclusões para esta seção.
Formate o relatório utilizando Markdown para a criacao de tabelas e estilização quando possível.
'''

prompt_template = PromptTemplate.from_template(template=template)
```
- O modelo **Gemini 1.5** é utilizado para gerar relatórios financeiros com uma temperatura de 0 (mais determinístico).  
- O **prompt** é configurado para definir a estrutura do relatório com variáveis dinâmicas, como empresa, período, idioma e tipo de análise.

### Interface com Streamlit
```python
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
```
Essas listas definem as opções disponíveis no menu lateral para o usuário.

### Lógica para Geração do Relatório
```python
st.title('Gerador de Relatório Financeiro:')

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
```
- A interface possui menus laterais para selecionar empresa, período, idioma e tipo de análise.  
- Quando o botão **Gerar Relatório** é clicado, o prompt é preenchido com os valores selecionados e enviado ao modelo generativo.  
- O relatório é exibido dinamicamente na tela usando **Markdown**.

---

## Exemplo de Uso
1. Selecione a empresa **Google**.
2. Escolha o período **Q2 2024**.
3. Selecione o idioma **Português** e a análise **Análise do Fluxo de Caixa**.
4. Clique em **Gerar Relatório** para ver o relatório detalhado gerado.

---

## Conclusão
Este projeto demonstra o uso prático de modelos de linguagem generativa para gerar relatórios financeiros personalizados. A combinação de **LangChain** e **Streamlit** oferece uma interface intuitiva e funcional para o usuário, enquanto a integração com o Google Generative AI garante uma geração de texto precisa e dinâmica.

---

Licença
Este projeto é licenciado sob a licença MIT.
