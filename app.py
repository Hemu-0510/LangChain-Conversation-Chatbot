import streamlit as st
from langchain_ollama import ChatOllama
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
st.set_page_config(
    page_title="Local LLM Chatbot",
    page_icon="🤖"
)

st.title("Local LLM Chatbot")
st.write("Chat with a local AI model using LangChain Memory.")
if "conversation" not in st.session_state:

    llm = ChatOllama(
        model="gemma3:1b",
        temperature=0.7
    )

    memory = ConversationBufferMemory(
        memory_key="history",
        input_key="input"
    )

    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)
    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.conversation.predict(
                    input=user_input
                )
                st.write(response)
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

    except Exception as e:
        st.error(f"Error: {e}")

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.session_state.conversation.memory.clear()
    st.rerun()
