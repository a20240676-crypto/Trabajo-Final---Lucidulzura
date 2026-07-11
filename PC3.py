import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# Configuración del menú horizontal alineado a tus diapositivas
selected = option_menu(
    menu_title=None, 
    options=['Inicio', 'Proyecto', 'Servicios', 'Sobre nosotros'], # Alinado con tu video
    icons=['home', 'folder', 'box-seam', 'person-heart'], 
    menu_icon=None, default_index=0, orientation="horizontal")

if selected == 'Inicio':
    st.markdown("<h1 style='text-align: center; color: #5D4037;'>Lucidulzura</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("Ana.jpeg", caption='Ana Lucía Ibañez - Fundadora', width=300)
        
    with col2:
        texto_inicio = """
        En **Lucidulzura**, transformamos la repostería tradicional en una experiencia de sabor única. 
        Nos dedicamos a la elaboración artesanal de alfajores de chocolate premium y cupcakes finos, 
        cuidando minuciosamente cada detalle, desde la calidad de nuestros ingredientes hasta la presentación final. 
        Creamos el detalle perfecto para regalar, compartir o darte ese gusto que tanto te mereces. 
        ¡Calidad, frescura y dulzura en un solo lugar!
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_inicio}</div>", unsafe_allow_html=True)

elif selected == 'Proyecto':
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>Desarrollo de un Sistema Interactivos de Comunicación</h2>", unsafe_allow_html=True)
    
    st.markdown("### 🎯 Objetivo General")
    st.write("Desarrollar una plataforma web funcional e interactiva que sirva como sistema de comunicación comercial y análisis de preferencias.")
    
    # Simulador o recomendador que mencionas en tu video (Backend con IF-ELIF-ELSE)
    st.markdown("---")
    st.markdown("### 🍫 Simulador de Pedidos e Interfaz Predictiva")
    st.write("Elige tus preferencias y el sistema te recomendará el alfajor ideal:")
    
    antojo = st.selectbox("¿Qué tipo de sabor prefieres hoy?", ["Intenso/Amargo", "Dulce tradicional", "Suave"])
    presupuesto = st.number_input("¿Cuál es tu presupuesto estimado (S/.)?", min_value=0.0, value=15.0)
    
    # Lógica de condicionales (If-elif-else) que explicaste en la exposición
    if antojo == "Intenso/Amargo" and presupuesto >= 12:
        recomendacion = "Te recomendamos nuestra caja de **Alfajores de Chocolate Bitter Premium**."
    elif antojo == "Dulce tradicional":
        recomendacion = "Tu opción ideal son nuestros clásicos **Alfajores de Manjar Blanco artesanal** con polvo de azúcar."
    else:
        recomendacion = "Te sugerimos probar nuestros **Cupcakes Finos de Vainilla y crema suave**."
        
    st.info(recomendacion)

elif selected == 'Servicios':
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>Análisis de Datos y Gráficos del Negocio</h2>", unsafe_allow_html=True)
    
    # Selector de gráficos estadísticos (Matplotlib que mencionas en el video)
    grafico = st.selectbox("Selecciona la métrica comercial que deseas revisar:", ["Aceptación de Sabores", "Control Administrativo (Ventas)"])
    
    if grafico == "Aceptación de Sabores":
        st.subheader("📊 Distribución de Preferencias en el Mercado")
        st.write("Análisis vectorial que identifica los sabores con mayor rotación.")
        # Aquí jalarás tu gráfico redondo de sabores
        st.image("aceptacion_sabores.png", width=700) 
        
    elif grafico == "Control Administrativo (Ventas)":
        st.subheader("📈 Comportamiento de Puntos de Venta")
        st.write("Optimización de stock y tendencias en tiempo real.")
        st.image("control_administrativo.png", width=700)

elif selected == 'Sobre nosotros':
    st.markdown("<h2 style='text-align: center; color: #5D4037;'>Mi Experiencia Programando 💻</h2>", unsafe_allow_html=True)
    
    texto_exp = """
    Al inicio estaba nerviosa porque no conocía demasiado del entorno de desarrollo. Sin embargo, este proceso 
    me demostró que la programación es una herramienta clave para cualquier comunicador en la era digital. 
    Nos permite entender cómo funcionan las interfaces, interactuar con bases de datos y procesar feedback 
    para tomar decisiones basadas en datos reales.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_exp}</div>", unsafe_allow_html=True)
    
    # Enlaces a tus videos de Canva que sustentan tus prácticas previas
    st.markdown("---")
    st.markdown("#### 🎥 Evidencias de aprendizaje (Prácticas del curso)")
    
    colA, colB, colC = st.columns(3)
    with colA:
        st.link_button("Video 1: Strings y Listas", "https://canva.link/hpbib9zh7qu3t0d")
    with colB:
        st.link_button("Video 2: Bucles For y While", "https://canva.link/rbkg3dluhxar8d9")
    with colC:
        st.link_button("Video 3: Sustentación Blog", "https://canva.link/sekfxj7b57e9oaf")
