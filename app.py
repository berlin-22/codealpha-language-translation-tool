import streamlit as st
from translator import translate_text
from tts import generate_audio
from languages import LANGUAGES, TARGET_LANGUAGES

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Translator",
    page_icon="⇄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS: Modern Clean Minimalist Design (Strictly Zero Blue) ───────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Global Reset & Typography */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    color: #18181b !important;
}

/* App Background: Clean Neutral Off-White (Strictly Zero Blue) */
.stApp {
    background-color: #f7f7f8 !important;
}

/* Hide Default Streamlit Chrome */
#MainMenu, header, footer, .stDeployButton {
    display: none !important;
}

/* Constrain Container Width for Clean Pro Layout */
.main .block-container {
    max-width: 1040px !important;
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
}

/* Top Brand Navigation */
.brand-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 1.25rem;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid #e4e4e7;
}
.brand-title-wrap {
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
}
.brand-title {
    font-size: 1.35rem;
    font-weight: 600;
    color: #18181b;
    letter-spacing: -0.025em;
    margin: 0;
}
.brand-subtitle {
    font-size: 0.82rem;
    color: #71717a;
    margin: 0;
}
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    font-size: 0.75rem;
    font-weight: 500;
    color: #52525b;
    background: #ffffff;
    border: 1px solid #e4e4e7;
    padding: 0.3rem 0.75rem;
    border-radius: 9999px;
}
.status-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: #10b981;
}

/* Panel Header Meta */
.panel-meta-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.6rem;
    min-height: 1.5rem;
}
.panel-heading {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #71717a;
}
.detected-pill {
    font-size: 0.72rem;
    font-weight: 500;
    color: #27272a;
    background-color: #f4f4f5;
    border: 1px solid #e4e4e7;
    padding: 2px 8px;
    border-radius: 4px;
}

/* Container Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    border: 1px solid #e4e4e7 !important;
    border-radius: 12px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03), 0 1px 2px rgba(0, 0, 0, 0.02) !important;
    padding: 1.25rem !important;
}

/* Input Textarea */
div[data-testid="stTextArea"] textarea {
    background: #ffffff !important;
    border: 1px solid #e4e4e7 !important;
    border-radius: 8px !important;
    color: #18181b !important;
    font-size: 0.95rem !important;
    line-height: 1.6 !important;
    padding: 0.85rem !important;
    box-shadow: none !important;
    transition: border-color 0.15s ease !important;
}
div[data-testid="stTextArea"] textarea:focus {
    border-color: #18181b !important;
    box-shadow: 0 0 0 1px #18181b !important;
}

/* Selectbox */
div[data-testid="stSelectbox"] > div > div {
    background: #ffffff !important;
    border: 1px solid #e4e4e7 !important;
    border-radius: 8px !important;
    color: #18181b !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    box-shadow: none !important;
    min-height: 42px !important;
}
div[data-testid="stSelectbox"] > div > div:hover,
div[data-testid="stSelectbox"] > div > div:focus-within {
    border-color: #18181b !important;
}
div[data-testid="stSelectbox"] label {
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.04em !important;
    color: #71717a !important;
    margin-bottom: 0.35rem !important;
}

/* Output Display Box */
.output-pane {
    background: #fafafa;
    border: 1px solid #e4e4e7;
    border-radius: 8px;
    padding: 0.85rem 1rem;
    min-height: 200px;
    max-height: 380px;
    overflow-y: auto;
    font-size: 0.95rem;
    line-height: 1.65;
    color: #18181b;
    word-break: break-word;
    white-space: pre-wrap;
}
.output-placeholder {
    color: #a1a1aa;
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    min-height: 180px;
    user-select: none;
}

/* Primary Action Button (Obsidian Charcoal - Strictly No Blue) */
button[data-testid="stBaseButton-primary"] {
    background-color: #18181b !important;
    color: #ffffff !important;
    border: 1px solid #18181b !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
    letter-spacing: 0.01em !important;
    padding: 0.55rem 1.25rem !important;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
    transition: all 0.15s ease !important;
}
button[data-testid="stBaseButton-primary"]:hover {
    background-color: #27272a !important;
    border-color: #27272a !important;
    color: #ffffff !important;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08) !important;
}
button[data-testid="stBaseButton-primary"]:active {
    background-color: #09090b !important;
}

