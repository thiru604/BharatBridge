import streamlit as st
import os
import tempfile
from translator import translate_to_native, translate_to_english, get_supported_languages
from gtts import gTTS

# Page config
st.set_page_config(
    page_title="BharatBridge",
    page_icon="🇮🇳",
    layout="centered"
)

def text_to_speech(text, lang_code):
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tmp_path = tempfile.mktemp(suffix=".mp3")
        tts.save(tmp_path)
        return tmp_path
    except:
        return None

# Header
st.title("🇮🇳 BharatBridge")
st.subheader("Breaking language barriers in Indian workplaces")
st.divider()

# Sidebar
languages = get_supported_languages()
lang_names = list(languages.keys())

st.sidebar.title("⚙️ Settings")
selected_lang_name = st.sidebar.selectbox(
    "Your Native Language",
    lang_names
)
selected_lang_code = languages[selected_lang_name]
st.sidebar.success(f"Language: {selected_lang_name}")

# Two tabs
tab1, tab2 = st.tabs(["📝 Text Translation", "🎤 Voice Translation"])

# ─── TAB 1 — Text ───────────────────────────
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📥 Input")
        direction = st.radio(
            "Direction",
            ["English → Native", "Native → English"]
        )
        input_text = st.text_area(
            "Enter message",
            height=150,
            placeholder="Type your message..."
        )

    with col2:
        st.markdown("### 📤 Output")
        output_box = st.empty()

    if st.button("🔄 Translate", use_container_width=True):
        if input_text.strip() == "":
            st.warning("Please enter some text!")
        else:
            with st.spinner("Translating..."):
                if direction == "English → Native":
                    result = translate_to_native(
                        input_text, selected_lang_code
                    )
                else:
                    result = translate_to_english(
                        input_text, selected_lang_code
                    )

            with col2:
                st.markdown("### 📤 Output")
                st.success(result)

                lang = selected_lang_code if direction == "English → Native" else "en"
                audio_path = text_to_speech(result, lang)
                if audio_path:
                    st.audio(audio_path)
                    os.unlink(audio_path)

# ─── TAB 2 — Voice ──────────────────────────
with tab2:
    st.markdown("### 🎤 Voice Translation")
    st.warning("⚠️ Voice transcription requires significant compute resources.")
    st.info("""
    **Voice translation is available when running locally:**
    
    1. Clone the repo: `git clone https://github.com/thiru604/BharatBridge`
    2. Install requirements: `pip install -r requirements.txt`
    3. Run: `streamlit run app.py`
    
    Use **Text Translation** tab above — works fully online! ✅
    """)
    st.markdown("**GitHub:** https://github.com/thiru604/BharatBridge")
