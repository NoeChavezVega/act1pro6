import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EcoAprende",
    page_icon="🌱",
    layout="wide"
)

# ---------------------------
#      PROGRESO INICIAL
# ---------------------------
progreso = {
    "Solar": {"completado": False, "puntaje": 0},
    "Eolica": {"completado": False, "puntaje": 0},
    "Hidraulica": {"completado": False, "puntaje": 0},
    "Biomasa": {"completado": False, "puntaje": 0},
}

total_lecciones = len(progreso)


# ---------------------------
#   FUNCIONES DE PANTALLAS
# ---------------------------

def mostrar_dashboard():
    """Pantalla Principal: Dashboard del Estudiante."""
    st.header("🌱 EcoAprende: Tu Aventura Ecológica")

    lecciones_completadas = sum(1 for data in progreso.values() if data["completado"])
    insignias = lecciones_completadas

    col1, col2 = st.columns([1, 4])
    with col1:
        st.metric(label="Insignias Obtenidas", value=f"{insignias}/{total_lecciones}", delta="¡Sigue así!")
    with col2:
        st.progress(lecciones_completadas / total_lecciones,
                    text=f"Progreso General: {lecciones_completadas}/{total_lecciones} Lecciones")

    st.markdown("---")
    st.subheader("Selecciona una Lección para empezar a aprender:")

    cols1 = st.columns(2)
    cols2 = st.columns(2)

    # ----------- SOLAR ------------
    with cols1[0]:
        color = "green" if progreso["Solar"]["completado"] else "orange"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>🌞 Energía Solar</h4>
            <p>Aprende sobre la energía del sol. Puntaje: {progreso["Solar"]["puntaje"]}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button('Iniciar Lección', key='solar_btn', use_container_width=True):
            st.session_state['pagina'] = 'solar'
            st.rerun()

    # ----------- EÓLICA ------------
    with cols1[1]:
        color = "green" if progreso["Eolica"]["completado"] else "blue"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>💨 Energía Eólica</h4>
            <p>Aprovecha la fuerza del viento. Puntaje: {progreso["Eolica"]["puntaje"]}</p>
        </div>
        """, unsafe_allow_html=True)
        st.button('Iniciar Lección', key='eolica_btn', use_container_width=True, disabled=True)

    # ----------- HIDRÁULICA ------------
    with cols2[0]:
        color = "green" if progreso["Hidraulica"]["completado"] else "cyan"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>💧 Energía Hidráulica</h4>
            <p>La potencia del agua en movimiento. Puntaje: {progreso["Hidraulica"]["puntaje"]}</p>
        </div>
        """, unsafe_allow_html=True)
        st.button('Iniciar Lección', key='hidraulica_btn', use_container_width=True, disabled=True)

    # ----------- MINI JUEGOS ------------
    with cols2[1]:
        st.markdown(f"""
        <div style="background-color: #e0e0e0; padding: 20px; border-radius: 10px; border-left: 5px solid purple;">
            <h4>🎮 Mini Juegos</h4>
            <p>¡Pon a prueba lo aprendido! (Desbloquea una insignia)</p>
        </div>
        """, unsafe_allow_html=True)
        st.button('Jugar Ahora', key='juegos_btn', use_container_width=True, disabled=True)

    st.markdown("---")


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
        Chihuahua, con su alto índice de días soleados, tiene un **potencial solar enorme**. 
        Grandes proyectos como parques solares aprovechan esta ventaja para la generación a gran escala.
        """)

        # ----------------- Cuestionario -----------------
        with st.expander("❓ Cuestionario Rápido: Energía Solar"):
            st.write("¡Responde para ganar 10 Puntos Ecológicos!")

            respuesta1 = st.radio(
                "¿Qué tipo de energía solar genera electricidad directamente?",
                ('Solar Térmica', 'Solar Fotovoltaica', 'Solar Geotérmica')
            )

            respuesta2 = st.radio(
                "¿Cuál es uno de los principales beneficios ambientales?",
                ('Genera pocos residuos', 'Reduce las emisiones de CO2', 'Funciona solo de noche')
            )

            if st.button("Enviar Respuestas", key='quiz_solar'):
                puntaje = 0

                if respuesta1 == 'Solar Fotovoltaica':
                    puntaje += 5

                if respuesta2 == 'Reduce las emisiones de CO2':
                    puntaje += 5

                st.session_state['solar_completado'] = True
                st.session_state['solar_puntaje'] = puntaje
                st.session_state['pagina'] = 'dashboard_update'
                st.rerun()

    with col_imagen:
        st.image("https://images.unsplash.com/photo-1509391007205-d143c7b80b2a",
                 caption="Paneles Solares Fotovoltaicos", use_column_width=True)

    if st.button("⬅️ Volver al Dashboard", key='back_solar'):
        st.session_state['pagina'] = 'dashboard'
        st.rerun()


# ---------------------------
#      MANEJO DE ESTADOS
# ---------------------------

if 'pagina' not in st.session_state:
    st.session_state['pagina'] = 'dashboard'

if 'solar_completado' not in st.session_state:
    st.session_state['solar_completado'] = False
    st.session_state['solar_puntaje'] = 0

# ---------------------------
#      CONTROL DE PÁGINAS
# ---------------------------

if st.session_state['pagina'] == 'dashboard':
    mostrar_dashboard()

elif st.session_state['pagina'] == 'solar':
    mostrar_leccion_solar()

elif st.session_state['pagina'] == 'dashboard_update':

    # Actualizar progreso
    progreso["Solar"]["completado"] = st.session_state['solar_completado']
    progreso["Solar"]["puntaje"] = st.session_state['solar_puntaje']

    st.success(f"¡Cuestionario completado! Ganaste **{progreso['Solar']['puntaje']}** Puntos Ecológicos.")
    st.balloons()

    if st.button("Continuar al Dashboard"):
        st.session_state['pagina'] = 'dashboard'
        st.rerun()
--------------------------------------------------
import streamlit as st
st.title("🌱 EcoAprende de Energías🔌")
progreso = {"Solar": {"completado": False, "puntaje": 0},
    "Eolica": {"completado": False, "puntaje": 0},
    "Hidraulica": {"completado": False, "puntaje": 0},
    "Biomasa": {"completado": False, "puntaje": 0},}
def mostrar_dashboard():
    st.header("Tipos de energias")
    st.subheader("Selecciona una energia:")
    for juego, data in progreso.items():
        nombre_mostrar = f"{juego} {'✔️' if data['completado'] else ''}"
        if st.button(nombre_mostrar, key=f"boton_{juego}"):
            st.session_state["pantalla"] = juego
            
def mostrar_preguntas(preguntas, juego):
    st.header(f" Juego: {juego}")
    puntaje = 0
    respuestas_usuario = {}
    for i, item in enumerate(preguntas):
        pregunta = item["pregunta"]
        opciones = item["opciones"]
        key_radio = f"{juego}_{i}"
        respuesta_usuario = st.radio(pregunta, opciones, key=key_radio)
        respuestas_usuario[i] = respuesta_usuario
    if st.button("Enviar respuestas", key=f"enviar_{juego}"):
        for i, item in enumerate(preguntas):
            if respuestas_usuario[i] == item["correcta"]:
                puntaje += 1
        progreso[juego]["completado"] = True
        progreso[juego]["puntaje"] = puntaje
        st.success(f"Juego completado. Ganaste {puntaje} puntos.")
        st.balloons()
        st.session_state["pantalla"] = "dashboard"

preguntas_solar = [
    {"pregunta":"¿Qué tipo de tecnología utiliza la energía solar?",
     "opciones":["pirolisis y carbonización","multiplicadora","mecánica","fotovoltaica"],
     "correcta":"fotovoltaica"},
    {"pregunta":"¿Qué hacen los electrones liberados en las placas?",
     "opciones":["se almacenan","generan una corriente alterna","luego de ser captados se dispersan","fluyen a través de la placa"],
     "correcta":"generan una corriente alterna"},
    {"pregunta":"¿La energía termo solar requiere de espejos para funcionar?",
     "opciones":["Verdadero","Falso"],
     "correcta":"Verdadero"},
    {"pregunta":"¿Cuál es el componente principal de los materiales que necesita la energía solar?",
     "opciones":["acero","aluminio","silicio","hierro"],
     "correcta":"silicio"},
    {"pregunta":"¿Cuándo los fotones golpean la placa, liberan electrones?",
     "opciones":["Verdadero","Falso"],
     "correcta":"Verdadero"},
    {"pregunta":"¿la temperatura afecta el rendimiento de una celda fotovoltaica?",
     "opciones":["Verdadero","Falso"],
     "correcta":"Falso"},
    {"pregunta":"¿Cuál es la principal razón por la que las celdas solares de silicio tienen mayor eficiencia que las policristalinas?",
     "opciones":["Tienen mayor grosor", "Poseen una estructura uniforme que reduce la recombinación electrónica ","Reflejan más luz para evitar saturación","Permiten operar a temperaturas más altas"],
     "correcta":"Poseen una estructura uniforme que reduce la recombinación electrónica"},
    {"pregunta":"¿Por qué se considera una energía renovable?",
     "opciones":["porque es económica","tiene un menor impacto ambienta","su tecnología es de una calidad mayor","puede usarse en diferentes ámbitos "],
     "correcta":"tiene un menor impacto ambiental"},
    {"pregunta":"¿Cuál de los siguientes factores aumenta la eficiencia de un panel solar?",
     "opciones":["Alta acumulación de polvo"," Alta temperatura ambiental","Orientación adecuada hacia el Sol","Colocarlo en sombra parcial"],
     "correcta":"Orientación adecuada hacia el Sol"},
    {"pregunta":"¿Cuál es una desventaja de la energía solar?",
     "opciones":["Produce gases contaminantes","Depende de la radiación solar ","Emite ruido durante la generación","Requiere combustibles fósiles"],
     "correcta":"Depende de la radiación solar"},]


preguntas_eolica = [{"pregunta":"¿Qué tipo de energía aprovechan los aerogeneradores?",
     "opciones":["Energía solar","Energía del viento","Energía hidráulica","Energía geotérmica"],
     "correcta":"Energía del viento"},
    {"pregunta":"¿Qué parte del aerogenerador recibe directamente la fuerza del viento?",
     "opciones":["Torre","Palas","Generador","Anemómetro"],
     "correcta":"Palas"},
    {"pregunta":"¿Qué mide un anemómetro en un parque eólico?",
     "opciones":["La presión atmosférica","La temperatura","La velocidad del viento","La humedad"],
     "correcta":"La velocidad del viento"},
    {"pregunta":"¿Cuál de estos es un beneficio de la energía eólica?",
     "opciones":["Produce gases tóxicos","Utiliza combustibles fósiles","Es una fuente renovable","Consume grandes cantidades de agua"],
     "correcta":"Es una fuente renovable"},
    {"pregunta":"¿En qué forma se genera la electricidad en un aerogenerador?",
     "opciones":["Combustión interna","Vibraciones mecánicas","Rotación de un eje conectada a un generador","Reacciones químicas"],
     "correcta":"Rotación de un eje conectada a un generador"},
    {"pregunta":"¿Cuál es una desventaja de la energía eólica?",
     "opciones":["Requiere petróleo para operar","Depende de la disponibilidad del viento","Produce dióxido de carbono","Solo funciona de noche"],
     "correcta":"Depende de la disponibilidad del viento"},
    {"pregunta":"¿Cuál es la función del generador dentro de un aerogenerador?",
     "opciones":["Controlar la orientación de las palas","Convertir energía mecánica en eléctrica","Medir la velocidad del viento","Detener el sistema"],
     "correcta":"Convertir energía mecánica en eléctrica"},
    {"pregunta":"¿Qué tipo de energía tiene el viento antes de mover las palas?",
     "opciones":["Energía química","Energía térmica","Energía cinética","Energía sonora"],
     "correcta":"Energía cinética"},
    {"pregunta":"¿Cómo se orientan los aerogeneradores hacia el viento?",
     "opciones":["Se mueven manualmente","Con sensores y un sistema de giro automático","Mediante una brújula","Girando por gravedad"],
     "correcta":"Con sensores y un sistema de giro automático"},
    {"pregunta":"¿Qué países suelen tener mayor potencial para la energía eólica?",
     "opciones":["Países sin costas","Países con fuertes vientos constantes","Países desérticos sin viento","Países muy húmedos"],
     "correcta":"Países con fuertes vientos constantes"}]

preguntas_hidraulica = [
    {"pregunta":"¿Qué tipo de energía aprovechan las plantas hidroeléctricas?",
     "opciones":["Energía térmica","Energía del movimiento del agua","Energía solar","Energía química"],
     "correcta":"Energía del movimiento del agua"},
    {"pregunta":"¿Qué estructura se utiliza para almacenar grandes volúmenes de agua?",
     "opciones":["Pozo","Tubería","Embalse","Sifón"],
     "correcta":"Embalse"},
    {"pregunta": "¿Qué componente convierte la energía del agua en energía mecánica?",
     "opciones": ["Transformador", "Turbina", "Motor eléctrico", "Condensador"],
     "correcta": "Turbina"},
    {"pregunta": "¿Qué se genera cuando la turbina hace girar al generador?",
     "opciones": ["Calor", "Sonido", "Electricidad", "Aire comprimido"],
     "correcta": "Electricidad"},
    {"pregunta": "¿Cuál es un beneficio de la energía hidráulica?",
     "opciones": ["Produce gases de efecto invernadero", "Es renovable", "Requiere petróleo", "No se puede almacenar"],
     "correcta": "Es renovable"},
    {"pregunta": "¿Cuál es una desventaja de la energía hidráulica?",
     "opciones": ["Produce residuos tóxicos", "Depende del caudal de los ríos", "Requiere combustible", "No es renovable"],
     "correcta": "Depende del caudal de los ríos"},
    {"pregunta": "¿Qué nombre recibe la caída de agua que se aprovecha para generar energía?",
     "opciones": ["Captación", "Precipitación", "Salto hidráulico", "Evaporación"],
     "correcta": "Salto hidráulico"},
    {"pregunta": "¿Qué tipo de energía tiene el agua antes de mover la turbina?",
     "opciones": ["Energía sonora", "Energía química", "Energía potencial y cinética", "Energía térmica"],
     "correcta": "Energía potencial y cinética"},
    {"pregunta": "¿Qué componente controla el flujo de agua hacia la turbina?",
     "opciones": ["Alternador", "Compuerta", "Transformador", "Generador auxiliar"],
     "correcta": "Compuerta"},
    {"pregunta": "¿Dónde se instalan típicamente las plantas hidroeléctricas?",
     "opciones": ["En zonas sin agua", "En montañas sin ríos", "En ríos o presas", "En desiertos"],
     "correcta": "En ríos o presas"},
    {"pregunta": "¿Qué mide el caudal de un río?",
     "opciones": ["La profundidad del agua", "La velocidad del viento", "La cantidad de agua que pasa por segundo", "La temperatura del agua"],
     "correcta": "La cantidad de agua que pasa por segundo"},
    {"pregunta": "¿Cómo se llama el proceso de convertir energía mecánica en eléctrica?",
     "opciones": ["Transformación térmica", "Generación eléctrica", "Compresión", "Filtración"],
     "correcta": "Generación eléctrica"}]

preguntas_biomasa = [
    {"pregunta":"¿Qué es la biomasa?",
     "opciones":["Energía del Sol","Materia orgánica utilizada como fuente de energía","Energía del viento","Rocas con minerales energéticos"],
     "correcta":"Materia orgánica utilizada como fuente de energía"},
    {"pregunta":"¿Cuál de los siguientes es un ejemplo de biomasa?",
     "opciones":["Carbón mineral","Aceite vegetal usado","Gas natural","Arena"],
     "correcta":"Aceite vegetal usado"},
    {"pregunta": "¿Qué tipo de energía se obtiene al quemar biomasa?",
     "opciones": ["Energía eléctrica", "Energía térmica", "Energía nuclear", "Energía eólica"],
     "correcta": "Energía térmica"},
    {"pregunta": "¿Cuál es una ventaja del uso de biomasa?",
     "opciones": ["Produce altos niveles de CO₂ fósil", "Es una fuente renovable", "Se agota rápidamente", "Requiere petróleo para funcionar"],
     "correcta": "Es una fuente renovable"},
    {"pregunta": "¿Qué gas se produce en la digestión anaerobia de la biomasa?",
     "opciones": ["Nitrógeno", "Oxígeno", "Metano", "Ozono"],
     "correcta": "Metano"},
    {"pregunta": "¿Cuál de los siguientes recursos NO es biomasa?",
     "opciones": ["Residuos agrícolas", "Madera", "Restos de comida", "Hierro mineral"],
     "correcta": "Hierro mineral"},
    {"pregunta": "¿Qué proceso convierte residuos orgánicos húmedos en biogás?",
     "opciones": ["Evaporación", "Digestión anaerobia", "Destilación", "Pirólisis"],
     "correcta": "Digestión anaerobia"},
    {"pregunta": "¿Qué combustible se obtiene de algunos cultivos como el maíz o la caña de azúcar?",
     "opciones": ["Diésel fósil", "Etanol", "Propano", "Gasolina"],
     "correcta": "Etanol"},
    {"pregunta": "¿Qué tipo de energía tiene la biomasa antes de ser procesada?",
     "opciones": ["Energía química almacenada", "Energía sonora", "Energía lumínica", "Energía cinética"],
     "correcta": "Energía química almacenada"},
    {"pregunta": "¿Qué impacto ambiental puede tener el uso excesivo de biomasa?",
     "opciones": ["Desaparición del viento", "Deforestación", "Aumento del gas ozono", "Contaminación radiactiva"],
     "correcta": "Deforestación"}]

if "pantalla" not in st.session_state:
    st.session_state["pantalla"] = "dashboard"
if st.session_state["pantalla"] == "dashboard":
    mostrar_dashboard()
elif st.session_state["pantalla"] == "Solar":
    mostrar_preguntas(preguntas_solar, "Solar")
elif st.session_state["pantalla"] == "Eolica":
    mostrar_preguntas(preguntas_eolica, "Eolica")
elif st.session_state["pantalla"] == "Hidraulica":
    mostrar_preguntas(preguntas_hidraulica, "Hidraulica")
elif st.session_state["pantalla"] == "Biomasa":
    mostrar_preguntas(preguntas_biomasa, "Biomasa")

