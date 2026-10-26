# 🌟 Un cielo para Kiara

Página de cumpleaños hecha con Streamlit, con el tema de un cielo de estrellas.

## ✨ Qué tiene

| # | Sección | Qué pasa |
|---|---------|----------|
| 1 | **Inicio** | Pantalla negra, las frases se escriben solas y aparece una estrella. Al tocarla hay una explosión de luz, se enciende el cielo y empieza la música. |
| 2 | **Su nombre en constelación** | Las estrellas dibujan "Kiara" una por una, y aparece cuántas vueltas al sol cumple. |
| 3 | **Lejos, pero juntas** | Un mapa con un corazón que viaja entre las dos ciudades, los km que las separan y números como los días de amistad. |
| 4 | **Nuestra historia** | Línea del tiempo con fotos estilo polaroid que se ilumina mientras bajas. |
| 5 | **Cielo de mensajes** | Una estrella por amigo. Cada una abre su carta, foto o video, y al abrirlas todas se desbloquea un mensaje secreto. |
| 6 | **Banda sonora** | Sus canciones de Spotify, cada una con el "por qué". |
| 7 | **Razones por las que te quiero** | Cada estrella fugaz trae una razón. |
| 8 | **El pastel** | Sopla al micrófono (o toca las velas) para apagarlas. Sale confeti y "¡Pide un deseo!". |
| 9 | **La carta** | Un sobre con sello que se abre, y la carta aparece párrafo por párrafo. |
| 10 | **Final** | "Te quiero hasta las estrellas y de regreso", con lluvia de estrellas. |

## ✏️ Cómo poner tus cosas

1. Abre **`contenido.py`** y cambia los textos (todo está explicado ahí).
2. Pon las fotos en `static/fotos/`, los videos cortos en `static/videos/` y la canción de fondo (.mp3) en `static/musica/`.
3. En `contenido.py` escribe el nombre del archivo, por ejemplo `"foto": "fotos/viaje.jpg"`.
4. Para los videos de los amigos lo más fácil es subirlos a **YouTube como "No listado"** o a **Google Drive con acceso "cualquiera con el enlace"**, y pegar el link.
5. Para Spotify: en la canción, *Compartir → Copiar enlace*, y pégalo en `"spotify": "..."`.

## 💻 Verla en tu compu

```bash
pip install -r requirements.txt
streamlit run app.py
```

Trucos con el link:
- `?ver`: la ves antes del cumple, aunque esté activa la cuenta regresiva.
- `?directo`: se salta la intro.

## 🚀 Publicarla gratis

**Opción A: Streamlit Community Cloud (la más fácil)**
1. Entra a https://share.streamlit.io con tu cuenta de GitHub.
2. *Create app* → elige este repositorio, la rama y el archivo `app.py`.
3. Deploy. Te da un link tipo `kiara.streamlit.app` para mandárselo.

**Opción B: Render**
1. Entra a https://render.com → *New* → *Blueprint* → elige este repositorio (usa `render.yaml`).
2. Si lo haces a mano: *Web Service*, Build `pip install -r requirements.txt` y Start `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`.

> 💡 En el plan gratis de Render la página "se duerme" y tarda unos 30 segundos en despertar. Ábrela tú un ratito antes de mandarle el link.
