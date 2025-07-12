import streamlit as st
from gtts import gTTS
import os
import tempfile
import base64
import json

# Load equipment data
with open("equipment_data.json", "r", encoding="utf-8") as f:
    equipment_data = json.load(f)

st.title("🩺 Medical Equipment Description using LLMs")
st.markdown("Get quick, multilingual descriptions of medical devices.")

# User Input
device = st.selectbox("Select Medical Equipment:", list(equipment_data.keys()))
language = st.radio("Choose Language:", ["English", "Hindi", "Gujarati"])

lang_code = {"English": "en", "Hindi": "hi", "Gujarati": "gu"}[language]

# Output Description
st.subheader("📄 Description:")
desc = equipment_data[device][lang_code]
st.write(desc)

# Voice Output
if st.button("🔊 Speak"):
    tts = gTTS(text=desc, lang=lang_code)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio_path = fp.name
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
        b64_audio = base64.b64encode(audio_bytes).decode()
        st.audio(f"data:audio/mp3;base64,{b64_audio}", format="audio/mp3")
