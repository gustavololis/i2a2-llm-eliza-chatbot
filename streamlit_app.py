import streamlit as st
import time
from eliza import eliza_response
from llm import generate_response_with_openAi_app

openai_api_key = st.sidebar.text_input('OpenAI API Key')

st.title('Eliza Chatbot - Desafio I2A2')
st.info('Olá! Sou Eliza, a terapeuta virtual. Como posso ajudá-lo hoje?')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escreva aqui"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = ''
    with st.chat_message("assistant"):
        try:
            if openai_api_key.startswith('sk-'):
                response = generate_response_with_openAi_app(input_text=prompt, openai_api_key=openai_api_key)
            else:
                response = eliza_response(input_text=prompt)

            # Simulando digitação no teclado
            message_placeholder = st.empty()
            full_response = ''
            for chunk in response.split():
                for char in chunk:
                    full_response += char
                    time.sleep(0.10)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌")
                full_response += ' '
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception:
            st.warning('No momento não posso atender, \
                        por favor ligue ligue para o CVV, telefone 188.')
            # st.warning(type(e))
            # st.warning(e)
