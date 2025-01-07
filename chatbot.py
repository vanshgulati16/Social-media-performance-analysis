import streamlit as st
import json
import requests
import logging
import sys
from typing import Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Configuration
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "e11cacf4-fca7-43d0-bbf3-2ad2095a7386"
FLOW_ID = "673f34ba-fbf2-479e-b819-a85e35aea1f2"
APPLICATION_TOKEN = "AstraCS:CPjaWjTZbAjvkCYcBZMHvZGd:e8edfb581e1fbc1aa95d9df83ec0d86d35216689562af6b3e70d84d9970c6525"  # Replace with your token

TWEAKS = {
    "ChatInput-Anfqy": {},
    "ParseData-OBh4R": {},
    "Prompt-tWgfz": {},
    "SplitText-mlz4F": {},
    "ChatOutput-mcmGS": {},
    "AstraDB-bakoN": {},
    "AstraDB-Xvf4u": {},
    "File-HynIH": {},
    "Google Generative AI Embeddings-oriEn": {},
    "Google Generative AI Embeddings-ejVuY": {},
    "GoogleGenerativeAIModel-lBYXt": {}
}

def run_flow(message: str, endpoint: str = FLOW_ID, tweaks: Optional[dict] = TWEAKS) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
    
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    
    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }
    
    if tweaks:
        payload["tweaks"] = tweaks
        
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        logging.info(f"Raw response: {response.text}")
        json_response = response.json()
        
        # Extract message from the nested response structure
        if json_response.get("outputs") and json_response["outputs"][0].get("outputs"):
            message = json_response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            return {"output": message}
        return {"error": "Unexpected response structure"}
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return {"error": str(e)}

def main():
    # Configure page and styling
    st.set_page_config(page_title="AI Chat Assistant", page_icon="💬", layout="centered")

    # Custom CSS for complete dark mode styling
    st.markdown("""
    <style>

        
        /* Chat container styling */
        .stChatMessage {
            background-color: #2D2D2D;
            border-radius: 15px;
            padding: 15px;
            margin: 5px 0;
        }
        
        /* User message styling */
        .stChatMessage[data-testid="user-message"] {
            background-color: #2B5278;
        }
        
        /* Assistant message styling */
        .stChatMessage[data-testid="assistant-message"] {
            background-color: #3D3D3D;
        }
        
        
        /* Header styling */
        .main-header {
            text-align: center;
            padding: 20px 0;
            margin-bottom: 30px;
            border-radius: 10px;
        }
        
        /* Spinner styling */
        .stSpinner > div {
            border-color: #2B5278 !important;
        }
        
        
        /* Chat input container */
        .css-1x8cf1d {
            background-color: #1E1E1E !important;
        }
        
        /* Dark scrollbar */
        ::-webkit-scrollbar {
            background-color: #1E1E1E;
            width: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background-color: #1E1E1E;
        }
        
        ::-webkit-scrollbar-thumb {
            background-color: #4D4D4D;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Custom header with gradient
    st.markdown('<div class="main-header"><h1>Social Media Assistant 💬</h1></div>', unsafe_allow_html=True)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat container
    chat_container = st.container()
    
    with chat_container:
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        # Log and display user message
        logging.info(f"User: {prompt}")
        with chat_container:
            st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get and display assistant response
        with chat_container:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = run_flow(prompt)
                    if "error" in response:
                        message = f"Error: {response['error']}"
                        st.error(message)
                    else:
                        message = response.get('output', 'No response received')
                        st.markdown(message)
                        st.session_state.messages.append({"role": "assistant", "content": message})
                    logging.info(f"Assistant: {message}")

if __name__ == "__main__":
    main()