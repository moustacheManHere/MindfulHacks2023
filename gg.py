import streamlit as st
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntity
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.llms import openai
from langchain.callbacks import get_openai_callback
import re

# init session state
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""
if "store_session" not in st.session_state:
    st.session_state["store"]

def get_text():
    """
    Get the user input text.
    Returns:
        (str): The text entered by the user
    """
    input_text = st.text_input("You: ", st.session_state["input"], key="input",
                               placeholder="Your Ai assistant here! Ask me anything ...",
                               label_visibility='hidden')
    return input_text

st.title("Memory Bot")
