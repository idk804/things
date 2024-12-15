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

# Apply custom CSS for a futuristic, modern design
st.markdown(
    """
    <style>
        /* Body and container styling */
        .stApp {
            background: linear-gradient(135deg, #ffafbd, #ffc3a0);
            font-family: 'Poppins', sans-serif;
            color: #333;
            padding: 0;
        }

        /* Main container */
        .main-container {
            max-width: 900px;
            margin: auto;
            padding: 3rem;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
        }

        /* Title styling */
        h1 {
            font-size: 3rem;
            font-weight: 700;
            color: #2c3e50;
            text-align: center;
            letter-spacing: 1px;
        }

        h2 {
            font-size: 1.5rem;
            color: #34495e;
            text-align: center;
            margin-top: -10px;
            font-weight: 500;
        }

        /* Model selector and prompt input styling */
        .stSelectbox select, .stTextArea textarea {
            border-radius: 12px;
            font-size: 16px;
            padding: 12px;
            border: 1px solid #e0e0e0;
            transition: all 0.3s ease;
            width: 100%;
        }

        .stSelectbox select:hover, .stTextArea textarea:hover {
            border-color: #3498db;
        }

        /* Button styling */
        .stButton button {
            background: #3498db;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            padding: 14px 30px;
            cursor: pointer;
            transition: 0.3s ease;
        }
        .stButton button:hover {
            background: #2980b9;
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
        }

        /* Response box styling */
        .response-box {
            padding: 20px;
            background: #ecf0f1;
            border-radius: 12px;
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
            white-space: pre-wrap;
            margin-top: 2rem;
            font-size: 16px;
            font-weight: 500;
            color: #2c3e50;
            transition: all 0.3s ease;
        }

        /* Animation for response */
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        .response-box {
            animation: fadeIn 0.8s ease-in-out;
        }

    </style>
    """,
    unsafe_allow_html=True,
)

# Layout setup
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Header
st.markdown('<h1>🌟 AI Text Generator 🌟</h1>', unsafe_allow_html=True)
st.markdown(
    '<h2>Enter a prompt, choose a model, and let the AI generate your content.</h2>',
    unsafe_allow_html=True,
)

# Input fields
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Type something creative or descriptive...",
    height=180,
    key="prompt_input",
)
selected_model = st.selectbox(
    "Choose a model:",
    options=available_models,
    key="model_selector",
)

# Action button for text generation
if st.button("Generate Response", key="generate_button"):
    if not prompt.strip():
        st.error("⚠️ Please enter a valid prompt!")
    else:
        with st.spinner("🔄 Generating AI response..."):
            response = gpt_text_response(prompt, selected_model)

        # Displaying response with smooth animation and polished box
        st.markdown('<div class="response-box">', unsafe_allow_html=True)
        st.write(response)
        st.markdown('</div>', unsafe_allow_html=True)

# Closing container
st.markdown('</div>', unsafe_allow_html=True)
