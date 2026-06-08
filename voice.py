import whisper
import tempfile
import os
from gtts import gTTS


def transcribe_audio(audio_bytes):
    try:
        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as tmp_file:
            tmp_file.write(audio_bytes)
            tmp_path = tmp_file.name

        model = whisper.load_model("base")
        result = model.transcribe(tmp_path)
        os.unlink(tmp_path)

        return result["text"].strip()

    except Exception as e:
        return f"Transcription error: {str(e)}"


def text_to_speech(text, lang_code="hi"):
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tmp_path = tempfile.mktemp(suffix=".mp3")
        tts.save(tmp_path)
        return tmp_path
    except Exception as e:
        return None