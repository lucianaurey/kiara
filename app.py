"""Página de cumpleaños para Kiara 🌟

Correr en tu compu:   streamlit run app.py
Todo el contenido se edita en  contenido.py
"""

import base64
import copy
import io
import json
import mimetypes
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageOps

from contenido import DATOS

RAIZ = Path(__file__).parent
STATIC = RAIZ / "static"
FORMATOS_FOTO = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

st.set_page_config(
    page_title=f"Feliz cumpleaños, {DATOS['nombre']} ✨",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Oculta todo lo de Streamlit para que la experiencia ocupe la pantalla completa
st.markdown(
    """
    <style>
      header, footer, #MainMenu,
      [data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }
      html, body, .stApp, [data-testid="stAppViewContainer"] { background: #060716 !important; }
      [data-testid="stMain"], section.main { overflow: hidden !important; }
      .block-container, [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      [data-testid="stElementContainer"]:has(> .stMarkdown) { display: none !important; }
      iframe { display: block; width: 100%; height: 100vh !important; height: 100dvh !important; border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def foto_a_base64(ruta: str, modificado: float) -> str:
    """Achica la foto y la incrusta en la página (así carga rápido en el celular)."""
    img = ImageOps.exif_transpose(Image.open(STATIC / ruta))
    img.thumbnail((1400, 1400))
    if img.mode not in ("RGB", "L"):
        fondo = Image.new("RGB", img.size, (255, 255, 255))
        fondo.paste(img, mask=img.convert("RGBA").split()[-1])
        img = fondo
    buf = io.BytesIO()
    img.convert("RGB").save(buf, "JPEG", quality=82, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def archivo(ruta: str) -> str:
    """Convierte 'fotos/x.jpg' en algo que el navegador pueda mostrar."""
    if not ruta or ruta.startswith(("http://", "https://", "data:")):
        return ruta
    ruta = ruta.lstrip("/").removeprefix("static/")
    real = STATIC / ruta
    if not real.is_file():
        st.toast(f"No encontré el archivo static/{ruta} 👀")
        return ""
    if real.suffix.lower() in FORMATOS_FOTO:
        return foto_a_base64(ruta, real.stat().st_mtime)
    # Videos y música: los sirve Streamlit desde la carpeta static/
    tipo = mimetypes.guess_type(real.name)[0] or ""
    if real.stat().st_size < 8 * 1024 * 1024 and tipo.startswith("audio"):
        return f"data:{tipo};base64," + base64.b64encode(real.read_bytes()).decode()
    return f"/app/static/{ruta}"


def preparar_datos() -> dict:
    datos = copy.deepcopy(DATOS)
    datos["musica_fondo"] = archivo(datos.get("musica_fondo", ""))
    for hito in datos.get("historia", []):
        hito["foto"] = archivo(hito.get("foto", ""))
    for msg in datos.get("mensajes", []):
        msg["foto"] = archivo(msg.get("foto", ""))
        msg["video"] = archivo(msg.get("video", ""))
    # ?ver = ver la página antes del cumple · ?directo = saltar la intro
    datos["_ver"] = "ver" in st.query_params
    datos["_directo"] = "directo" in st.query_params
    return datos


plantilla = (RAIZ / "plantilla.html").read_text(encoding="utf-8")
json_datos = json.dumps(preparar_datos(), ensure_ascii=False).replace("</", "<\\/")
components.html(plantilla.replace("/*__DATOS__*/null", json_datos), height=900, scrolling=True)
