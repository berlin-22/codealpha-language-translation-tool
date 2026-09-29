# Language Translation Tool — CodeAlpha AI Internship

A clean, modern, real-time multi-language translation web application built with **Streamlit** and **translatepy**. Features a dual-pane workspace, automatic source language detection, and Text-to-Speech (TTS) capabilities.

![Python](https://img.shields.io/badge/Python-3.9+-18181b?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-18181b?logo=streamlit)

---

## Features

- **Dual-Pane Interface**: Side-by-side DeepL-inspired layout for seamless input and translation.
- **Auto Language Detection**: Automatically detects input languages (e.g. English, French, Spanish, Tamil, etc.).
- **30+ Supported Languages**: Wide coverage across global and regional languages.
- **Language & Text Swap**: One-click swap between source and target languages.
- **Text-to-Speech (TTS)**: Listen to translated speech with native pronunciation.
- **One-Click Copy & Clear**: Clean utilities for copying translation results and clearing panels.
- **Minimalist Design**: Neutral, high-contrast, clean UI with zero clutter.

---

## Tech Stack

| Component | Technology |
|---|---|
| **Frontend** | Streamlit |
| **Translation Engine** | translatepy (multi-provider neural translation) |
| **Text-to-Speech** | gTTS (Google Text-to-Speech) |
| **Language** | Python 3.9+ |

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/berlin-22/codealpha-language-translation-tool.git
   cd codealpha-language-translation-tool
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application**
   ```bash
   streamlit run app.py
   ```

5. Open `http://localhost:8501` in your browser.

---

## Project Structure

```
CodeAlpha_LanguageTranslationTool/
├── .streamlit/
│   └── config.toml     # Minimalist theme configuration
├── app.py              # Streamlit application & UI
├── translator.py       # Translation logic & auto-detection
├── tts.py              # Text-to-Speech audio generation
├── languages.py        # Language mappings & ISO codes
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Documentation
```

---

## Acknowledgements

Built for the **CodeAlpha Artificial Intelligence Internship** (Task 1).
