import streamlit as st
from translator import translate_to_native, translate_to_english, get_supported_languages

# Page config
st.set_page_config(
    page_title="BharatBridge",
    page_icon="🇮🇳",
    layout="centered"
)

# Header
st.title("🇮🇳 BharatBridge")
st.subheader("Breaking language barriers in Indian workplaces")
st.divider()

# Get supported languages
languages = get_supported_languages()
lang_names = list(languages.keys())

# Sidebar — user settings
st.sidebar.title("⚙️ Settings")
selected_lang_name = st.sidebar.selectbox(
    "Your Native Language",
    lang_names
)
selected_lang_code = languages[selected_lang_name]
st.sidebar.success(f"Language set to: {selected_lang_name}")

# Main area
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 Input")
    direction = st.radio(
        "Translation Direction",
        ["English → Native", "Native → English"]
    )
    input_text = st.text_area(
        "Enter message here",
        height=150,
        placeholder="Type your message..."
    )

with col2:
    st.markdown("### 📤 Output")
    output_placeholder = st.empty()

# Translate button
if st.button("🔄 Translate", use_container_width=True):
    if input_text.strip() == "":
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Translating..."):
            if direction == "English → Native":
                result = translate_to_native(input_text, selected_lang_code)
            else:
                result = translate_to_english(input_text, selected_lang_code)

        with col2:
            st.markdown("### 📤 Output")
            st.success(result)

        # Show details
        st.divider()
        st.markdown("#### Translation Details")
        detail_col1, detail_col2, detail_col3 = st.columns(3)
        with detail_col1:
            st.metric("Direction", direction.split("→")[0].strip())
        with detail_col2:
            st.metric("Language", selected_lang_name)
        with detail_col3:
            st.metric("Words", len(input_text.split()))

# Footer
st.divider()
st.caption("BharatBridge — Built for India's workforce 🇮🇳")