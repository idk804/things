import streamlit as st
import g4f
import os

# Configuração da página
st.set_page_config(page_title="Modern Streamlit Chatbot", layout="centered")

# Definir o provedor e os modelos disponíveis
provider = g4f.Provider.Blackbox
available_models = [
    "o1",
    "o3-mini",
    "deepseek-r1",
    "gpt-4o",
    "claude-3.7-sonnet"
]

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f8fafe;
        margin: 0;
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }
    .chat-message {
        display: inline-block;
        border-radius: 12px;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 75%;
    }
    .chat-bot {
        background-color: #e8f1ff;
        text-align: left;
        color: #333;
    }
    .chat-user {
        background-color: #2b73de;
        color: #fff;
        text-align: right;
        float: right;
    }
    .header {
        display: flex;
        justify-content: center;
        font-size: 2rem;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #333;
    }
    .chat-container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        padding: 10px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #f0f2f6;
        padding: 15px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho
st.markdown("<div class='header'>Modern Streamlit Chatbot</div>", unsafe_allow_html=True)
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# Inicializar histórico do chat
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Exibir mensagens anteriores
for chat in st.session_state["messages"]:
    role = chat["role"]
    content = chat["content"]
    css_class = "chat-bot" if role == "assistant" else "chat-user"
    st.markdown(f"<div class='chat-message {css_class}'>{content}</div>", unsafe_allow_html=True)
    st.write("<div style='clear: both;'></div>", unsafe_allow_html=True)

# Entrada de usuário e upload de imagem
user_input = st.chat_input("Digite sua mensagem...")
uploaded_images = st.file_uploader("Envie imagens:", type=["jpg", "jpeg", "png", "webp"], accept_multiple_files=True)

# Selecionar modelo
selected_model = st.selectbox("Selecione o modelo:", available_models)

# Processar resposta
def gpt_response(prompt, selected_model, images=None):
    try:
        saved_images = []
        if images:
            image_dir = "uploaded_images"
            os.makedirs(image_dir, exist_ok=True)
            for image in images:
                file_path = os.path.join(image_dir, image.name)
                with open(file_path, "wb") as f:
                    f.write(image.getbuffer())
                saved_images.append(file_path)

        response = g4f.ChatCompletion.create(
            provider=provider,
            model=selected_model,
            messages=[{"role": "user", "content": prompt}],
            images=saved_images if images else None
        )
        return response if response else "❌ Erro ao obter resposta da IA"
    except Exception as e:
        return f"⚠️ Erro: {e}"

# Se usuário enviar mensagem ou imagem, processa a resposta
if user_input or uploaded_images:
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})

    response = gpt_response(user_input, selected_model, uploaded_images)

    st.session_state["messages"].append({"role": "assistant", "content": response})

    st.rerun()  # Atualiza a interface para exibir novas mensagens

# Rodapé
st.markdown("<div class='footer'></div>", unsafe_allow_html=True)
