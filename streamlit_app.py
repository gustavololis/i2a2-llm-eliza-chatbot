import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from eliza import eliza_response

# Carregando chave da openai salva localmente
# import configparser
# from os import path
# config = configparser.ConfigParser()
# config.read_file(open(path.dirname(__file__) + '/config.properties'))
# openai_api_key = config.get('open_ai', 'openai_api_key')
openai_api_key = st.sidebar.text_input('OpenAI API Key')

template = (
    '''Você é um psiquiatra e psicólogo, que só fala a língua portuguesa brasileira, mas não pode dar diagnósticos e prescrever terapias medicamentosas. 
       Você é educado, cordial e atencioso, pergunta a respeito da saúde mental e física, possíveis condições referentes ao estado psíquico, 
       tal qual quadros ansiosos, depressivos, maníacos e comportamentais importantes. Você acolhe o paciente e dá conselhos clínicos e de mudanças
       comportamentais que podem ajudar o paciente. Quando o paciente referir sentimentos tristes, demonstre compaixão, se forem bons sentimentos, 
       demonstre alegria, sobre sentimentos neutros, apenas acompanhe. Se o paciente já tiver um diagnóstico, você se aprofunda nos sintomas da doença 
       diagnosticada para entender as circunstâncias. Além disso, o ensina a entender o próprio processo saúde/doença e sugere qual profissional deve buscar e 
       ajuda o usuário a entender o que tem passado, sugerindo mudanças comportamentais, medidas e atitudes que demonstram respostas positivas quanto aos sinais 
       e sintomas. Você o questiona sempre sobre a possibilidade de ideação suicida e automutilação, você a aconselha a procurar e onde encontrar ajuda 
       (telefones, sites, unidades de saúde, etc.).'''
)
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)



st.title('Eliza Chatbot - Desafio I2A2')
st.info('Olá! Sou Eliza, a terapeuta virtual. Como posso ajudá-lo hoje?')

def generate_response(input_text):
    chat = ChatOpenAI(temperature=0.7,
                     openai_api_key=openai_api_key,
                     model_name="gpt-3.5-turbo",
                     max_tokens=256,
                     max_retries=1)
    # st.info(chat.completion_with_retry(input_text))

    # st.info(chat(input_text=input_text))
    
    ai_message = chat(
        chat_prompt.format_prompt(
            text=input_text
        ).to_messages()
    )
    #st.info(ai_message.content)
    return ai_message.content


with st.form('my_form'):
    text = st.text_area('Você:', '')
    submitted = st.form_submit_button('Submit')
    #if not openai_api_key.startswith('sk-'):
    #    st.warning('Por favor informe sua OpenAI API key!', icon='⚠')
    try:
        if submitted and openai_api_key.startswith('sk-'):
            st.info('Eliza: ' + generate_response(text))
        elif submitted:
            st.info('Eliza: ' + eliza_response(input_text=text))
    except Exception as e:
        st.warning('No momento não posso atender, por favor tente mais tarde, ou ligue para um serviço de emergência.')        
        st.warning(type(e))
        st.warning(e)
            