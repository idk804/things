import streamlit as st
from g4f.client import Client

# Initialize the G4F client
client = Client()

# Updated list of available models (excluding "o1-mini" and "o1-preview")
available_models = [
    "gpt-4o-mini",  # Text generation model
    "gpt-4o",  # Text generation model
    "gpt-4",  # Text generation model
    "gpt-3.5-turbo",  # Text generation model
    "claude-3.5-sonnet",  # Text generation model
    "unity"  # Hybrid model (used as a text model in this case)
]

# Function for handling text generation with GPT-based models
def gpt_text_response(prompt, selected_model):
    try:
        # Handle text models
        response = client.chat.completions.create(
            model=selected_model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content  # Text response
    except Exception as e:
        return f"An error occurred with G4F API: {e}"  # Error message

# Apply custom CSS for a modern UI
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            color: #333333;
        }
        .stApp {
            background-color: #f5f5f5;
        }
        .main-container {
            max-width: 800px;
            margin: auto;
            padding: 2rem;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .stTextArea textarea {
            border-radius: 10px;
            font-size: 16px;
            padding: 12px;
        }
        .stSelectbox select {
            border-radius: 10px;
            font-size: 16px;
            padding: 8px;
        }
        h1 {
            text-align: center;
            color: #333333;
            font-weight: bold;
        }
        p {
            text-align: center;
            font-size: 18px;
            color: #555555;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Layout setup
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("✨ AI Text Generator")
    st.markdown(
        "Enter a prompt and select a model to generate AI-powered text. This tool uses advanced models to help you craft responses."
    )

    # User inputs
    with st.form(key="text_generator_form"):
        prompt = st.text_area(
            "Enter your prompt:",
            placeholder="Type your description or text for generation...",
            height=150,
        )
        selected_model = st.selectbox("Choose a model:", options=available_models)
        generate_button = st.form_submit_button(label="Generate")

    if generate_button:
        if prompt.strip() == "":
            st.error("⚠️ Please enter a prompt before generating!")
        else:
            with st.spinner("🔄 Generating response..."):
                response = gpt_text_response(prompt, selected_model)
            st.success("✅ Generated Response:")
            st.text_area("AI Response", value=response, height=200, disabled=True)
    st.markdown('</div>', unsafe_allow_html=True)
