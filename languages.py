# Supported languages mapping: Display Name -> ISO 639-1 Code
LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Arabic": "ar",
    "Hindi": "hi",
    "Bengali": "bn",
    "Urdu": "ur",
    "Tamil": "ta",
    "Telugu": "te",
    "Turkish": "tr",
    "Dutch": "nl",
    "Polish": "pl",
    "Swedish": "sv",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Malay": "ms",
    "Greek": "el",
    "Hebrew": "he",
    "Czech": "cs",
    "Romanian": "ro",
    "Ukrainian": "uk",
}

# Target languages (exclude "Auto Detect")
TARGET_LANGUAGES = {k: v for k, v in LANGUAGES.items() if v != "auto"}

# Reverse lookup: code -> name
CODE_TO_NAME = {v: k for k, v in LANGUAGES.items()}
