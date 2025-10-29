import streamlit as st
import pandas as pd

# --- Configuración de la Página ---
st.set_page_config(
    page_title="EcoAprende",
    page_icon="🌱",
    layout="wide"
)

# --- Datos de Progreso Simulados ---
# Esto simula un sistema de progreso y puntajes
progreso = {
    "Solar": {"completado": True, "puntaje": 10},
    "Eolica": {"completado": False, "puntaje": 0},
    "Hidraulica": {"completado": False, "puntaje": 0},
    "Biomasa": {"completado": False, "puntaje": 0},
}
total_lecciones = len(progreso)
lecciones_completadas = sum(1 for data in progreso.values() if data["completado"])
insignias = lecciones_completadas

# --- Funciones de Interacción ---

def mostrar_dashboard():
    """Pantalla Principal: Dashboard del Estudiante."""
    st.header("🌱 EcoAprende: Tu Aventura Ecológica")
    
    # Muestra el progreso
    col1, col2 = st.columns([1, 4])
    with col1:
        st.metric(label="Insignias Obtenidas", value=f"{insignias}/{total_lecciones}", delta="¡Sigue así!")
    with col2:
        st.progress(lecciones_completadas / total_lecciones, text=f"Progreso General: {lecciones_completadas}/{total_lecciones} Lecciones")

    st.markdown("---")
    st.subheader("Selecciona una Lección para empezar a aprender:")
    
    # Tarjetas de Lección
    
    # Crear dos filas de columnas para las tarjetas
    cols1 = st.columns(2)
    cols2 = st.columns(2)
    
    lecciones_keys = list(progreso.keys())
    
    # Tarjeta 1: Solar
    with cols1[0]:
        color = "green" if progreso["Solar"]["completado"] else "orange"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>🌞 Energía Solar</h4>
            <p>Aprende sobre la energía del sol. Puntaje: {progreso["Solar"]["puntaje"]}</p>
            {st.button('Iniciar Lección', key='solar_btn', use_container_width=True)}
        </div>
        """, unsafe_allow_html=True)
        if st.session_state.get('solar_btn'):
            st.session_state['pagina'] = 'solar'
            st.rerun()

    # Tarjeta 2: Eólica
    with cols1[1]:
        color = "green" if progreso["Eolica"]["completado"] else "blue"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>💨 Energía Eólica</h4>
            <p>Aprovecha la fuerza del viento. Puntaje: {progreso["Eolica"]["puntaje"]}</p>
            {st.button('Iniciar Lección', key='eolica_btn', use_container_width=True, disabled=True)}
        </div>
        """, unsafe_allow_html=True)

    # Tarjeta 3: Hidráulica
    with cols2[0]:
        color = "green" if progreso["Hidraulica"]["completado"] else "cyan"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>💧 Energía Hidráulica</h4>
            <p>La potencia del agua en movimiento. Puntaje: {progreso["Hidraulica"]["puntaje"]}</p>
            {st.button('Iniciar Lección', key='hidraulica_btn', use_container_width=True, disabled=True)}
        </div>
        """, unsafe_allow_html=True)

    # Botón para Mini-Juegos (Acceso Rápido)
    with cols2[1]:
        st.markdown(f"""
        <div style="background-color: #e0e0e0; padding: 20px; border-radius: 10px; border-left: 5px solid purple;">
            <h4>🎮 Mini Juegos</h4>
            <p>¡Pon a prueba lo aprendido! (Desbloquea una insignia)</p>
            {st.button('Jugar Ahora', key='juegos_btn', use_container_width=True, disabled=True)}
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")

# --- Lección Detallada (Solar) ---

