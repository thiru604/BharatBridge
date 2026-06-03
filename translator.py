from deep_translator import GoogleTranslator

def translate_to_native(text, target_lang="hi"):
    try:
        translated = GoogleTranslator(
            source='en',
            target=target_lang
        ).translate(text)
        return translated
    except Exception as e:
        return f"Translation error: {str(e)}"

def translate_to_english(text, source_lang="hi"):
    try:
        translated = GoogleTranslator(
            source=source_lang,
            target='en'
        ).translate(text)
        return translated
    except Exception as e:
        return f"Translation error: {str(e)}"

def get_supported_languages():
    return {
        "Hindi": "hi",
        "Tamil": "ta",
        "Telugu": "te",
        "Bengali": "bn",
        "Marathi": "mr",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Punjabi": "pa",
        "Gujarati": "gu",
        "Urdu": "ur"
    }

# Test
if __name__ == "__main__":
    msg = "Please submit your report by Friday"
    
    hindi = translate_to_native(msg, "hi")
    print(f"Original : {msg}")
    print(f"Hindi    : {hindi}")
    
    back = translate_to_english(hindi, "hi")
    print(f"Back     : {back}")
    
    tamil = translate_to_native(msg, "ta")
    print(f"Tamil    : {tamil}")
    
    kannada = translate_to_native(msg, "kn")
    print(f"Kannada  : {kannada}")