/* Secondary Buttons */
button[data-testid="stBaseButton-secondary"] {
    background-color: #ffffff !important;
    color: #3f3f46 !important;
    border: 1px solid #e4e4e7 !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
    font-size: 0.82rem !important;
    padding: 0.45rem 0.9rem !important;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02) !important;
    transition: all 0.15s ease !important;
}
button[data-testid="stBaseButton-secondary"]:hover {
    background-color: #f4f4f5 !important;
    border-color: #d4d4d8 !important;
    color: #18181b !important;
}

/* Code block clean styling */
div[data-testid="stCodeBlock"] {
    border: 1px solid #e4e4e7 !important;
    border-radius: 8px !important;
    background: #f4f4f5 !important;
    margin-top: 0.75rem !important;
}

/* Meta info */
.meta-char-count {
    font-size: 0.78rem;
    color: #a1a1aa;
    text-align: right;
    line-height: 2.2;
}

/* Footer */
.app-footer {
    margin-top: 3rem;
    padding-top: 1.25rem;
    border-top: 1px solid #e4e4e7;
    text-align: center;
    font-size: 0.78rem;
    color: #a1a1aa;
}
</style>
""", unsafe_allow_html=True)

# ── Session State Initialization ─────────────────────────────────────────────
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""
if "detected_lang" not in st.session_state:
    st.session_state.detected_lang = None
if "source_lang_key" not in st.session_state:
    st.session_state.source_lang_key = "English"
if "target_lang_key" not in st.session_state:
    st.session_state.target_lang_key = "Hindi"
if "audio_bytes" not in st.session_state:
    st.session_state.audio_bytes = None
if "show_copy_code" not in st.session_state:
    st.session_state.show_copy_code = False

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="brand-nav">
    <div class="brand-title-wrap">
        <h1 class="brand-title">Translator</h1>
        <p class="brand-subtitle">Fast, accurate multi-language neural translation</p>
    </div>
    <div class="status-pill">
        <span class="status-dot"></span>
        <span>Neural Engine Online</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Language Selectors & Swap Bar ────────────────────────────────────────────
source_names = list(LANGUAGES.keys())
target_names = list(TARGET_LANGUAGES.keys())

def format_lang_label(name: str) -> str:
    code = LANGUAGES.get(name, "")
    if name == "Auto Detect":
        return "Auto Detect"
    return f"{name} ({code.upper()})"

col_src, col_swap, col_tgt = st.columns([5, 1, 5], gap="small")

with col_src:
    current_src_index = source_names.index(st.session_state.source_lang_key) if st.session_state.source_lang_key in source_names else 1
    selected_source = st.selectbox(
        "Source Language",
        source_names,
        index=current_src_index,
        key="source_select",
        format_func=format_lang_label,
    )
    st.session_state.source_lang_key = selected_source

with col_swap:
    st.markdown("<div style='height: 1.7rem;'></div>", unsafe_allow_html=True)
    if st.button("⇄", help="Swap source and target languages", use_container_width=True, key="swap_btn"):
        if selected_source == "Auto Detect":
            st.toast("Select a specific source language to swap.")
        else:
            old_src = st.session_state.source_lang_key
            old_tgt = st.session_state.target_lang_key
            st.session_state.source_lang_key = old_tgt
            st.session_state.target_lang_key = old_src
            # Swap content if translation exists
            if st.session_state.translated_text:
                current_input = st.session_state.get("input_text", "")
                st.session_state.input_text = st.session_state.translated_text
                st.session_state.translated_text = current_input
            st.rerun()

with col_tgt:
    current_tgt_index = target_names.index(st.session_state.target_lang_key) if st.session_state.target_lang_key in target_names else 0
    selected_target = st.selectbox(
        "Target Language",
        target_names,
        index=current_tgt_index,
        key="target_select",
        format_func=format_lang_label,
    )
    st.session_state.target_lang_key = selected_target

st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)

# ── Dual-Pane Workspace ──────────────────────────────────────────────────────
col_input_card, col_output_card = st.columns(2, gap="medium")

# ── Left Pane: Input ─────────────────────────────────────────────────────────
with col_input_card:
    with st.container(border=True):
        st.markdown("""
        <div class="panel-meta-bar">
            <span class="panel-heading">Source Text</span>
        </div>
        """, unsafe_allow_html=True)

        input_text = st.text_area(
            "Source Text",
            placeholder="Type or paste text to translate...",
            height=200,
            max_chars=5000,
            key="input_text",
            label_visibility="collapsed",
        )

        char_count = len(input_text) if input_text else 0

        # Toolbar below input
        tb_col1, tb_col2, tb_col3 = st.columns([2, 1, 2], gap="small")
        with tb_col1:
            st.markdown(f'<div class="meta-char-count">{char_count:,} / 5,000</div>', unsafe_allow_html=True)
        with tb_col2:
            if st.button("Clear", key="clear_input_btn", use_container_width=True):
                st.session_state.input_text = ""
                st.session_state.translated_text = ""
                st.session_state.audio_bytes = None
                st.session_state.detected_lang = None
                st.session_state.show_copy_code = False
                st.rerun()
        with tb_col3:
            translate_clicked = st.button("Translate", type="primary", use_container_width=True, key="do_translate_btn")

# ── Process Translation Immediate Execution ─────────────────────────────────
if translate_clicked:
    if not input_text or not input_text.strip():
        st.toast("Please enter text to translate.")
    else:
        src_code = LANGUAGES[selected_source]
        tgt_code = TARGET_LANGUAGES[selected_target]

        with st.spinner("Translating..."):
            result = translate_text(input_text, src_code, tgt_code)

        if result["success"]:
            st.session_state.translated_text = result["translated_text"]
            st.session_state.detected_lang = result.get("detected_lang")
            st.session_state.audio_bytes = None
            st.session_state.show_copy_code = False
        else:
            st.toast(result["error"])

# ── Right Pane: Output ────────────────────────────────────────────────────────
with col_output_card:
    with st.container(border=True):
        detected_tag_html = ""
        if st.session_state.detected_lang and st.session_state.source_lang_key == "Auto Detect":
            detected_tag_html = f'<span class="detected-pill">Detected: {st.session_state.detected_lang}</span>'

        st.markdown(f"""
        <div class="panel-meta-bar">
            <span class="panel-heading">Translation</span>
            {detected_tag_html}
        </div>
        """, unsafe_allow_html=True)

        if st.session_state.translated_text:
            st.markdown(
                f'<div class="output-pane">{st.session_state.translated_text}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="output-pane"><div class="output-placeholder">Translation will appear here</div></div>',
                unsafe_allow_html=True,
            )

        # Action bar below output
        act_col1, act_col2, act_col3 = st.columns(3, gap="small")
        with act_col1:
            listen_clicked = st.button(
                "Listen",
                use_container_width=True,
                key="listen_btn",
                disabled=not bool(st.session_state.translated_text),
            )
        with act_col2:
            copy_clicked = st.button(
                "Copy",
                use_container_width=True,
                key="copy_btn",
                disabled=not bool(st.session_state.translated_text),
            )
        with act_col3:
            clear_out_clicked = st.button(
                "Clear",
                use_container_width=True,
                key="clear_out_btn",
                disabled=not bool(st.session_state.translated_text),
            )

        if clear_out_clicked:
            st.session_state.translated_text = ""
            st.session_state.audio_bytes = None
            st.session_state.detected_lang = None
            st.session_state.show_copy_code = False
            st.rerun()

        if copy_clicked:
            st.session_state.show_copy_code = True
            st.toast("Ready to copy from snippet box below")

        if st.session_state.show_copy_code and st.session_state.translated_text:
            st.code(st.session_state.translated_text, language=None)

        if listen_clicked and st.session_state.translated_text:
            tgt_code = TARGET_LANGUAGES[st.session_state.target_lang_key]
            with st.spinner("Generating speech..."):
                audio = generate_audio(st.session_state.translated_text, tgt_code)
            if audio:
                st.session_state.audio_bytes = audio
                st.rerun()
            else:
                st.toast(f"Speech audio not supported for {st.session_state.target_lang_key}")

        if st.session_state.audio_bytes:
            st.markdown("<div style='margin-top: 0.75rem;'></div>", unsafe_allow_html=True)
            st.audio(st.session_state.audio_bytes, format="audio/mp3")

# ── Understated Clean Footer ─────────────────────────────────────────────────
st.markdown("""
<div class="app-footer">
    Powered by neural translation engine • 31 languages supported
</div>
""", unsafe_allow_html=True)
