# =====================================================================
#  🌟  AQUÍ EDITAS TODO EL CONTENIDO DE LA PÁGINA DE KIARA  🌟
# ---------------------------------------------------------------------
#  - Cambia los textos entre comillas "..." por los tuyos.
#  - Las fotos, videos y música van dentro de la carpeta  static/
#      static/fotos/   -> fotos  (.jpg, .png, .webp)
#      static/videos/  -> videos cortos (.mp4)  (para videos largos usa YouTube)
#      static/musica/  -> canción de fondo (.mp3)
#    y aquí solo escribes el nombre:  "fotos/primera-foto.jpg"
#  - Para videos también puedes pegar un link de YouTube o de Google Drive.
#  - Si dejas algo vacío "" esa parte simplemente no se muestra
#    (o aparece un recuadro de ejemplo para que sepas dónde va).
# =====================================================================

DATOS = {
    # ---------- Lo básico ----------
    "nombre": "Kiara",
    "tu_nombre": "Tu mejor amiga",  # 👈 pon tu nombre
    # Fecha del cumple (AAAA-MM-DD). Antes de ese día la página muestra
    # una cuenta regresiva. Déjalo "" para que se abra siempre.
    # (Tú puedes verla antes entrando con  ?ver  al final del link)
    "fecha_cumple": "",
    # Su fecha de nacimiento, para calcular sus "vueltas al sol" ("" si no quieres)
    "nacimiento": "2004-11-15",
    # Desde cuándo son amigas (para contar los días de amistad)
    "inicio_amistad": "2015-03-01",

    # Canción de fondo que suena al tocar la estrella (archivo .mp3 en static/musica/)
    # Spotify no deja reproducir de fondo, por eso esta va como archivo.
    "musica_fondo": "",

    # ---------- 1. El inicio ----------
    # Frases que aparecen escribiéndose una por una en la pantalla negra
    "intro": [
        "Kiara...",
        "hace muchos años, el universo hizo algo increíble.",
        "encendió una estrella que brilla más que todas las demás.",
        "y yo tuve la suerte de encontrarla.",
    ],

    # ---------- 2. La distancia ----------
    "ubicaciones": {
        "tu": {"ciudad": "Lima", "lat": -12.0464, "lon": -77.0428},       # 👈 tu ciudad
        "ella": {"ciudad": "Madrid", "lat": 40.4168, "lon": -3.7038},     # 👈 su ciudad
    },
    # (Busca "coordenadas de <ciudad>" en Google para sacar lat y lon)

    # ---------- 3. Nuestra historia ----------
    "historia": [
        {
            "fecha": "2015",
            "titulo": "El día que nos conocimos",
            "texto": "Nadie sabía que ese día empezaba la amistad más bonita de mi vida.",
            "foto": "",  # ej: "fotos/2015.jpg"
        },
        {
            "fecha": "2017",
            "titulo": "Nuestro primer viaje juntas",
            "texto": "Nos perdimos, nos reímos hasta llorar y prometimos repetirlo mil veces.",
            "foto": "",
        },
        {
            "fecha": "2019",
            "titulo": "Ese chiste que solo entendemos nosotras",
            "texto": "Hasta hoy no puedo escucharlo sin acordarme de ti.",
            "foto": "",
        },
        {
            "fecha": "2022",
            "titulo": "El día que te fuiste lejos",
            "texto": "Lloré en el aeropuerto, pero aprendí que la distancia no cambia nada de lo importante.",
            "foto": "",
        },
        {
            "fecha": "Hoy",
            "titulo": "Y aquí seguimos",
            "texto": "Miles de kilómetros, mil videollamadas y el mismo cariño de siempre.",
            "foto": "",
        },
    ],

    # ---------- 4. El cielo de mensajes (una estrella por amigo) ----------
    # video: link de YouTube / Google Drive, o "videos/archivo.mp4"
    "mensajes": [
        {"de": "Mamá de Kiara", "desde": "Casa", "texto": "Mi niña hermosa, feliz cumpleaños. Te extrañamos cada día.", "foto": "", "video": ""},
        {"de": "Amigo 1", "desde": "Lima", "texto": "¡Feliz cumple, Kiara! Aquí te seguimos esperando para la próxima fiesta.", "foto": "", "video": ""},
        {"de": "Amiga 2", "desde": "Cusco", "texto": "Eres de las personas más lindas que conozco. Que este año te dé todo lo que mereces.", "foto": "", "video": ""},
        {"de": "Amigo 3", "desde": "Buenos Aires", "texto": "Feliz vuelta al sol 🌞 ¡Un abrazo enorme desde aquí!", "foto": "", "video": ""},
        {"de": "Amiga 4", "desde": "Bogotá", "texto": "Gracias por siempre escucharme. Te quiero muchísimo.", "foto": "", "video": ""},
        {"de": "Amigo 5", "desde": "Madrid", "texto": "¡Que vivan los 22! Hoy invito yo el café ☕", "foto": "", "video": ""},
    ],
    # Mensaje que se desbloquea cuando abre TODAS las estrellas
    "mensaje_secreto": "Abriste todas las estrellas ✨ Todas estas personas te quieren, y yo más que nadie.",

    # ---------- 5. Nuestra banda sonora (Spotify) ----------
    # En Spotify: canción → Compartir → Copiar enlace, y pégalo aquí
    "playlist": "",  # ej: "https://open.spotify.com/playlist/xxxxxxxx"
    "canciones": [
        {"titulo": "Nuestra canción", "spotify": "", "porque": "La que cantamos a gritos cada vez que suena."},
        {"titulo": "La del viaje", "spotify": "", "porque": "Sonó todo el camino, una y otra vez."},
        {"titulo": "La que me recuerda a ti", "spotify": "", "porque": "Cada vez que la escucho, siento que estás aquí."},
    ],

    # ---------- 6. Razones por las que te quiero (estrellas fugaces) ----------
    "razones": [
        "Porque te ríes de mis chistes aunque sean malísimos.",
        "Porque contigo puedo ser 100% yo.",
        "Porque siempre sabes qué decir cuando todo va mal.",
        "Porque la distancia nunca pudo con nosotras.",
        "Porque tus audios de 7 minutos me alegran el día.",
        "Porque eres valiente, aunque a veces no lo creas.",
        "Porque eres mi persona favorita en todo el universo.",
    ],

    # ---------- 7. El pastel ----------
    "velas": 5,  # cuántas velas tiene el pastel (máximo 10)
    "deseo": "Ojalá este año te traiga todo lo que sueñas... y un pasaje para volver a vernos pronto ✈️",

    # ---------- 8. La carta final ----------
    "carta": """Querida Kiara:

Hoy es tu día, y aunque no pueda darte un abrazo en persona, quería regalarte un pedacito de cielo hecho con todo lo que siento por ti.

Gracias por cada risa, cada consejo, cada llamada a deshoras y por quedarte, aunque estemos lejos.

Eres mi mejor amiga, mi hermana elegida, mi todo.

Feliz cumpleaños. Te quiero infinito.""",

    # Frase final gigante
    "final": "Te quiero hasta las estrellas y de regreso",
}
