import streamlit as st
from googletrans import Translator

# Add custom CSS for improved visibility and styling
st.markdown("""
    <style>
        body {
            background-color: #e0f7fa;
            font-family: 'Verdana', sans-serif;
        }
        .header {
            background-color: #00796b;
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
        }
        .card {
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
        }
        .card-header {
            background-color: #004d40;
            color: white;
            padding: 10px;
            border-radius: 8px 8px 0 0;
            font-weight: bold;
        }
        .text-area {
            width: 100%;
            padding: 12px;
            border: 1px solid #00796b;
            border-radius: 8px;
            font-size: 16px;
            margin-bottom: 20px;
        }
        .btn-primary {
            background-color: #004d40;
            border: none;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
        }
        .btn-primary:hover {
            background-color: #003d33;
        }
        .translation-panel {
            background-color: #f0f4c3;  /* Light yellow background for better contrast */
            color: black;  /* Black text color for better readability */
            border-left: 5px solid #00796b;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Shadow for better visibility */
        }
        .language-tag {
            color: #00796b;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize translator
translator = Translator()

# Header of the app
st.markdown('<div class="header"><h1>Smart Language Translator</h1></div>', unsafe_allow_html=True)

# Main content area with a card layout
with st.container():
    st.markdown('<div class="card"><div class="card-header">Input Text</div>', unsafe_allow_html=True)
    input_text = st.text_area("Type or paste your text here:", height=150, key="input_text", help="Enter the text you want to translate.", 
                              label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Multi-select for languages
    languages = {'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani',
                 'bn': 'Bengali', 'be': 'Belarusian', 'bg': 'Bulgarian', 'ca': 'Catalan', 'zh-cn': 'Chinese (Simplified)', 
                 'zh-tw': 'Chinese (Traditional)', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 
                 'en': 'English', 'fr': 'French', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'hi': 'Hindi', 
                 'hu': 'Hungarian', 'is': 'Icelandic', 'it': 'Italian', 'ja': 'Japanese', 'ko': 'Korean', 'ml': 'Malayalam', 
                 'pt': 'Portuguese', 'ru': 'Russian', 'es': 'Spanish', 'ta': 'Tamil', 'te': 'Telugu', 'tr': 'Turkish', 
                 'vi': 'Vietnamese'}
    
    st.markdown('<div class="card"><div class="card-header">Select Target Languages</div>', unsafe_allow_html=True)
    selected_languages = st.multiselect("Choose languages:", options=list(languages.values()), 
                                        help="Select the languages you want to translate to.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Translate button with custom style
    if st.button("Translate Now", key="translate_button", help="Click to start the translation.", 
                 use_container_width=True):
        if input_text.strip():
            detected_lang_code = translator.detect(input_text).lang
            detected_language = languages.get(detected_lang_code, 'Unknown')

            # Display detected language
            st.markdown(f'<div class="card"><div class="card-header">Detected Language</div>'
                        f'<div class="translation-panel">Detected Language: <span class="language-tag">{detected_language}</span></div></div>',
                        unsafe_allow_html=True)

            if selected_languages:
                for lang in selected_languages:
                    target_lang_code = [code for code, name in languages.items() if name == lang][0]
                    translation = translator.translate(input_text, src=detected_lang_code, dest=target_lang_code)
                    st.markdown(f'<div class="translation-panel"><strong>{lang}:</strong> {translation.text}</div>',
                                unsafe_allow_html=True)
            else:
                st.markdown('<div class="card"><div class="card-header">Error</div>'
                            '<div class="translation-panel">Please select at least one target language.</div></div>',
                            unsafe_allow_html=True)
        else:
            st.markdown('<div class="card"><div class="card-header">Error</div>'
                        '<div class="translation-panel">Please enter some text to translate.</div></div>',
                        unsafe_allow_html=True)
