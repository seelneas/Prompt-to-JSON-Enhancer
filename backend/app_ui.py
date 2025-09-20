import streamlit as st
import requests
import json
import os

API_URL = os.getenv("API_URL", "http://localhost:8000/enhance")


st.set_page_config(page_title="Prompt-to-JSON Enhancer", layout="centered")

st.title("🔧 Prompt-to-JSON Enhancer")
st.markdown("Convert your raw prompts into structured JSON automatically.")

user_prompt = st.text_area("✍️ Enter your prompt:", height=150)

if st.button("Enhance to JSON"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt before submitting.")
    else:
        with st.spinner("Enhancing prompt..."):
            try:
                response = requests.post(API_URL, json={"prompt": user_prompt})
                if response.status_code == 200:
                    json_output = response.json()
                    st.success("✅ Enhanced JSON:")
                    st.json(json_output) 
                else:
                    st.error(f"❌ Error: {response.status_code}\n{response.text}")
            except Exception as e:
                st.error(f"⚠️ Failed to connect to backend: {e}")
