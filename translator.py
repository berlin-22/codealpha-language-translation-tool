from translatepy import Translator

# Single translator instance — auto-rotates between services
# (Google, Bing, Yandex, Reverso, DeepL, etc.)
_translator = Translator()


def translate_text(text: str, source: str, target: str) -> dict:
    """
    Translate text from source language to target language.
    Uses translatepy which aggregates multiple free translation services.

    Args:
        text: The text to translate.
        source: Source language ISO code (or 'auto' for auto-detect).
        target: Target language ISO code.

    Returns:
        dict with keys: 'translated_text', 'source_lang', 'success', 'error'
    """
    if not text or not text.strip():
        return {
            "translated_text": "",
            "source_lang": source,
            "success": False,
            "error": "Please enter some text to translate.",
        }

    if source == target and source != "auto":
        return {
            "translated_text": text,
            "source_lang": source,
            "success": True,
            "error": None,
        }

    try:
        # Handle long text by chunking
        max_chunk = 4500

        if len(text) > max_chunk:
            chunks = []
            for i in range(0, len(text), max_chunk):
                chunk = text[i : i + max_chunk]
                if source == "auto":
                    result = _translator.translate(chunk, target)
                else:
                    result = _translator.translate(chunk, target, source)
                chunks.append(str(result))
            translated = " ".join(chunks)
        else:
            if source == "auto":
                result = _translator.translate(text, target)
            else:
                result = _translator.translate(text, target, source)
            translated = str(result)

        detected = None
        if hasattr(result, "source_language") and result.source_language:
            detected = getattr(result.source_language, "name", str(result.source_language))

        return {
            "translated_text": translated,
            "source_lang": source,
            "detected_lang": detected,
            "success": True,
            "error": None,
        }

    except Exception as e:
        return {
            "translated_text": "",
            "source_lang": source,
            "success": False,
            "error": f"Translation failed: {str(e)}",
        }
