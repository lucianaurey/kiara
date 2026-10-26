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
    "fecha_cumple": "2026-11-06",
    # Su fecha de nacimiento, para calcular sus "vueltas al sol" ("" si no quieres)
    "nacimiento": "2006-11-06",
    # Cómo se escribe su edad en la nota a mano ("feliz cumple veinte, mi vida")
    "edad_en_letras": "veinte",
    # Desde cuándo son amigas. Pon una fecha (AAAA-MM-DD) para contar los días,
    # o déjala "" y se muestra el texto de "amigas_desde".
    "inicio_amistad": "",
    "amigas_desde": "5.º de primaria",

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
        "tu": {"ciudad": "Cochabamba", "lat": -17.3895, "lon": -66.1568},
        "ella": {"ciudad": "Aguascalientes", "lat": 21.8853, "lon": -102.2916},
    },
    # (Busca "coordenadas de <ciudad>" en Google para sacar lat y lon)

    # ---------- 3. Nuestra historia (un libro que pasa páginas) ----------
    # Cada capítulo ocupa dos páginas: el texto y su foto.
    # Lo que está entre [corchetes] cámbialo por tus recuerdos reales.
    "historia": [
        {
            "titulo": "Segundo de primaria",
            "texto": "Yo tenía ocho años la primera vez que te vi. Todavía no sabía que esa niña iba a convertirse en mi persona favorita del universo.",
            "nota": "¿te acuerdas de [ese día]?",
            "foto": "",  # ej: "fotos/primaria.jpg"
            "pie": "las dos, chiquitas",
        },
        {
            "titulo": "Quinto de primaria",
            "texto": "Ahí empezó todo de verdad. Un día dejaste de ser la niña de mi salón y te volviste mi amiga.",
            "nota": "[nuestro primer recuerdo juntas]",
            "foto": "",
            "pie": "aquí empezamos",
        },
        {
            "titulo": "Primero de secundaria",
            "texto": "Desde ese año fuimos inseparables: los recreos, los secretos y las risas que nadie más entendía.",
            "nota": "[el chiste que solo es nuestro]",
            "foto": "",
            "pie": "inseparables",
        },
        {
            "titulo": "5 878 kilómetros",
            "texto": "Ahora tú estás en Aguascalientes y yo en Cochabamba. Cambió el mapa, pero no cambió nada de lo importante.",
            "nota": "y seguimos mirando el mismo cielo",
            "foto": "",
            "pie": "lejos, pero juntas",
            "coordenadas": True,  # muestra las coordenadas de las dos ciudades
        },
        {
            "titulo": "Veinte",
            "texto": "Hoy cumples veinte años. Veinte vueltas al sol, y yo tuve la suerte de acompañarte en más de la mitad.",
            "nota": "cierra los ojos y pide un deseo",
            "foto": "",
            "pie": "feliz cumple, mi vida",
        },
    ],

    # ---------- 4. El cielo de mensajes (una estrella por amigo) ----------
    # video: link de YouTube / Google Drive, o "videos/archivo.mp4"
    "mensajes": [
        {"de": "Mamá de Kiara", "desde": "Casa", "texto": "Mi niña hermosa, feliz cumpleaños. Te extrañamos cada día.", "foto": "", "video": ""},
        {"de": "Amigo 1", "desde": "Cochabamba", "texto": "¡Feliz cumple, Kiara! Aquí te seguimos esperando para la próxima fiesta.", "foto": "", "video": ""},
        {"de": "Amiga 2", "desde": "Cusco", "texto": "Eres de las personas más lindas que conozco. Que este año te dé todo lo que mereces.", "foto": "", "video": ""},
        {"de": "Amigo 3", "desde": "Buenos Aires", "texto": "Feliz vuelta al sol 🌞 ¡Un abrazo enorme desde aquí!", "foto": "", "video": ""},
        {"de": "Amiga 4", "desde": "Bogotá", "texto": "Gracias por siempre escucharme. Te quiero muchísimo.", "foto": "", "video": ""},
        {"de": "Amigo 5", "desde": "Aguascalientes", "texto": "¡Que vivan los 20! Hoy invito yo el café ☕", "foto": "", "video": ""},
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
    "velas": "20",  # las velas forman este número
    "deseo": "Ojalá este año te traiga todo lo que sueñas... y un pasaje para volver a vernos pronto ✈️",

    # ---------- 8. La carta final ----------
    "carta": """Querida Kiara:

Hoy es tu día, y aunque no pueda darte un abrazo en persona, quería regalarte un pedacito de cielo hecho con todo lo que siento por ti.

Gracias por cada risa, cada consejo, cada llamada a deshoras y por quedarte, aunque estemos lejos.

Desde segundo de primaria hasta hoy, eres mi mejor amiga, mi hermana elegida, mi todo.

Feliz cumpleaños. Te quiero infinito.""",

    # Frase final gigante
    "final": "Te quiero hasta las estrellas y de regreso",
    # Frase que va debajo, como firmada a mano
    "final_firma": "always under the same sky",
}
