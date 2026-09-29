from io import BytesIO
from gtts import gTTS


def generate_audio(text: str, lang: str = "en") -> bytes | None:
    """
    Generate Text-to-Speech audio from text.

    Args:
        text: The text to convert to speech.
        lang: Language code for TTS.

    Returns:
        Audio bytes (MP3) or None on failure.
    """
    if not text or not text.strip():
        return None

    try:
        # Some language codes need mapping for gTTS
        tts_lang_map = {
            "zh-CN": "zh-cn",
            "zh-TW": "zh-tw",
        }
        tts_lang = tts_lang_map.get(lang, lang)

        # gTTS doesn't support all languages — fallback to English
        tts = gTTS(text=text, lang=tts_lang, slow=False)
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer.read()

    except Exception:
        return None
