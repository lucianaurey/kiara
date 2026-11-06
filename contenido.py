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
    "tu_nombre": "Lu",  # 👈 tu nombre (así firma la página)
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
    "amigas_desde": "abril de 2014",
    # Si lo llenas, reemplaza "amigas desde" por un contador de aventuras
    "aventuras": "+1000",

    # Canción de fondo que suena al tocar la estrella.
    # Va con Spotify: si Kiara tiene la sesión de Spotify abierta en su navegador
    # suena completa; si no, Spotify solo deja escuchar una vista previa de 30 s.
    "spotify_fondo": "https://open.spotify.com/intl-es/track/6XXQA6e8qXPJ1sZtRxvbws",  # El Fin del Mundo
    # (Opcional) Si pones un .mp3 en static/musica/ y escribes aquí su nombre,
    # se usa el archivo en vez de Spotify, ej: "musica/el-fin-del-mundo.mp3"
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
    # Foto que va en la portada del libro, junto a la dedicatoria
    "portada": "fotos/portada.jpg",
    # Cada capítulo ocupa dos páginas: el texto y su foto.
    # Lo que está entre [corchetes] cámbialo por tus recuerdos reales.
    "historia": [
        {
            "titulo": "Los MUNs",
            "texto": "Nuestro amor a los MUNs: una de las cosas que más amo compartir contigo.",
            "nota": "pd: VIVA JAPONNN",
            "foto": "fotos/mun-2.jpg",
            "fotos": [
                "fotos/mun-1.jpg",
                "fotos/mun-2.jpg",
                "fotos/mun-3.jpg",
                "fotos/mun-4.jpg",
                "fotos/mun-5.jpg",
                "fotos/mun-6.jpg",
                "fotos/mun-7.jpg",
            ],
            "pie": "delegadas de excelencia",
        },
        {
            "titulo": "El Salar",
            "texto": "Nuestro viaje al Salar. Aunque no estaba planeado, terminaste siendo mi roomie y fuiste la mejor. El mejor viaje, a tu lado.",
            "nota": "narices rojas who",
            "foto": "fotos/salar-atardecer.jpg",
            # Con "fotos" (varias) la página de la foto se vuelve un collage
            "fotos": [
                "fotos/salar-atardecer.jpg",
                "fotos/salar-camara.jpg",
                "fotos/salar-narices-rojas.jpg",
                "fotos/salar-marvel.jpg",
            ],
            "pie": "la mejor roomie del mundo",
        },
        {
            "titulo": "Por más jodas a tu lado",
            "texto": "Por más jodas a tu lado.",
            "nota": "que viva el Bacardi mojito, el tequila Olmeca y el Four Loko",
            "foto": "fotos/jodas-2.jpg",
            "fotos": [
                "fotos/jodas-1.jpg",
                "fotos/jodas-2.jpg",
                "fotos/jodas-3.jpg",
                "fotos/jodas-4.jpg",
                "fotos/jodas-5.jpg",
                "fotos/jodas-6.jpg",
            ],
            # Videos (en static/videos/): salen chiquitos y se abren solo si los toca
            "videos": [
                "videos/jodas-1.mp4",
                "videos/jodas-2.mp4",
                "videos/jodas-3.mp4",
                "videos/jodas-4.mp4",
                "videos/jodas-5.mp4",
            ],
            "pie": "salud por nosotras",
        },
        {
            "titulo": "2024, nuestro año de promo",
            "texto": "Gracias a vos fue uno de los mejores años de mi vida. Tantas memorias a tu lado.",
            "nota": "y obvio, el mejor proyecto de BTH",
            "foto": "fotos/promo-3.jpg",
            # Las dos primeras salen debajo del texto: el abrazo de graduación y el proyecto de BTH
            "fotos": [f"fotos/promo-{n}.jpg" for n in (3, 8, 1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16)],
            "videos": ["videos/promo-1.mp4", "videos/promo-2.mp4"],
            "pie": "promo 2024, para siempre",
        },
        {
            "titulo": "Nuestras rides en auto",
            "texto": "Nuestras rides en auto: the best feeling ever.",
            "nota": "y no hay que olvidar nuestros primeros choques juntas",
            "foto": "fotos/rides-1.jpg",
            # La primera (el choque) sale debajo del texto, junto a la nota
            "fotos": [f"fotos/rides-{n}.jpg" for n in range(1, 6)],
            "videos": [f"videos/rides-{n}.mp4" for n in range(1, 6)],
            "pie": "copilotas para siempre",
        },
        {
            "titulo": "Veinte",
            "texto": "Hoy cumples veinte años. Veinte vueltas al sol, y yo tuve la suerte de acompañarte en más de la mitad. Y por cada momento que pasamos juntas le doy gracias a Dios y a la vida.",
            "nota": "",
            "foto": "fotos/veinte-9.jpg",
            # Las dos primeras salen debajo del texto: el balcón con las montañas y el abrazo en la cama
            "fotos": [f"fotos/veinte-{n}.jpg" for n in (9, 18, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20)],
            "pie": "feliz cumpleaños, rubia 💗",
        },
    ],

    # ---------- 4. El cielo de mensajes (una estrella por amigo) ----------
    # video: link de YouTube / Google Drive, o "videos/archivo.mp4"
    "mensajes": [
        {
            "de": "Gaby",
            "desde": "Aguascalientes",
            "texto": """Querida Kiara:

Feliz feliz cumpleaños mi Kiariiis. Que hermoso poder compartir otro cumpleaños contigo y ser igual (o más) cercanas que hace un año jajajjaa.

Ya subiste de escalón, ya cambiaste de dígito y espero lo estes haciendo con todo el orgullo de todo lo que eres y has logrado. Agredezco infinito a Dios siempre el que te haya traído a México, a Aguascalientes para que estemos juntas.

Antes de que tu llegaras la única mujer boliviana de la edad era yo y, aunque quiero mucho a los chicos y confío mucho en ellos, deseaba alguien que me entienda como solo las mujeres nos entendemos, alguien con quien ir al baño jajaja y no ir sola y Diosito como es lo máximo te trajo y no solo una boliviana sino una BAILARINA.

Alguien con una personalidad tan linda con quien compartimos pensamiento e ideales muy parecidos, y en especial, alguien a quien admirar porque mi kiaris eres sorprendente. Admiro tu responsabilidad, tu calma, tu alegría, tu nobleza y tu bondad. Definitivamente serías a la persona a la que iría para que me acompañe a vomitar jajaja

Espero en este año y los que siguen podamos seguir haciendo nuevas aventuras teniendo chistes internos y conociendo nuevos lugares.

Espero nunca te pase por la cabeza el dudar que siempre voy a estar para ti, para lo que sea. Tienes en mi alguien con quien reir y llorar, ir de fiesta o ir a misa y decirte si estas loca o no jaajjajaja

Te ama infinito
Gaby""",
            "foto": "",
            "video": "",
        },
        {
            "de": "Vivi",
            "desde": "",
            "texto": """Feliz cumple kiariss de verdad no sabes lo mucho que te quieroo y lo agradecida y muy feliz que estoy de tenerte en mi vida, gracias por estar ahi siempre para mi y para todas nosotrass 💕 pasatela bonitooo""",
            "foto": "",
            "video": "",
        },
        {
            "de": "Pao",
            "desde": "",
            "texto": """Para: Kiaris
De: Pao

Mi Kiaris te quiero desear un muy lindo cumpleaños y que ojalá sea un día muy único y especial para ti. Que Diosito y la Virgencita siempre te cuiden y iluminen tu camino, y que sea un año lleno de muchas bendiciones. Que siempre seas esa niña tan alegre que nos contagia su alegría a todos los que te rodean, y que siempre seas esa persona tan dedicada, dulce y responsable que admiro demasiado y de la que siempre aprendo mucho.

Que nunca never nos falten nuestras pláticas y saliditas, te quiero tanto tanto y sos de las personas que doy muchas gracias a Diosito por poner en mi vida porque devderdad sos home away from home y siempre que platico o estoy contigo es como un abrazito al corazón. Te mando un abrazo enorme y espero que la pases increíble en tu día, te adoro mi Kiaris y sabe que siempre siempre estoy aquí para ti!!

Con muchísimo Cariño Pao""",
            "foto": "",
            "video": "",
        },
        {
            "de": "Cami",
            "desde": "",
            "texto": """Feliz cumpleañoooos, mi Kiaris! Espero que hoy tengas un día tan hermoso y especial como vos. Te deseo de todo corazón lo mejor hoy y siempre, porque te mereces todas las cosas lindas de la vida. Doy gracias por haberte conocido y por tenerte en mi vida. De verdad espero que sigamos compartiendo muchísimos cumpleaños más, acompañándonos en cada etapa de nuestras vidas.

Eres una persona hermosisima, con un corazón increíble, y quiero que nunca te olvides de lo mucho que vales y lo querida que eres por todos. Quiero que sepas que siempre voy a estar para vos, en los días buenos, en los no tan buenos y en cada momento que me necesites. Espero que disfrutes muchísimo tu día, y que todos tus deseos se hagan realidad. Siempre para voss, te amo mucho ❤️""",
            "foto": "",
            "video": "",
        },
        {
            "de": "Nathy",
            "desde": "",
            "texto": """Para Kiara,

Happiest birthday!! Welcome to your 20's. En este nuevo año, y nueva etapa de tu vida que estás por comenzar espero sepas que deseo, desde el fondo de mi corazón, que la vida te traiga muchas cosas buenas y bonitas, porque te mereces eso y más. Espero que todas las metas que te propongas las puedas alcanzar pero que también podrás descubrir nuevos sueños.

Desde que te conocí es difícil no darse cuenta de la luz y calidez tan bella que transmitis a tu alrededor, sos como un lugar seguro para todos los que te rodean, siempre dispuesta a ayudar a los demás, una cualidad tuya tan característica y admirable. Estoy extremadamente agradecida con la vida por darme la oportunidad de conocerte y que podamos ser tan buenas amigas, y espero podamos seguirlo siendo por muchísimo tiempo.

Admiro muchísimo el esfuerzo y dedicación que le pones a todo lo que haces ya que dejas relucir el amor tan grande que traes dentro de vos. Tu delicadeza y amabilidad destacan tanto, sos como un glitter gel pen en un mundo de lapiceros negros, y espero que sigas transmitiendo eso y que vos misma sepas lo especial que sos.

Desde que estamos juntas en el consejo (viva el consejo), hemos tenido la oportunidad de unirnos un poquito más, y la verdad es que no se que haría sin ti mi Kiara!! Hacemos un dream team súper épico, nos la pasamos increíble y no podría desear un mejor teammate para hacer un trabajo tan bonito como el que procuramos hacer. So, en corto te quiero muchísimo amiga, espero que hoy sea un dia especial y que sea un preámbulo de un nuevo año increíble!!

With love, Nathy""",
            "foto": "",
            "video": "",
        },
        {
            "de": "Jime",
            "desde": "",
            "texto": """BBY KIARA!! Feliz cumpleaños bby, I can’t believe its the second birthday we spend together, pero genuinamente I can’t believe it porque siento como si hubiera pasado muchos más a tu lados.

Eres mi más grande regalo que me dió Dios al venir a México, with you I founded una hermana, eres en quien siempre puedo y podré confiar; and I hope you feel the same. En esta nueva etapa de los 20´s (viejita ;p) espero que te permita crecer y brillar aún más, te deseo todo lo mejor, que se cumplan tus metas propuestas, que siempre encuentres algo por lo que luchar y seguir superándote, que no te falten risas y que sea un año lleno de prosperidad.

Se que los veintes pueden verse un poco aterradores, pero no tengo duda que podrás enfrentarlos increíblemente y que sepas, que estaré a tu lado siempre; cuando necesites un abrazo, un hombro sobre el que llorar, incluso un consejo o un momento para bailar y reír.

Gracias por ser uno de mis grandes modelos a seguir, honestamente eres como mi hermana mayor, and I couldn't be more grateful. Eres una genia, y admiro muchísimo el amor que le pones a todo lo que haces, incluso a las cosas más simples, para mí esa es una de tus virtudes que más me inspiras.

Estoy feliz de haber podido coincidir contigo para experimentar esta etapa tan loca como la universidad, me alegra que seamos the best team!! Y aunque se que estoy un poco loca a veces, nunca me has dejado ni me has juzgado, eres una persona que amo como hermana. I just hope que en tú vida siempre estés acompañada de la gente correcta y rodeada de tanto amor como el que tú esparces.

Recordarte que estoy muy orgullosa de todo lo que has logrado, de como te has superado día a día en México, como has enfrentado tus miedo y lo sigues haciendo. Estás creciendo como una persona increíble, nunca dudes that you are doing great!! Y sé seguirás haciendo incluso mejor ❤.

Gracias por ser mi acompañante leal, te amo con todo mi corazón baby. Feliz día, y no dudes que siempre que me necesites, llegaré volando.

Te amo muchísimo, Jime""",
            "foto": "",
            "video": "",
        },
        {
            "de": "Forns",
            "desde": "",
            "texto": """Kiara ya tienes 20!!!! ☠️☠️☠️

Amorcito!!! Hoy en tu día te quería recordar lo increíble que eres, no podría estar más feliz y orgulloso por la persona en la que te estás convirtiendo, soy tu fan número 1 y todas las cosas que te pasan es por que te lo mereces !!! quiero que entiendas eso SIEMPRE!!! te mereces el mundo entero y más.

Y te prometo que mientras me sigas permitiendo estar a tu lado yo intentaré darte el mundo entero y más… gracias por ser siempre tú y estar en todos lo momentos en especial los duros por qué no se sienten tan feos cuando tú eres la que está escuchando del otro lado, te agradezco todo Y NUNCA CAMBIES!!!

Te amo muchísimo y te mando besos, abrazos y muchas bendiciones amorcito 🥳❤️""",
            "foto": "",
            "video": "",
        },
        {
            "de": "Mila",
            "desde": "",
            "texto": """Que terrible que ya tengas 20, estas vieja!!!!!!!! Esperooo que este año y etapa de tu vida sea igual de bonita o mejor de lo que ya es! Te extraño y amo muuuuuuuuuundos FELIZ CUMPLEAÑOS KIARA!!!!!""",
            "foto": "",
            "video": "",
        },
        {
            "de": "Abu",
            "desde": "",
            "texto": """Princesa hoy te extraño más q nunca te mando un abrazo grande grande. Q dure hasta cuando vengas, que pases un lindo día""",
            "foto": "",
            "video": "",
        },
        {
            "de": "Mami",
            "desde": "",
            "texto": """Mi 🐟 mio de mi, hoy te deseo lo más bonito que se pueda imaginar!! 💖🥳

Que seas muy feliz, tengas mucha salud y siempre estés rodeada de personas que te hagan bien!! 🌻🌻

Hace 20 años llegaste a mi vida y llegaste como una bendición de Diosito 🙏 sos mi primer regalo más preciado y (aunque ya lo sepás..) soy la mamá más feliz y orgullosa del mundo!!! 🥰🥰

Feliz cumple mi 🐟 hermosa!! Te mando el abrazo más fuerte de la vida!! Te amo tanto tanto!! Pasalo hermoso y disfrtutá mucho mucho!!! 🥂🥂🍾💐💝💝""",
            "foto": "",
            "video": "",
        },
        {
            "de": "Fati",
            "desde": "",
            "texto": """Feliz cumple Kiara, espero tengas un día increíble como vos. Espero sepas lo mucho que te quiero y lo agradecida que estoy por tenerte como amiga. Sos uno de los mejores regalitos que me pudo dar México. Me encanta poder tener con vos anécdotas y momentos increíbles.

Espero nunca cambies tu forma tan linda de ser (que haces sonreir a todos en cualquier momento) y que nunca te hagan falta motivos para sonreir. Espero que este nuevo año este lleno de aventuras, anécdotas, logros y que se cumplan todas las metas que te propongas. Nunca te olvides de la maravillosa persona que sos y todo lo bonito que le das al mundo, te mereces lo mejor y espero que este nuevo año te trate igual de bonito o aún mejor. Cheers to twenty te amo muchisiimooo amigaa <33 !!""",
            "foto": "",
            "video": "",
        },
    ],
    # Mensaje que se desbloquea cuando abre TODAS las estrellas
    "mensaje_secreto": "Todas estas personas te quieren y aprecian por la persona que eres, y obvio yo más que nadie.",

    # ---------- 5. Nuestra banda sonora (Spotify) ----------
    # En Spotify: canción → Compartir → Copiar enlace, y pégalo aquí
    "playlist": "",  # ej: "https://open.spotify.com/playlist/xxxxxxxx"
    "canciones": [
        {"titulo": "I Love It", "artista": "Icona Pop ft. Charli XCX", "spotify": "https://open.spotify.com/intl-es/track/2U8NXPTXZWG2O0ye2sYRiH", "porque": "Para cantarla a gritos y que no nos importe nada."},
        {"titulo": "Count on Me", "artista": "Bruno Mars", "spotify": "https://open.spotify.com/intl-es/track/7l1qvxWjxcKpB9PCtBuTbU", "porque": "Porque siempre, siempre vas a poder contar conmigo."},
        {"titulo": "Time of Our Lives", "artista": "Pitbull, Ne-Yo", "spotify": "https://open.spotify.com/intl-es/track/2bJvI42r8EF3wxjOuDav4r", "porque": "Por todas las veces que la pasamos increíble."},
        {"titulo": "Count Me In", "artista": "Liv and Maddie", "spotify": "https://open.spotify.com/intl-es/track/10fVu7S4wYUG82dfEnRktg", "porque": "Para cualquier plan, cuenta conmigo."},
        {"titulo": "The Nights", "artista": "Avicii", "spotify": "https://open.spotify.com/intl-es/track/0ct6r3EGTcMLPtrXHDvVjc", "porque": "Por todas las noches que nunca vamos a olvidar."},
        {"titulo": "Cruisin' for a Bruisin'", "artista": "Teen Beach Movie", "spotify": "https://open.spotify.com/intl-es/track/5e3UWcbvTaF5CJWu81MqlQ", "porque": "La de nuestras rides en auto, a todo volumen."},
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
    "carta": """Para mi rubia favorita, en sus 20 años. 💗

Mi Kiarita:

¡FELICES 20 AÑOS, MI RUBIA FAVORITA!

No sabes lo feliz que me hace poder celebrar este día tan especial para ti. Hoy comienza una nueva década de tu vida y, aunque me encantaría poder estar a tu lado para abrazarte, festejar contigo y hacerte sentir lo especial que eres, nos toca celebrar con unos cuantos kilómetros de distancia de por medio. Quién diría que tendría que felicitarte desde tan lejos, con todo un país de por medio, mientras tú estás en México y yo aquí, deseando poder darte uno de esos abrazos que no necesitan palabras.

Quiero que sepas que, aunque la distancia a veces no nos permita compartir tantos momentos como quisiéramos, eso nunca va a cambiar el cariño tan grande que te tengo. Me encantaría poder aparecer hoy, darte un abrazo enorme, salir a celebrar, reírnos hasta que nos duela la barriga y hacer todas esas cosas que seguramente terminarían convirtiéndose en otra anécdota que recordaríamos durante años. Pero, por ahora, me conformo con mandarte todo mi cariño desde aquí y recordarte lo muchísimo que significas para mí.

A veces me pongo a pensar en todas las personas que llegan a nuestra vida y en lo afortunada que soy de que tú seas una de ellas. Gracias por tu amistad, por cada momento compartido, por las risas, las conversaciones interminables, los chismes, las ocurrencias y hasta por esas pequeñas tonterías que quizás parecen insignificantes, pero que terminan convirtiéndose en los recuerdos más bonitos. Espero que sepas que valoro muchísimo tenerte en mi vida y que siempre voy a guardar un lugar muy especial para ti en mi corazón.

Hoy quiero desearte absolutamente todo lo bonito que existe. Que tus 20 sean una etapa llena de experiencias increíbles, que puedas conocer lugares nuevos, cumplir sueños que alguna vez parecían imposibles, conocer personas maravillosas y descubrir cada vez más la mujer increíble en la que te estás convirtiendo. Que nunca te falten las ganas de comerte el mundo, la valentía para perseguir lo que quieres y la capacidad de encontrar felicidad incluso en las cosas más pequeñas.

Quiero verte cumplir cada una de tus metas, celebrar tus logros y sentirte orgullosa de todo lo que vas construyendo. Y también quiero que recuerdes que no tienes que tener todo resuelto, que está bien equivocarse, cambiar de opinión, empezar de nuevo y tomarse las cosas con calma. Estás comenzando una década que seguramente tendrá muchísimas sorpresas y deseo que la vivas intensamente, que te permitas disfrutarla y que nunca dejes de ser esa persona tan especial que eres.

Y BUENO, hablando de nosotras, creo que tenemos demasiadas cosas pendientes por recuperar. Nos quedan muchísimas recuestas juntas, muchísimos chismes por ponernos al día, noches de hablar de absolutamente todo, salidas improvisadas, fotos, risas, aventuras y, por supuesto, muchísimos vinos que tenemos que compartir. Porque cuando volvamos a estar juntas no pienso aceptar una reunión cortita: quiero tiempo de sobra para ponernos al día, brindar por todo lo que hemos vivido, contar todo lo que nos hemos perdido y crear nuevos recuerdos.

Espero que algún día miremos hacia atrás y nos riamos de esta etapa en la que nos tocó estar lejos, pero que aun así encontramos la manera de seguir presentes en la vida de la otra. Porque si algo tengo claro es que la distancia puede separar ciudades, países y kilómetros, pero no tiene por qué separar a las personas que realmente se quieren. Y yo espero que, sin importar dónde nos encuentre la vida, siempre podamos volver a encontrarnos, sentarnos juntas y sentir que nada ha cambiado.

Quiero que sepas que aquí tienes a alguien que te quiere muchísimo, que se alegra de tus alegrías, que desea verte triunfar y que siempre va a estar feliz de saber que estás cumpliendo tus sueños. Nunca dudes de lo importante que eres ni de todo lo bonito que tienes para ofrecerle al mundo.

Gracias por ser mi Kiara, mi rubia favorita, por existir y por formar parte de mi vida. Ojalá la vida nos regale muchísimos años más de amistad, de cumpleaños que celebrar, de historias que contar y de momentos que algún día recordaremos con una sonrisa enorme.

Por tus 20 años, por todos los sueños que vienen, por las personas que te quieren, por los kilómetros que algún día volveremos a acortar y, sobre todo, por nosotras. Por más recuestas juntas, más vinos, más brindis, más aventuras y más recuerdos que todavía nos esperan.

Te extraño muchísimo y espero que hoy tengas uno de los días más bonitos de tu vida. ¡Disfruta muchísimo, déjate consentir y celebra a lo grande porque te lo mereces!

TE AMO INFINITAMENTE, MI RUBIA FAVORITA. FELICES 20 AÑOS.

Con muchísimo cariño, por siempre tu amiga. ❤️""",

    # Frase final gigante
    "final": "Te quiero hasta las estrellas y de regreso",
    # Frase que va debajo, como firmada a mano
    "final_firma": "always under the same sky",
}
