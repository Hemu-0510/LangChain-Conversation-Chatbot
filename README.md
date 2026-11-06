# Local LLM Chatbot with LangChain Conversation Memory

## Project Overview

This project is a simple AI-powered chatbot developed using a Local Large Language Model (LLM), LangChain, and Streamlit. It uses the Gemma 3:1B model through Ollama to generate intelligent responses and maintain conversation history using ConversationBufferMemory.

The chatbot provides an interactive interface where users can ask questions and continue conversations while the system remembers previous messages.

## Objective

The main objective of this project is to develop a chatbot using a locally running LLM and implement conversation memory using LangChain. It also aims to provide a user-friendly interface using Streamlit.

## Technologies Used

- **Python:** Main programming language.
- **Ollama:** Runs the language model locally.
- **Gemma 3:1B:** Local AI language model.
- **LangChain:** Connects the language model with conversation memory.
- **ConversationBufferMemory:** Stores previous conversations.
- **Streamlit:** Creates the chatbot web application.

## Key Features

1. **Local AI Chatbot:** Generates responses using the Gemma 3:1B model.
2. **Conversation Memory:** Remembers previous questions and answers during the current session.
3. **Interactive Interface:** Provides a simple and user-friendly chat experience.
4. **Clear Chat Option:** Allows users to clear the conversation history.
5. **Custom Dashboard:** Includes a professional green and cream colour theme.
6. **Local Execution:** Runs the AI model on the user's computer through Ollama.


## Working Process

1. The user enters a message in the Streamlit chatbot.
2. The message is passed to the LangChain conversation chain.
3. Ollama processes the input using the Gemma 3:1B model.
4. ConversationBufferMemory maintains the previous conversation.
5. The chatbot generates and displays a response.
6. Users can continue the conversation with the stored context.

## Expected Output

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/8e152dd0-3a3a-40ed-a98a-09e2cd2d58b3" />

## Conclusion

This project demonstrates the implementation of a local AI chatbot using Ollama and LangChain. By integrating ConversationBufferMemory, the chatbot can maintain conversational context and provide more meaningful responses. Streamlit makes the application interactive and easy to use.
