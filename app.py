from pathlib import Path
import base64

import streamlit as st
from streamlit.components.v1 import html as st_html


st.set_page_config(
    page_title="Portfolio - Youssouph Sagna",
    page_icon="💼",
    layout="wide",
)

index_path = Path("index.html")
image_path = Path("assets/profile.jpg")

if not index_path.exists():
    st.error("Le fichier index.html est introuvable dans le dossier de l'application.")
else:
    html_content = index_path.read_text(encoding="utf-8")

    # Intègre la photo de profil directement en base64 pour que Streamlit l'affiche correctement
    if image_path.exists():
        encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
        data_url = f"data:image/jpeg;base64,{encoded}"
        html_content = html_content.replace("assets/profile.jpg", data_url)

    # Affiche le portfolio complet dans un composant HTML
    st_html(html_content, height=1000, scrolling=True)

