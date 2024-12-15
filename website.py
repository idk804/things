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

# Streamlit interface
st.title("AI Text Generator")
st.write(
    "Select a model to generate text based on your prompt. Unity is used as a text model in this setup."
)

# User inputs
prompt = st.text_area("Enter your prompt:", placeholder="Type your description or text for generation...")
selected_model = st.selectbox("Choose a model:", options=available_models, index=0)

# Generate button
if st.button("Generate"):
    if prompt.strip() == "":
        st.error("Please enter a prompt before generating!")
    else:
        with st.spinner("Generating response..."):
            response = gpt_text_response(prompt, selected_model)
        st.success("Generated Response:")
        st.text_area("AI Response", value=response, height=200, disabled=True)
