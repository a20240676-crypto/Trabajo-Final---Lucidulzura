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
        st.image("Alfajor_cheesecakedemaracuya.jpeg", caption='alfajor de cheeesecake de maracuya - alfajor', width=300)
        
    with col2:
        texto_inicio = """
        En Lucidulzura, transformamos la repostería tradicional en una experiencia de sabor única. 
        Nos dedicamos a la elaboración artesanal de alfajores de chocolate premium y cupcakes finos, 
        cuidando minuciosamente cada detalle, desde la calidad de nuestros ingredientes hasta la presentación final. 
        Creamos el detalle perfecto para regalar, compartir o darte ese gusto que tanto te mereces. 
        ¡Calidad, frescura y dulzura en un solo lugar!
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_inicio}</div>", unsafe_allow_html=True)

elif selected == 'Proyecto':
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>Desarrollo de un Sistema Interactivo de Comunicación</h2>", unsafe_allow_html=True)
    
    st.markdown("### 🎯 Objetivo General")
    st.write("Desarrollar una plataforma web funcional e interactiva que sirva como sistema de comunicación comercial y análisis de preferencias.")
    
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
    presupuesto = st.number_input("¿Cuál es tu presupuesto estimado (S/.)?", min_value=0.0, value=15.0)
    
    # Lógica de condicionales enriquecida con tu carta real
    if antojo == "Intenso/Chocolate" and presupuesto >= 3.5:
        recomendacion = "Tu opción ideal es el **Alfajor Tentación de Oreo (S/ 3.50)**."
    elif antojo == "Dulce tradicional" and presupuesto >= 3.0:
        recomendacion = "El clásico de clásicos: **Alfajor Clásico de Manjar (S/ 3.00)**."
    elif antojo == "Cítrico / Frutado" and presupuesto >= 4.0:
        recomendacion = "Te sugerimos probar el sofisticado **Alfajor Cheesecake de Maracuyá o Fresa (S/ 4.00)** o el fresco **Pie de Limón (S/ 3.50)**."
    elif antojo == "Estilo Postre" and presupuesto >= 4.0:
        recomendacion = "Debes probar de inmediato el **Alfajor de Tiramisú (S/ 4.00)** o el jugoso **Alfajor de Tres Leches (S/ 4.00)**."
    else:
        recomendacion = "¡Contamos con opciones desde S/ 3.00! Ajusta tu presupuesto para recomendarte el alfajor ideal."
        
    st.info(recomendacion)

elif selected == 'Servicios':
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>Análisis de Datos y Gráficos del Negocio</h2>", unsafe_allow_html=True)
    
    grafico = st.selectbox("Selecciona la métrica comercial que deseas revisar:", ["Aceptación de Sabores", "Control Administrativo (Ventas)"])
    
    if grafico == "Aceptación de Sabores":
        st.subheader("📊 Distribución de Preferencias en el Mercado")
        st.write("Análisis vectorial que identifica los sabores con mayor rotación.")
        st.image("aceptacion_sabores.png", width=700) 
        
    elif grafico == "Control Administrativo (Ventas)":
        st.subheader("📈 Comportamiento de Puntos de Venta")
        st.write("Optimización de stock y tendencias en tiempo real.")
        st.image("control_administrative.png", width=700)

elif selected == 'Sobre nosotros':
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>Mi Experiencia Programando 💻</h2>", unsafe_allow_html=True)
    
    texto_exp = """
    Al inicio estaba nerviosa porque no conocía demasiado del entorno de desarrollo. Sin embargo, este proceso 
    me demostró que la programación es una herramienta clave para cualquier comunicador en la era digital. 
    Nos permite entender cómo funcionan las interfaces, interactuar con bases de datos y procesar feedback 
    para tomar decisiones basadas en datos reales.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_exp}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 🎥 Evidencias de aprendizaje (Prácticas del curso)")
    
    colA, colB, colC = st.columns(3)
    with colA:
        st.link_button("Video 1: Strings y Listas", "https://canva.link/hpbib9zh7qu3t0d")
    with colB:
        st.link_button("Video 2: Bucles For y While", "https://canva.link/rbkg3dluhxar8d9")
    with colC:
        st.link_button("Video 3: Sustentación Blog", "https://canva.link/sekfxj7b57e9oaf")