def mostrar_leccion_solar():
    """Contenido de la Lección de Energía Solar."""
    st.title("🌞 Energía Solar: Aprovechando la Luz")
    
    st.info("💡 **Definición:** La energía solar aprovecha la radiación del sol para generar electricidad o calor.")
    
    col_texto, col_imagen = st.columns(2)
    
    with col_texto:
        st.subheader("Características Principales")
        st.markdown("""
        * **Fuente Inagotable:** Es un recurso que se renueva continuamente.
        * **Bajo Impacto Ambiental:** No produce emisiones de CO2 en su generación.
        * **Aplicación:** Se usa en paneles fotovoltaicos (electricidad) y calentadores solares (calor).
        """)
        
        st.subheader("Beneficios para Chihuahua")
        st.markdown("""
        Chihuahua, con su alto índice de días soleados, tiene un **potencial solar enorme**. Grandes proyectos como parques solares aprovechan esta ventaja para la generación a gran escala.
        """)
        
        # Cuestionario Desplegable
        with st.expander("❓ Cuestionario Rápido: Energía Solar"):
            st.write("¡Responde para ganar 10 Puntos Ecológicos!")
            
            # Pregunta 1
            respuesta1 = st.radio(
                "¿Qué tipo de energía solar genera electricidad directamente?",
                ('Solar Térmica', 'Solar Fotovoltaica', 'Solar Geotérmica')
            )
            
            # Pregunta 2
            respuesta2 = st.radio(
                "¿Cuál es uno de los principales beneficios ambientales?",
                ('Genera pocos residuos', 'Reduce las emisiones de CO2', 'Funciona solo de noche')
            )
            
            if st.button("Enviar Respuestas", key='quiz_solar'):
                puntaje = 0
                feedback = []
                
                # Validación simple del cuestionario
                if respuesta1 == 'Solar Fotovoltaica':
                    puntaje += 5
                    feedback.append("✅ Pregunta 1: ¡Correcto!")
                else:
                    feedback.append("❌ Pregunta 1: Incorrecto. La fotovoltaica convierte luz en electricidad.")
                    
                if respuesta2 == 'Reduce las emisiones de CO2':
                    puntaje += 5
                    feedback.append("✅ Pregunta 2: ¡Correcto!")
                else:
                    feedback.append("❌ Pregunta 2: Incorrecto. El principal beneficio es la reducción de CO2.")
                    
                st.session_state['solar_completado'] = True
                st.session_state['solar_puntaje'] = puntaje
                st.session_state['pagina'] = 'dashboard_update' # Usar una página de transición
                st.rerun()

    with col_imagen:
        st.image("https://images.unsplash.com/photo-1509391007205-d143c7b80b2a", caption="Paneles Solares Fotovoltaicos", use_column_width=True)
        st.video("https://youtu.be/J-p4j11H7y8", caption="Video explicativo simple (Ejemplo)") # Usar un video educativo real si se tiene

    if st.button("⬅️ Volver al Dashboard", key='back_solar'):
        st.session_state['pagina'] = 'dashboard'
        st.rerun()

# --- Lógica de la Aplicación Principal ---

# Inicializar estado de la página si no existe
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = 'dashboard'

# Inicializar estado de las lecciones si no existe
if 'solar_completado' not in st.session_state:
    st.session_state['solar_completado'] = progreso["Solar"]["completado"]
    st.session_state['solar_puntaje'] = progreso["Solar"]["puntaje"]

# Lógica de navegación
if st.session_state['pagina'] == 'dashboard':
    mostrar_dashboard()
elif st.session_state['pagina'] == 'solar':
    mostrar_leccion_solar()
elif st.session_state['pagina'] == 'dashboard_update':
    # Lógica de actualización de progreso después del quiz
    
    if st.session_state.get('solar_completado'):
        progreso["Solar"]["completado"] = True
        progreso["Solar"]["puntaje"] = st.session_state.get('solar_puntaje', 0)
        
        st.success(f"¡Cuestionario completado! Ganaste **{progreso['Solar']['puntaje']}** Puntos Ecológicos.")
        st.balloons()
        
        # Actualiza el estado global de la sesión
        st.session_state['solar_completado'] = progreso["Solar"]["completado"]
        st.session_state['solar_puntaje'] = progreso["Solar"]["puntaje"]
        
        if st.button("Continuar al Dashboard"):
            st.session_state['pagina'] = 'dashboard'
            st.rerun()
