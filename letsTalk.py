import time
import streamlit as st
from excuses import Excuses
from prompts import PromptCls
from geminiKey import GeminiKey
import google.generativeai as geminiai



def LetsTalk():
    
    
    geminiai.configure(api_key = str(GeminiKey()))  # "AIzaSyAde1168Yh8ORh8GS-jFMWMDNg7h5RbiHw"
    ################################################
    
    model = geminiai.GenerativeModel("gemini-pro")
    ################################################
    # st.title("`General Chatbot`")
    st.info("This is an AI general chatbot. Put your query here. Thank you!")
    container_1 = st.container(height = 350, border = False)

    ################################################
        
    if "messages_temp_12" not in st.session_state:
        st.session_state.messages_temp_12 = []

    

    with container_1:
        for message in st.session_state.messages_temp_12:
            with st.chat_message(message["role"]):
                st.markdown(message["content"], unsafe_allow_html = True)

    if prompt := st.chat_input("Ask me anything!"):
        st.session_state.messages_temp_12.append({"role": str("Let's talk")+"user", "content": prompt})
        with container_1:
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
               
                with st.spinner(":green[just wait . . .]"):
                    try: 
                        full_response = ""
                        prompt = PromptCls.ConversationPromptStyle(prompt)
                        response = model.generate_content(prompt)
                        for responses in response.text:
                            full_response += responses
                            message_placeholder.markdown(full_response + "▌")
                            time.sleep(0.001)
                        message_placeholder.markdown(full_response)
                    except Exception as e:
                        full_response = Excuses.listofExcuses()
                        temp_full_response = ''
                        for i in full_response:
                            temp_full_response += i
                            message_placeholder.markdown(temp_full_response + "▌")
                            time.sleep(0.01)
                        message_placeholder.markdown(full_response)
            st.session_state.messages_temp_12.append({"role": str("Generic Chatbot")+"assistant", "content": full_response})
