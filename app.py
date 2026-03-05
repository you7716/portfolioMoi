from pathlib import Path

import streamlit as st
from streamlit.components.v1 import html as st_html


st.set_page_config(
    page_title="Portfolio - Youssouph Sagna",
    page_icon="💼",
    layout="wide",
)

index_path = Path("index.html")

if not index_path.exists():
    st.error("Le fichier index.html est introuvable dans le dossier de l'application.")
else:
    html_content = index_path.read_text(encoding="utf-8")
    # Affiche le portfolio complet dans un composant HTML
    st_html(html_content, height=1000, scrolling=True)

