import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# Configuración del menú horizontal alineado a tus diapositivas
selected = option_menu(
    menu_title=None, 
    options=['Inicio', 'Alfajores', 'Servicios', 'Sobre nosotros'], # Alineado con tu video
    icons=['home', 'folder', 'box-seam', 'person-heart'], 
    menu_icon=None, default_index=0, orientation="horizontal")

if selected == 'Inicio':
    st.markdown("<h1 style='text-align: center; color: #5D4037;'>Lucidulzura</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("Alfajor_cheesecakedemaracuya.jpeg", caption='ALFAJORES HECHOS CON AMOR', width=300)
        
    with col2:
        texto_inicio = """
        En Lucidulzura, transformamos la repostería tradicional en una experiencia de sabor única. 
        Nos dedicamos a la elaboración artesanal de alfajores de chocolate premium y cupcakes finos, 
        cuidando minuciosamente cada detalle, desde la calidad de nuestros ingredientes hasta la presentación final. 
        Creamos el detalle perfecto para regalar, compartir o darte ese gusto que tanto te mereces. 
        ¡Calidad, frescura y dulzura en un solo lugar!
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_inicio}</div>", unsafe_allow_html=True)
# --- NUEVA SECCIÓN: ¿QUÉ OFRECEMOS? ---
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>Nuestras Especialidades y Servicios</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Creamos 3 columnas para mostrar la variedad de manera llamativa
    sec1, sec2, sec3 = st.columns(3)

    with sec1:
        st.markdown("<h3 style='text-align: center; color: #8D6E63;'>Pedidos al por Mayor</h3>", unsafe_allow_html=True)
        # Aquí puedes cambiar "ventas_mayor.jpeg" por el nombre real de tu foto
        st.image("Pack.png", use_container_width=True) 
        st.markdown(
            "<div style='text-align: center; font-size: 15px;'>"
            "¿Tienes un evento, cumpleaños o reunión corporativa? "
            "Llevamos la dulzura a gran escala con precios especiales para pedidos mayoristas."
            "</div>", 
            unsafe_allow_html=True
        )

    with sec2:
        st.markdown("<h3 style='text-align: center; color: #8D6E63;'>Ediciones Temáticas</h3>", unsafe_allow_html=True)
        # Aquí puedes cambiar "alfajores_tematicos.jpeg" por tu foto
        st.image("Feliz_dia_papa.png", use_container_width=True) 
        st.markdown(
            "<div style='text-align: center; font-size: 15px;'>"
            "¡Celebramos cada fecha especial contigo! Diseños exclusivos y personalizados para el "
            "Día de la Madre, Día del Padre y fechas especiales."
            "</div>", 
            unsafe_allow_html=True
        )

    with sec3:
        st.markdown("<h3 style='text-align: center; color: #8D6E63;'>Flores Edition</h3>", unsafe_allow_html=True)
        # Aquí puedes cambiar "alfajores_pride.jpeg" por tu foto
        st.image("Caja_de_alfajores_decorada.jpeg", use_container_width=True) 
        st.markdown(
            "<div style='text-align: center; font-size: 15px;'>"
            "Llenamos de color y sabor tus momentos favoritos con nuestras ediciones especiales llenas de creatividad."
            "</div>", 
            unsafe_allow_html=True
        )
elif selected == 'Alfajores':
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>Desarrollo de un Sistema...</h2>", unsafe_allow_html=True)
    
    st.markdown("### 🎯 Objetivo General")
    st.write(" Objetivo General")
    st.write("Diseñar, desarrollar e implementar una plataforma web integral, funcional y altamente interactiva, estructurada con el propósito de centralizar la gestión de la comunicación comercial y optimizar la recolección de datos cualitativos. El sistema buscará transformar la interacción con el usuario en información de valor mediante el análisis sistemático de sus preferencias, facilitando así la identificación de tendencias de consumo y la toma de decisiones estratégicas basadas en evidencia.")
    
    st.markdown("---")
    
    # NUEVA SECCIÓN: CARTA DE ALFAJORES PREMIUM
    st.markdown("<h3 style='color: #5D4037;'>✨ Nuestra Carta de Alfajores Premium</h3>", unsafe_allow_html=True)
    st.write("Descubre las deliciosas combinaciones artesanales que tenemos para ti:")
    
    # Organizamos la carta en pestañas para que el usuario navegue cómodamente sin saturar la pantalla
    tab1, tab2, tab3 = st.tabs(["Clásicos & Crocantes", "Cítricos & Frutados", "De Colección (Postres)"])
    
    with tab1:
        st.markdown("#### **Clásico de Manjar** | S/ 3.00")
        st.caption("El amor a primera mordida. Nuestra suave y tradicional masa artesanal que se deshace en tu boca, rellena del más cremoso y generoso manjar blanco. El clásico que nunca falla y siempre enamora.")
        
        st.markdown("#### **Tentación de Oreo** | S/ 3.50")
        st.caption("¿Amante del chocolate y la crocancia? Una fusión perfecta de nuestra masa clásica con trocitos de la galleta más famosa del mundo, rellena con una cremosa combinación que te hará pecar sin culpa.")
        
    with tab2:
        st.markdown("#### **Pie de Limón** | S/ 3.50")
        st.caption("El balance perfecto entre dulce y cítrico. Una propuesta fresca y atrevida: masa tradicional rellena de una suave crema de limón hecha en casa, coronada con un toque sutil que recrea la magia del postre original.")
        
        st.markdown("#### **Cheesecake de Maracuyá o Fresa** | S/ 4.00")
        st.caption("La sofisticación hecha alfajor. Elige tu fruta favorita: el toque tropical y ácido de la maracuyá o la dulce frescura de la fresa. Ambos combinados con un sedoso relleno estilo cheesecake que elevará tu experiencia.")
        
    with tab3:
        st.markdown("#### **Alfajor de Tiramisú** | S/ 4.00")
        st.caption("Un viaje directo a Italia en cada bocado. Para los paladares más exigentes. Su masa absorbe las notas del café premium, complementada con un relleno que imita la textura y el sabor del clásico queso mascarpone y un toque de cacao puro en polvo.")
        
        st.markdown("#### **Alfajor de Tres Leches** | S/ 4.00")
        st.caption("¡El más jugoso y sorprendente! Inspirado en el tradicional postre latino. Una masa delicada que abraza un relleno sumamente húmedo y cremoso, concentrando todo el sabor de la mezcla perfecta de tres leches. ¡Una explosión de dulzura!")

    st.markdown("---")
    
    # Simulador o recomendador (Backend con IF-ELIF-ELSE)
    st.markdown("### 🍫 Simulador de Pedidos e Interfaz Predictiva")
    st.write("Elige tus preferencias y el sistema te recomendará tu alfajor ideal de la carta:")
    
    antojo = st.selectbox("¿Qué tipo de sabor prefieres hoy?", ["Intenso/Chocolate", "Dulce tradicional", "Cítrico / Frutado", "Estilo Postre"])
    presupuesto = st.number_input("¿Cuál es tu presupuesto estimado (S/.)?", min_value=0.0, value=5.0)
    
    # Lógica de condicionales enriquecida con tu carta real
   # Asegúrate de que todas estas palabras (if, elif, else) estén perfectamente alineadas a la izquierda:
# Lógica de condicionales enriquecida con tu carta real
    if antojo == "Intenso/Chocolate" and presupuesto >= 3.5:
        recomendacion = "Tu opción ideal es el **Alfajor Tentación de Oreo (S/ 3.50)**."
        
    elif antojo == "Dulce tradicional" and presupuesto >= 3.0:
        recomendacion = "El clásico de clásicos: **Alfajor Clásico de Manjar (S/ 3.00)**."
        
    elif antojo == "Cítrico / Frutado" and presupuesto >= 4.0:
        recomendacion = "Te sugerimos probar el sofisticado **Alfajor Cheesecake de Maracuyá o Fresa (S/ 4.00)**."
        
    elif antojo == "Cítrico / Frutado" and presupuesto >= 3.5:
        recomendacion = "Tu opción ideal es el fresco **Alfajor de Pay de Limón (S/ 3.50)**."
        
    elif antojo == "Estilo Postre" and presupuesto >= 4.0:
        recomendacion = "Debes probar de inmediato el **Alfajor de Tiramisú (S/ 4.00)** o el jugoso **Alfajor de Tres Leches**."
        
    else:
        recomendacion = "¡Contamos con opciones desde S/ 3.00! Ajusta tu presupuesto para recomendarte el alfajor ideal."

    st.info(recomendacion)
elif selected == 'Servicios':
    # 1. Título principal de la sección
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>Mapa: lugares de reparto</h2>", unsafe_allow_html=True)
    
    # 2. Subtítulo y descripción del Mapa
    st.subheader("📍 Georreferenciación y Densidad de Entregas")
    st.write("Visualización de las zonas estratégicas principales de alta repetición de pedidos en Lucidulzura:")
    
    # 3. Apertura y lectura de tu archivo HTML de forma segura
    with open("mapa_trabajofinal.html", "r", encoding="utf-8") as f:
        html_data = f.read()
    
    # 4. Renderizado del mapa en la pantalla de Streamlit
    import streamlit.components.v1 as components
    components.html(html_data, height=500, scrolling=True)
    # 1. Título principal de la sección de Analítica
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>Análisis de Datos y Gráficos del Negocio</h2>", unsafe_allow_html=True)
    
    # 2. Subtítulo y descripción del gráfico
    st.subheader("📊 Distribución de Preferencias en el Mercado")
    st.write("Análisis cualitativo que identifica los sabores con mayor rotación en Lucidulzura.") 
    
    # 3. Tu gráfico directo
    st.image("Aceptacion_sabores_Lucidulzura.png", width=700)
# LÍNEA FINAL DEL MENÚ: Pegada por completo al borde izquierdo
elif selected == 'Sobre nosotros':
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>¿Cómo se creó Lucidulzura?</h2>", unsafe_allow_html=True)
    st.write("""
    Lucidulzura nace de la unión de dos cosas que llenan mi corazón: Lucy, en honor a mi abuelo, y dulzura, por el cariño infinito que le pongo a la repostería artesanal. Es un nombre que lleva historia, respeto y mucho amor familiar en cada letra.

    **Compartiendo un talento, horneando felicidad**

    Esta aventura comenzó como una experiencia hermosa y muy grata. Guiada por mi pasión por la repostería y el deseo de generar mis propios ingresos, descubrí que tenía un talento en las manos que no podía quedarme solo para mí. ¡Tenía que compartirlo con los demás!

    Cada postre que sale de nuestro horno está hecho con paciencia, dedicación y ese toque casero y auténtico que transforma un simple antojo en un momento especial.
    """)
