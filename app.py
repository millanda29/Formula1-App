import streamlit as st
import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import plotly.colors as pc

# -----------------------------
# 📅 Calendario de la F1 2025
# -----------------------------
calendario = [
    {"ronda": 1, "gran_premio": "Australia", "fecha": "16 de marzo", "circuito": "Albert Park", "fecha_completa": "14-16 de marzo", "sprint": False},
    {"ronda": 2, "gran_premio": "China", "fecha": "23 de marzo", "circuito": "Shanghai", "fecha_completa": "21-23 de marzo", "sprint": True},
    {"ronda": 3, "gran_premio": "Japón", "fecha": "6 de abril", "circuito": "Suzuka", "fecha_completa": "4-6 de abril", "sprint": False},
    {"ronda": 4, "gran_premio": "Baréin", "fecha": "13 de abril", "circuito": "Sakhir", "fecha_completa": "11-13 de abril", "sprint": False},
    {"ronda": 5, "gran_premio": "Arabia Saudita", "fecha": "20 de abril", "circuito": "Jeddah", "fecha_completa": "18-20 de abril", "sprint": False},
    {"ronda": 6, "gran_premio": "Miami", "fecha": "4 de mayo", "circuito": "Hard Rock Stadium", "fecha_completa": "2-4 de mayo", "sprint": True},
    {"ronda": 7, "gran_premio": "Emilia-Romaña", "fecha": "18 de mayo", "circuito": "Imola", "fecha_completa": "16-18 de mayo", "sprint": False},
    {"ronda": 8, "gran_premio": "Mónaco", "fecha": "25 de mayo", "circuito": "Montecarlo", "fecha_completa": "23-25 de mayo", "sprint": False},
    {"ronda": 9, "gran_premio": "España", "fecha": "1 de junio", "circuito": "Catalunya", "fecha_completa": "30 mayo - 1 junio", "sprint": False},
    {"ronda": 10, "gran_premio": "Canadá", "fecha": "15 de junio", "circuito": "Gilles Villeneuve", "fecha_completa": "13-15 de junio", "sprint": False},
    {"ronda": 11, "gran_premio": "Austria", "fecha": "29 de junio", "circuito": "Red Bull Ring", "fecha_completa": "27-29 de junio", "sprint": False},
    {"ronda": 12, "gran_premio": "Gran Bretaña", "fecha": "6 de julio", "circuito": "Silverstone", "fecha_completa": "4-6 de julio", "sprint": False},
    {"ronda": 13, "gran_premio": "Bélgica", "fecha": "27 de julio", "circuito": "Spa-Francorchamps", "fecha_completa": "25-27 de julio", "sprint": True},
    {"ronda": 14, "gran_premio": "Hungría", "fecha": "3 de agosto", "circuito": "Hungaroring", "fecha_completa": "1-3 de agosto", "sprint": False},
    {"ronda": 15, "gran_premio": "Países Bajos", "fecha": "31 de agosto", "circuito": "Zandvoort", "fecha_completa": "29-31 de agosto", "sprint": False},
    {"ronda": 16, "gran_premio": "Italia", "fecha": "7 de septiembre", "circuito": "Monza", "fecha_completa": "5-7 de septiembre", "sprint": False},
    {"ronda": 17, "gran_premio": "Azerbaiyán", "fecha": "21 de septiembre", "circuito": "Baku", "fecha_completa": "19-21 de septiembre", "sprint": False},
    {"ronda": 18, "gran_premio": "Singapur", "fecha": "5 de octubre", "circuito": "Marina Bay", "fecha_completa": "3-5 de octubre", "sprint": False},
    {"ronda": 19, "gran_premio": "Estados Unidos", "fecha": "19 de octubre", "circuito": "Las Américas", "fecha_completa": "17-19 de octubre", "sprint": True},
    {"ronda": 20, "gran_premio": "México", "fecha": "26 de octubre", "circuito": "Hermanos Rodríguez", "fecha_completa": "24-26 de octubre", "sprint": False},
    {"ronda": 21, "gran_premio": "São Paulo", "fecha": "9 de noviembre", "circuito": "Interlagos", "fecha_completa": "7-9 de noviembre", "sprint": True},
    {"ronda": 22, "gran_premio": "Las Vegas", "fecha": "22 de noviembre", "circuito": "Las Vegas", "fecha_completa": "21-22 de noviembre", "sprint": False},
    {"ronda": 23, "gran_premio": "Catar", "fecha": "30 de noviembre", "circuito": "Losail", "fecha_completa": "28-30 de noviembre", "sprint": True},
    {"ronda": 24, "gran_premio": "Abu Dabi", "fecha": "7 de diciembre", "circuito": "Yas Marina", "fecha_completa": "5-7 de diciembre", "sprint": False},
]

# -----------------------------
# 🧑‍🤝‍🧑 Pilotos y Equipos
# -----------------------------
pilotos_equipos = {
    "Max Verstappen": {"equipo": "Red Bull Racing", "emoji": "🇳🇱", "color": "#3671C6"},
    "Liam Lawson": {"equipo": "Red Bull Racing", "emoji": "🇳🇿", "color": "#3671C6"},
    "Charles Leclerc": {"equipo": "Ferrari", "emoji": "🇲🇨", "color": "#F91536"},
    "Lewis Hamilton": {"equipo": "Ferrari", "emoji": "🇬🇧", "color": "#F91536"},
    "George Russell": {"equipo": "Mercedes", "emoji": "🇬🇧", "color": "#6CD3BF"},
    "Andrea Kimi Antonelli": {"equipo": "Mercedes", "emoji": "🇮🇹", "color": "#6CD3BF"},
    "Lando Norris": {"equipo": "McLaren", "emoji": "🇬🇧", "color": "#FF8000"},
    "Oscar Piastri": {"equipo": "McLaren", "emoji": "🇦🇺", "color": "#FF8000"},
    "Fernando Alonso": {"equipo": "Aston Martin", "emoji": "🇪🇸", "color": "#358C75"},
    "Lance Stroll": {"equipo": "Aston Martin", "emoji": "🇨🇦", "color": "#358C75"},
    "Pierre Gasly": {"equipo": "Alpine", "emoji": "🇫🇷", "color": "#2293D1"},
    "Jack Doohan": {"equipo": "Alpine", "emoji": "🇦🇺", "color": "#2293D1"},
    "Esteban Ocon": {"equipo": "Haas", "emoji": "🇫🇷", "color": "#B6BABD"},
    "Oliver Bearman": {"equipo": "Haas", "emoji": "🇬🇧", "color": "#B6BABD"},
    "Yuki Tsunoda": {"equipo": "RB", "emoji": "🇯🇵", "color": "#5E8FAA"},
    "Isack Hadjar": {"equipo": "RB", "emoji": "🇫🇷", "color": "#5E8FAA"},
    "Alexander Albon": {"equipo": "Williams", "emoji": "🇹🇭", "color": "#37003C"},
    "Carlos Sainz": {"equipo": "Williams", "emoji": "🇪🇸", "color": "#37003C"},
    "Nico Hülkenberg": {"equipo": "Sauber", "emoji": "🇩🇪", "color": "#52E252"},
    "Gabriel Bortoleto": {"equipo": "Sauber", "emoji": "🇧🇷", "color": "#52E252"},
    "Franco Colapinto": {"equipo": "Sauber", "emoji": "🇦🇷", "color": "#52E252"}
}

pilotos_titulares = list(pilotos_equipos.keys())

# -----------------------------
# 📂 Archivo de Resultados
# -----------------------------
archivo_resultados = "resultados.txt"
archivo_resultados_sprint = "resultados_sprint.txt"

# -----------------------------
# 🏁 Sistema de Puntuación
# -----------------------------
puntos_por_posicion = {
    1: 25, 2: 18, 3: 15, 4: 12, 5: 10,
    6: 8, 7: 6, 8: 4, 9: 2, 10: 1
}

# Sistema de puntuación para Sprint
puntos_sprint = {
    1: 8, 2: 7, 3: 6, 4: 5, 5: 4,
    6: 3, 7: 2, 8: 1
}

# -----------------------------
# 🔎 Leer resultados existentes
# -----------------------------
def leer_resultados():
    resultados = {}
    if os.path.exists(archivo_resultados):
        with open(archivo_resultados, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:  # Ignorar líneas vacías
                    try:
                        ronda, piloto, posicion = linea.split(",")
                        ronda = int(ronda)
                        if ronda not in resultados:
                            resultados[ronda] = []
                        resultados[ronda].append((piloto, int(posicion)))
                    except ValueError:
                        # Ignorar líneas malformadas
                        continue
    return resultados

def leer_resultados_sprint():
    resultados_sprint = {}
    if os.path.exists(archivo_resultados_sprint):
        with open(archivo_resultados_sprint, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:  # Ignorar líneas vacías
                    try:
                        ronda, piloto, posicion = linea.split(",")
                        ronda = int(ronda)
                        if ronda not in resultados_sprint:
                            resultados_sprint[ronda] = []
                        resultados_sprint[ronda].append((piloto, int(posicion)))
                    except ValueError:
                        # Ignorar líneas malformadas
                        continue
    return resultados_sprint

# -----------------------------
# 📊 Calcular clasificación general
# -----------------------------
def calcular_clasificacion(resultados, resultados_sprint=None):
    clasificacion = {}
    
    # Puntos de carreras principales
    for rondas in resultados.values():
        for piloto, posicion in rondas:
            puntos = puntos_por_posicion.get(posicion, 0)
            clasificacion[piloto] = clasificacion.get(piloto, 0) + puntos
    
    # Agregar puntos de Sprint si están disponibles
    if resultados_sprint:
        for rondas_sprint in resultados_sprint.values():
            for piloto, posicion in rondas_sprint:
                puntos = puntos_sprint.get(posicion, 0)
                clasificacion[piloto] = clasificacion.get(piloto, 0) + puntos
    
    return clasificacion

# -----------------------------
# 📊 Calcular clasificación por equipos
# -----------------------------
def calcular_clasificacion_equipos(resultados, resultados_sprint=None):
    clasificacion_equipos = {}
    
    # Puntos de carreras principales
    for rondas in resultados.values():
        for piloto, posicion in rondas:
            puntos = puntos_por_posicion.get(posicion, 0)
            equipo = pilotos_equipos[piloto]["equipo"]
            clasificacion_equipos[equipo] = clasificacion_equipos.get(equipo, 0) + puntos
    
    # Agregar puntos de Sprint si están disponibles
    if resultados_sprint:
        for rondas_sprint in resultados_sprint.values():
            for piloto, posicion in rondas_sprint:
                puntos = puntos_sprint.get(posicion, 0)
                equipo = pilotos_equipos[piloto]["equipo"]
                clasificacion_equipos[equipo] = clasificacion_equipos.get(equipo, 0) + puntos
    
    return clasificacion_equipos

# -----------------------------
# 📈 Crear gráfico de evolución de puntos
# -----------------------------
def crear_grafico_evolucion(resultados):
    if not resultados:
        return None
    
    # Preparar datos para el gráfico
    datos_evolucion = {}
    clasificacion_acumulada = {}
    
    for ronda in sorted(resultados.keys()):
        for piloto, posicion in resultados[ronda]:
            puntos = puntos_por_posicion.get(posicion, 0)
            if piloto not in clasificacion_acumulada:
                clasificacion_acumulada[piloto] = 0
            clasificacion_acumulada[piloto] += puntos
            
            if piloto not in datos_evolucion:
                datos_evolucion[piloto] = []
            datos_evolucion[piloto].append({
                'ronda': ronda,
                'puntos_acumulados': clasificacion_acumulada[piloto]
            })
    
    # Crear DataFrame
    df_list = []
    for piloto, datos in datos_evolucion.items():
        for punto in datos:
            df_list.append({
                'Piloto': piloto,
                'Ronda': punto['ronda'],
                'Puntos': punto['puntos_acumulados'],
                'Equipo': pilotos_equipos[piloto]["equipo"],
                'Color': pilotos_equipos[piloto]["color"]
            })
    
    if not df_list:
        return None
        
    df = pd.DataFrame(df_list)
    
    # Crear gráfico
    fig = px.line(df, x='Ronda', y='Puntos', color='Piloto',
                  title='🏆 Evolución del Campeonato de Pilotos',
                  labels={'Puntos': 'Puntos Acumulados', 'Ronda': 'Ronda del GP'})
    
    fig.update_layout(
        height=600,
        showlegend=True,
        legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02)
    )
    
    return fig

# -----------------------------
# 📊 Crear gráfico de barras del campeonato
# -----------------------------
def crear_grafico_clasificacion(clasificacion):
    if not clasificacion:
        return None
    
    df_clasificacion = []
    for piloto, puntos in sorted(clasificacion.items(), key=lambda x: x[1], reverse=True):
        df_clasificacion.append({
            'Piloto': f"{pilotos_equipos[piloto]['emoji']} {piloto}",
            'Puntos': puntos,
            'Equipo': pilotos_equipos[piloto]["equipo"],
            'Color': pilotos_equipos[piloto]["color"]
        })
    
    df = pd.DataFrame(df_clasificacion)
    
    fig = px.bar(df, x='Puntos', y='Piloto', color='Equipo',
                 title='🏁 Clasificación General de Pilotos',
                 labels={'Puntos': 'Puntos Totales'},
                 orientation='h')
    
    fig.update_layout(
        height=800, 
        showlegend=True,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    return fig

# -----------------------------
# 🏎️ Crear gráfico de equipos
# -----------------------------
def crear_grafico_equipos(clasificacion_equipos):
    if not clasificacion_equipos:
        return None
    
    df_equipos = []
    for equipo, puntos in sorted(clasificacion_equipos.items(), key=lambda x: x[1], reverse=True):
        # Buscar el color del equipo
        color_equipo = "#000000"  # Color por defecto
        for piloto, datos in pilotos_equipos.items():
            if datos["equipo"] == equipo:
                color_equipo = datos["color"]
                break
        
        df_equipos.append({
            'Equipo': equipo,
            'Puntos': puntos,
            'Color': color_equipo
        })
    
    df = pd.DataFrame(df_equipos)
    
    fig = px.bar(df, x='Equipo', y='Puntos',
                 title='🏆 Clasificación de Constructores',
                 labels={'Puntos': 'Puntos Totales'},
                 color='Equipo')
    
    fig.update_layout(
        height=500, 
        showlegend=False,
        xaxis={'tickangle': 45}
    )
    
    return fig

def crear_grafico_evolucion_detallado(resultados, resultados_sprint):
    """Crear gráfico de evolución más detallado incluyendo sprint"""
    if not resultados:
        return None
    
    # Obtener todos los pilotos que han participado
    todos_pilotos = set()
    for ronda_resultados in resultados.values():
        for piloto, _ in ronda_resultados:
            todos_pilotos.add(piloto)
    
    # Limitar a top 8 para mejor visualización
    clasificacion_actual = calcular_clasificacion(resultados, resultados_sprint)
    top_pilotos = sorted(clasificacion_actual.items(), key=lambda x: x[1], reverse=True)[:8]
    pilotos_seleccionados = [piloto for piloto, _ in top_pilotos]
    
    data = []
    
    # Procesar cada ronda
    todas_rondas = sorted(set(list(resultados.keys()) + list(resultados_sprint.keys())))
    
    for ronda in todas_rondas:
        for piloto in pilotos_seleccionados:
            # Calcular puntos acumulados hasta esta ronda
            puntos_acumulados = 0
            
            # Sumar puntos de carreras principales hasta esta ronda
            for r in range(1, ronda + 1):
                if r in resultados:
                    for p, pos in resultados[r]:
                        if p == piloto:
                            puntos_acumulados += puntos_por_posicion.get(pos, 0)
                            break
                
                # Sumar puntos de sprint hasta esta ronda
                if r in resultados_sprint:
                    for p, pos in resultados_sprint[r]:
                        if p == piloto:
                            puntos_acumulados += puntos_sprint.get(pos, 0)
                            break
            
            # Determinar tipo de carrera
            tipo_carrera = "Sprint + Carrera" if ronda in resultados_sprint and ronda in resultados else "Solo Carrera"
            
            data.append({
                'Ronda': ronda,
                'Piloto': piloto,
                'Puntos': puntos_acumulados,
                'Tipo': tipo_carrera,
                'Emoji': pilotos_equipos[piloto]["emoji"],
                'Color': pilotos_equipos[piloto]["color"]
            })
    
    if not data:
        return None
    
    df = pd.DataFrame(data)
    
    # Crear el gráfico
    fig = px.line(df, x='Ronda', y='Puntos', color='Piloto',
                  title='📈 Evolución de Puntos por Piloto (Incluye Sprint)',
                  labels={'Puntos': 'Puntos Acumulados', 'Ronda': 'Ronda del Campeonato'},
                  markers=True)
    
    # Personalizar colores por piloto
    color_map = {}
    for piloto in pilotos_seleccionados:
        color_map[piloto] = pilotos_equipos[piloto]["color"]
    
    # Actualizar colores de las líneas
    for i, piloto in enumerate(pilotos_seleccionados):
        if i < len(fig.data):
            fig.data[i].line.color = color_map[piloto]
            fig.data[i].marker.color = color_map[piloto]
    
    # Marcar rondas Sprint
    rondas_sprint = [r for r in todas_rondas if r in resultados_sprint]
    for ronda_sprint in rondas_sprint:
        fig.add_vline(x=ronda_sprint, line_dash="dot", line_color="orange", 
                     annotation_text=f"Sprint R{ronda_sprint}", annotation_position="top")
    
    fig.update_layout(
        height=600,
        hovermode='x unified',
        xaxis={'tickmode': 'linear', 'tick0': 1, 'dtick': 1},
        legend={'orientation': 'h', 'yanchor': 'bottom', 'y': 1.02, 'xanchor': 'right', 'x': 1}
    )
    
    return fig

# -----------------------------
# 🖥️ Configuración de página
# -----------------------------
st.set_page_config(
    page_title="🏎️ F1 2025 Championship",
    page_icon="🏁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar la apariencia
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #FF6B6B;
        margin: 0.5rem 0;
    }
    .podium-card {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    .stSelectbox label {
        font-weight: bold;
        color: #2E3440;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 🖥️ Interfaz de Streamlit
# -----------------------------
st.markdown('<div class="main-header"><h1>🏎️ Temporada 2025 de Fórmula 1 🏁</h1></div>', unsafe_allow_html=True)

# Sidebar para navegación
st.sidebar.title("🏁 Navegación")
seccion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["🏆 Dashboard Principal", "📊 Análisis Detallado", "📥 Gestión de Resultados", "📅 Calendario"]
)

# Cargar resultados previos
resultados = leer_resultados()
resultados_sprint = leer_resultados_sprint()
clasificacion = calcular_clasificacion(resultados, resultados_sprint)
clasificacion_equipos = calcular_clasificacion_equipos(resultados, resultados_sprint)

# -----------------------------
# � FUNCIÓN AUXILIAR PARA MOSTRAR RESULTADOS
# -----------------------------
def mostrar_resultados_carrera(resultados_lista, sistema_puntos, es_sprint):
    """Función para mostrar los resultados de una carrera (principal o sprint)"""
    if not resultados_lista:
        return
        
    resultados_actuales = sorted(resultados_lista, key=lambda x: x[1])
    
    # Crear tarjetas para cada resultado
    for piloto, posicion in resultados_actuales:
        emoji_pais = pilotos_equipos[piloto]["emoji"]
        equipo = pilotos_equipos[piloto]["equipo"]
        puntos = sistema_puntos.get(posicion, 0)
        
        # Determinar la clase CSS según la posición y tipo de carrera
        if posicion == 1:
            css_class = "position-1"
            emoji_pos = "🥇"
        elif posicion == 2:
            css_class = "position-2"
            emoji_pos = "🥈"
        elif posicion == 3:
            css_class = "position-3"
            emoji_pos = "🥉"
        elif es_sprint and posicion <= 8:
            css_class = "sprint-points"
            emoji_pos = f"P{posicion}"
        elif not es_sprint and posicion <= 10:
            css_class = "points-zone"
            emoji_pos = f"P{posicion}"
        else:
            css_class = "no-points"
            emoji_pos = f"P{posicion}"
        
        # Crear la tarjeta del resultado
        st.markdown(f"""
        <div class="result-card {css_class}">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div class="position-number">{emoji_pos}</div>
                    <div>
                        <div class="driver-name">{emoji_pais} {piloto}</div>
                        <div class="team-name">{equipo}</div>
                    </div>
                </div>
                <div class="points-earned">
                    {puntos} pts {'(Sprint)' if es_sprint else ''}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Mostrar el podio destacado solo si hay al menos 3 pilotos
    podio_actual = resultados_actuales[:3]
    if len(podio_actual) >= 3:
        evento_nombre = "🏃‍♂️ Sprint" if es_sprint else "🏁 Carrera Principal"
        st.markdown(f"#### 🏆 Podio {evento_nombre}")
        col1, col2, col3 = st.columns(3)
        
        # Segundo lugar (izquierda)
        with col1:
            if len(podio_actual) > 1:
                piloto_2, _ = podio_actual[1]
                emoji_pais_2 = pilotos_equipos[piloto_2]["emoji"]
                equipo_2 = pilotos_equipos[piloto_2]["equipo"]
                puntos_2 = sistema_puntos.get(2, 0)
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #C0C0C0, #A9A9A9); 
                            padding: 15px; border-radius: 10px; text-align: center; 
                            height: 120px; display: flex; flex-direction: column; 
                            justify-content: center;">
                    <div style="font-size: 2em;">🥈</div>
                    <div style="font-weight: bold; color: #2c3e50;">{emoji_pais_2} {piloto_2}</div>
                    <div style="font-size: 0.8em; color: #7f8c8d;">{equipo_2}</div>
                    <div style="font-size: 0.9em; color: #e74c3c;">{puntos_2} pts</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Primer lugar (centro, más alto)
        with col2:
            piloto_1, _ = podio_actual[0]
            emoji_pais_1 = pilotos_equipos[piloto_1]["emoji"]
            equipo_1 = pilotos_equipos[piloto_1]["equipo"]
            puntos_1 = sistema_puntos.get(1, 0)
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #FFD700, #FFA500); 
                        padding: 20px; border-radius: 10px; text-align: center; 
                        height: 140px; display: flex; flex-direction: column; 
                        justify-content: center; margin-top: -10px;">
                <div style="font-size: 2.5em;">🥇</div>
                <div style="font-weight: bold; color: #2c3e50; font-size: 1.1em;">{emoji_pais_1} {piloto_1}</div>
                <div style="font-size: 0.8em; color: #7f8c8d;">{equipo_1}</div>
                <div style="font-size: 0.9em; color: #e74c3c;">{puntos_1} pts</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Tercer lugar (derecha)
        with col3:
            if len(podio_actual) > 2:
                piloto_3, _ = podio_actual[2]
                emoji_pais_3 = pilotos_equipos[piloto_3]["emoji"]
                equipo_3 = pilotos_equipos[piloto_3]["equipo"]
                puntos_3 = sistema_puntos.get(3, 0)
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #CD7F32, #B8860B); 
                            padding: 15px; border-radius: 10px; text-align: center; 
                            height: 120px; display: flex; flex-direction: column; 
                            justify-content: center;">
                    <div style="font-size: 2em;">🥉</div>
                    <div style="font-weight: bold; color: #2c3e50;">{emoji_pais_3} {piloto_3}</div>
                    <div style="font-size: 0.8em; color: #7f8c8d;">{equipo_3}</div>
                    <div style="font-size: 0.9em; color: #e74c3c;">{puntos_3} pts</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Estadísticas rápidas de la carrera
    if len(resultados_actuales) > 0:
        evento_nombre = "Sprint" if es_sprint else "Carrera"
        st.markdown(f"#### 📊 Estadísticas del {evento_nombre}")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            ganador = resultados_actuales[0][0]
            puntos_ganador = sistema_puntos.get(1, 0)
            st.metric("🏆 Ganador", ganador, f"{puntos_ganador} pts")
        
        with col2:
            max_puntos = 10 if not es_sprint else 8
            pilotos_puntos = [piloto for piloto, pos in resultados_actuales if pos <= max_puntos]
            zona_text = "Top 10" if not es_sprint else "Top 8"
            st.metric("🎯 Pilotos en Puntos", len(pilotos_puntos), zona_text)
        
        with col3:
            equipos_representados = len(set([pilotos_equipos[piloto]["equipo"] for piloto, _ in resultados_actuales]))
            st.metric("🏎️ Equipos", equipos_representados, "participantes")
        
        with col4:
            total_puntos = sum([sistema_puntos.get(pos, 0) for _, pos in resultados_actuales])
            tipo_puntos = "Sprint" if es_sprint else "Carrera"
            st.metric("📈 Puntos Totales", total_puntos, f"{tipo_puntos}")

# -----------------------------
# �🏆 DASHBOARD PRINCIPAL
# -----------------------------
if seccion == "🏆 Dashboard Principal":
    
    # CSS adicional para el dashboard mejorado
    st.markdown("""
    <style>
    .dashboard-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    .champion-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 25px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 15px 0;
        box-shadow: 0 15px 35px rgba(255, 87, 108, 0.3);
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
        margin: 20px 0;
    }
    .stat-item {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        color: #2c3e50;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .progress-ring {
        width: 120px;
        height: 120px;
        margin: 0 auto;
    }
    .recent-winner {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 8px 25px rgba(252, 182, 159, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Hero Section - Información principal del campeonato
    if clasificacion:
        lider = max(clasificacion.items(), key=lambda x: x[1])
        lider_emoji = pilotos_equipos[lider[0]]["emoji"]
        lider_equipo = pilotos_equipos[lider[0]]["equipo"]
        
        st.markdown(f"""
        <div class="champion-card">
            <h1>👑 LÍDER DEL CAMPEONATO</h1>
            <h2>{lider_emoji} {lider[0]}</h2>
            <h3>{lider_equipo}</h3>
            <h1 style="font-size: 3em; margin: 10px 0;">{lider[1]} PUNTOS</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # Métricas principales mejoradas
    st.markdown("### 📊 Estadísticas de la Temporada")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_carreras = len([r for r in resultados.keys()])
        progreso_temporada = (total_carreras / len(calendario)) * 100
        st.markdown(f"""
        <div class="dashboard-card">
            <h3>🏁</h3>
            <h2>{total_carreras}</h2>
            <p>Carreras Completadas</p>
            <small>{progreso_temporada:.1f}% de la temporada</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if clasificacion_equipos:
            equipo_lider = max(clasificacion_equipos.items(), key=lambda x: x[1])
            st.markdown(f"""
            <div class="dashboard-card">
                <h3>🏆</h3>
                <h2>{equipo_lider[0]}</h2>
                <p>Equipo Líder</p>
                <small>{equipo_lider[1]} puntos</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="dashboard-card">
                <h3>🏆</h3>
                <h2>N/A</h2>
                <p>Equipo Líder</p>
                <small>0 puntos</small>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        carreras_restantes = len(calendario) - total_carreras
        st.markdown(f"""
        <div class="dashboard-card">
            <h3>📅</h3>
            <h2>{carreras_restantes}</h2>
            <p>Carreras Restantes</p>
            <small>Quedan por disputar</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        if resultados:
            total_puntos_repartidos = sum(sum(puntos_por_posicion.get(pos, 0) for _, pos in ronda) for ronda in resultados.values())
            st.markdown(f"""
            <div class="dashboard-card">
                <h3>📈</h3>
                <h2>{total_puntos_repartidos}</h2>
                <p>Puntos Repartidos</p>
                <small>En toda la temporada</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="dashboard-card">
                <h3>📈</h3>
                <h2>0</h2>
                <p>Puntos Repartidos</p>
                <small>En toda la temporada</small>
            </div>
            """, unsafe_allow_html=True)
    
    if resultados:
        # Última carrera disputada
        ultima_ronda = max(resultados.keys())
        nombre_ultima_carrera = calendario[ultima_ronda-1]['gran_premio']
        circuito_ultima_carrera = calendario[ultima_ronda-1]['circuito']
        resultados_ultima = sorted(resultados[ultima_ronda], key=lambda x: x[1])
        ganador_ultima = resultados_ultima[0][0]
        emoji_ganador = pilotos_equipos[ganador_ultima]["emoji"]
        
        st.markdown("### 🏁 Última Carrera Disputada")
        st.markdown(f"""
        <div class="recent-winner">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h3>🏎️ GP {nombre_ultima_carrera} - {circuito_ultima_carrera}</h3>
                    <h4>🏆 Ganador: {emoji_ganador} {ganador_ultima}</h4>
                    <p>Ronda {ultima_ronda} de {len(calendario)}</p>
                </div>
                <div style="font-size: 4em;">🏁</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Gráficos principales con mejor layout
        st.markdown("### 📈 Análisis Visual")
        
        # Primera fila de gráficos
        col1, col2 = st.columns([3, 2])
        
        with col1:
            fig_evolucion = crear_grafico_evolucion(resultados)
            if fig_evolucion:
                st.plotly_chart(fig_evolucion, use_container_width=True)
        
        with col2:
            # Top 5 pilotos mejorado
            st.markdown("#### 🥇 Top 5 Pilotos")
            clasificacion_ordenada = sorted(clasificacion.items(), key=lambda x: x[1], reverse=True)[:5]
            
            for i, (piloto, puntos) in enumerate(clasificacion_ordenada, 1):
                emoji_pos = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}º")
                emoji_pais = pilotos_equipos[piloto]["emoji"]
                equipo = pilotos_equipos[piloto]["equipo"]
                color_equipo = pilotos_equipos[piloto]["color"]
                
                # Calcular la diferencia con el líder
                diferencia = clasificacion_ordenada[0][1] - puntos if i > 1 else 0
                diferencia_text = f"-{diferencia}" if diferencia > 0 else "Líder"
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {color_equipo}22, {color_equipo}11); 
                           border-left: 4px solid {color_equipo}; padding: 12px; margin: 8px 0; 
                           border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <strong style="font-size: 1.1em;">{emoji_pos} {emoji_pais} {piloto}</strong><br>
                            <small style="color: #666;">{equipo}</small>
                        </div>
                        <div style="text-align: right;">
                            <strong style="color: {color_equipo}; font-size: 1.3em;">{puntos}</strong><br>
                            <small style="color: #888;">{diferencia_text}</small>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Segunda fila de gráficos
        col1, col2 = st.columns(2)
        
        with col1:
            fig_clasificacion = crear_grafico_clasificacion(clasificacion)
            if fig_clasificacion:
                st.plotly_chart(fig_clasificacion, use_container_width=True)
        
        with col2:
            fig_equipos = crear_grafico_equipos(clasificacion_equipos)
            if fig_equipos:
                st.plotly_chart(fig_equipos, use_container_width=True)
        
        # Estadísticas adicionales
        st.markdown("### 🏆 Estadísticas Destacadas")
        
        # Calcular estadísticas interesantes
        victorias = {}
        podios = {}
        for ronda_resultados in resultados.values():
            ganador = min(ronda_resultados, key=lambda x: x[1])[0]
            victorias[ganador] = victorias.get(ganador, 0) + 1
            
            top3 = sorted(ronda_resultados, key=lambda x: x[1])[:3]
            for piloto, _ in top3:
                podios[piloto] = podios.get(piloto, 0) + 1
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if victorias:
                max_wins = max(victorias.values())
                pilotos_mas_ganadores = [p for p, w in victorias.items() if w == max_wins]
                piloto_dominante = pilotos_mas_ganadores[0]
                emoji_dominante = pilotos_equipos[piloto_dominante]["emoji"]
                
                st.markdown(f"""
                <div class="stat-item">
                    <h3>🏆 Más Victorias</h3>
                    <h2>{emoji_dominante} {piloto_dominante}</h2>
                    <p>{max_wins} victoria{'s' if max_wins != 1 else ''}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            if podios:
                max_podios = max(podios.values())
                piloto_mas_podios = max(podios.items(), key=lambda x: x[1])[0]
                emoji_podios = pilotos_equipos[piloto_mas_podios]["emoji"]
                
                st.markdown(f"""
                <div class="stat-item">
                    <h3>🥇 Más Podios</h3>
                    <h2>{emoji_podios} {piloto_mas_podios}</h2>
                    <p>{max_podios} podio{'s' if max_podios != 1 else ''}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col3:
            # Equipo más consistente
            if clasificacion_equipos:
                equipo_consistente = max(clasificacion_equipos.items(), key=lambda x: x[1])[0]
                puntos_consistente = clasificacion_equipos[equipo_consistente]
                
                st.markdown(f"""
                <div class="stat-item">
                    <h3>⚡ Más Consistente</h3>
                    <h2>{equipo_consistente}</h2>
                    <p>{puntos_consistente} puntos totales</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Próxima carrera con countdown visual
        proxima_carrera = None
        for carrera in calendario:
            if carrera["ronda"] not in resultados:
                proxima_carrera = carrera
                break
        
        if proxima_carrera:
            st.markdown("### 🔮 Próxima Carrera")
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                       padding: 25px; border-radius: 20px; color: white; text-align: center;
                       margin: 20px 0; box-shadow: 0 15px 35px rgba(79, 172, 254, 0.3);">
                <h2>�️ GP {proxima_carrera['gran_premio']}</h2>
                <h3>📍 {proxima_carrera['circuito']}</h3>
                <h4>📅 {proxima_carrera['fecha_completa']}</h4>
                <h3>�🏁 Carrera: {proxima_carrera['fecha']}</h3>
            </div>
            """, unsafe_allow_html=True)
    
    else:
        # Estado inicial cuando no hay resultados
        st.markdown("""
        <div style="text-align: center; padding: 50px; color: #666;">
            <div style="font-size: 8em;">🏎️</div>
            <h2>¡Bienvenido a la Temporada 2025 de F1!</h2>
            <p style="font-size: 1.2em;">No hay resultados registrados aún.</p>
            <p>Comienza agregando los resultados de las carreras en la sección "📥 Gestión de Resultados"</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Mostrar calendario de próximas carreras
        st.markdown("### 🗓️ Próximas Carreras")
        for i, carrera in enumerate(calendario[:5]):  # Mostrar las primeras 5 carreras
            st.markdown(f"""
            <div style="background: #f8f9fa; padding: 15px; margin: 10px 0; 
                       border-radius: 10px; border-left: 4px solid #3498db;">
                <strong>Ronda {carrera['ronda']}: {carrera['gran_premio']}</strong><br>
                <small>📍 {carrera['circuito']} | 📅 {carrera['fecha_completa']}</small>
            </div>
            """, unsafe_allow_html=True)

# -----------------------------
# 📊 ANÁLISIS DETALLADO
# -----------------------------
elif seccion == "📊 Análisis Detallado":
    st.header("📊 Análisis Detallado del Campeonato")
    
    if resultados:
        # Selector de carrera para análisis
        carreras_completadas = list(resultados.keys())
        if carreras_completadas:
            carrera_seleccionada = st.selectbox(
                "🏁 Selecciona una carrera para análisis:",
                carreras_completadas,
                format_func=lambda x: f"Ronda {x}: {calendario[x-1]['gran_premio']}"
            )
            
            if carrera_seleccionada in resultados:
                st.subheader(f"🏆 Resultados de la Ronda {carrera_seleccionada}: {calendario[carrera_seleccionada-1]['gran_premio']}")
                
                # Crear DataFrame para la carrera
                resultados_carrera = resultados[carrera_seleccionada]
                df_carrera = []
                for piloto, posicion in sorted(resultados_carrera, key=lambda x: x[1]):
                    puntos = puntos_por_posicion.get(posicion, 0)
                    df_carrera.append({
                        'Posición': posicion,
                        'Piloto': f"{pilotos_equipos[piloto]['emoji']} {piloto}",
                        'Equipo': pilotos_equipos[piloto]['equipo'],
                        'Puntos': puntos
                    })
                
                df_display = pd.DataFrame(df_carrera)
                st.dataframe(df_display, use_container_width=True, hide_index=True)
                
                # Podio especial
                podio = sorted(resultados_carrera, key=lambda x: x[1])[:3]
                st.subheader("🥇 Podio de la Carrera")
                
                col1, col2, col3 = st.columns(3)
                for i, (col, (piloto, _)) in enumerate(zip([col2, col1, col3], podio), 1):
                    with col:
                        emoji_pos = {1: "🥇", 2: "🥈", 3: "🥉"}[i]
                        emoji_pais = pilotos_equipos[piloto]["emoji"]
                        st.markdown(f"""
                        <div class="podium-card">
                            <h2>{emoji_pos}</h2>
                            <h3>{emoji_pais} {piloto}</h3>
                            <p>{pilotos_equipos[piloto]['equipo']}</p>
                        </div>
                        """, unsafe_allow_html=True)
        
        # Estadísticas adicionales mejoradas
        st.subheader("📈 Estadísticas Generales de la Temporada")
        
        # Métricas principales en cards
        col1, col2, col3, col4 = st.columns(4)
        
        total_carreras = len(resultados)
        total_carreras_sprint = len(resultados_sprint)
        total_pilotos_activos = len(set([piloto for ronda_res in resultados.values() for piloto, _ in ronda_res]))
        
        with col1:
            st.metric("🏁 Carreras Completadas", total_carreras, f"de {len(calendario)}")
        with col2:
            st.metric("🏃‍♂️ Carreras Sprint", total_carreras_sprint, f"de 6 programadas")
        with col3:
            st.metric("👥 Pilotos Activos", total_pilotos_activos, "en temporada")
        with col4:
            puntos_totales_temporada = sum(clasificacion.values())
            st.metric("📊 Puntos Totales", puntos_totales_temporada, "otorgados")
        
        # Sección de estadísticas detalladas
        st.markdown("---")
        
        # Pestañas para diferentes análisis
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏆 Victorias & Podios", "📊 Análisis de Rendimiento", "🏎️ Estadísticas por Equipo", "🎯 Récords & Racha", "📈 Tendencias"])
        
        with tab1:
            col1, col2 = st.columns(2)
            
            with col1:
                # Victorias por piloto (mejorado)
                victorias = {}
                victorias_sprint = {}
                
                # Contar victorias en carreras principales
                for ronda_resultados in resultados.values():
                    ganador = min(ronda_resultados, key=lambda x: x[1])[0]
                    victorias[ganador] = victorias.get(ganador, 0) + 1
                
                # Contar victorias en sprints
                for ronda_resultados in resultados_sprint.values():
                    ganador = min(ronda_resultados, key=lambda x: x[1])[0]
                    victorias_sprint[ganador] = victorias_sprint.get(ganador, 0) + 1
                
                if victorias:
                    st.markdown("### 🏆 Victorias por Piloto")
                    
                    # Crear DataFrame para mejor visualización
                    victorias_data = []
                    all_pilots = set(list(victorias.keys()) + list(victorias_sprint.keys()))
                    
                    for piloto in all_pilots:
                        main_wins = victorias.get(piloto, 0)
                        sprint_wins = victorias_sprint.get(piloto, 0)
                        total_wins = main_wins + sprint_wins
                        
                        if total_wins > 0:
                            emoji_pais = pilotos_equipos[piloto]["emoji"]
                            equipo = pilotos_equipos[piloto]["equipo"]
                            color_equipo = pilotos_equipos[piloto]["color"]
                            
                            victorias_data.append({
                                'piloto': piloto,
                                'emoji': emoji_pais,
                                'equipo': equipo,
                                'color': color_equipo,
                                'main_wins': main_wins,
                                'sprint_wins': sprint_wins,
                                'total_wins': total_wins
                            })
                    
                    # Ordenar por total de victorias
                    victorias_data.sort(key=lambda x: x['total_wins'], reverse=True)
                    
                    for data in victorias_data[:8]:  # Top 8
                        main_text = f"{data['main_wins']} principal{'es' if data['main_wins'] != 1 else ''}" if data['main_wins'] > 0 else ""
                        sprint_text = f"{data['sprint_wins']} sprint{'s' if data['sprint_wins'] != 1 else ''}" if data['sprint_wins'] > 0 else ""
                        detail_text = " + ".join(filter(None, [main_text, sprint_text]))
                        
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {data['color']}22, {data['color']}11); 
                                   border-left: 4px solid {data['color']}; padding: 10px; margin: 5px 0; 
                                   border-radius: 8px;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <strong>{data['emoji']} {data['piloto']}</strong><br>
                                    <small style="color: #666;">{data['equipo']}</small>
                                </div>
                                <div style="text-align: right;">
                                    <strong style="color: {data['color']}; font-size: 1.2em;">{data['total_wins']}</strong><br>
                                    <small style="color: #888;">{detail_text}</small>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
            
            with col2:
                # Podios por piloto (mejorado)
                podios = {}
                podios_sprint = {}
                
                # Contar podios en carreras principales
                for ronda_resultados in resultados.values():
                    top3 = sorted(ronda_resultados, key=lambda x: x[1])[:3]
                    for piloto, _ in top3:
                        podios[piloto] = podios.get(piloto, 0) + 1
                
                # Contar podios en sprints
                for ronda_resultados in resultados_sprint.values():
                    top3 = sorted(ronda_resultados, key=lambda x: x[1])[:3]
                    for piloto, _ in top3:
                        podios_sprint[piloto] = podios_sprint.get(piloto, 0) + 1
                
                if podios:
                    st.markdown("### 🥇 Podios por Piloto")
                    
                    # Crear DataFrame para podios
                    podios_data = []
                    all_pilots = set(list(podios.keys()) + list(podios_sprint.keys()))
                    
                    for piloto in all_pilots:
                        main_podiums = podios.get(piloto, 0)
                        sprint_podiums = podios_sprint.get(piloto, 0)
                        total_podiums = main_podiums + sprint_podiums
                        
                        if total_podiums > 0:
                            emoji_pais = pilotos_equipos[piloto]["emoji"]
                            equipo = pilotos_equipos[piloto]["equipo"]
                            color_equipo = pilotos_equipos[piloto]["color"]
                            
                            podios_data.append({
                                'piloto': piloto,
                                'emoji': emoji_pais,
                                'equipo': equipo,
                                'color': color_equipo,
                                'main_podiums': main_podiums,
                                'sprint_podiums': sprint_podiums,
                                'total_podiums': total_podiums
                            })
                    
                    # Ordenar por total de podios
                    podios_data.sort(key=lambda x: x['total_podiums'], reverse=True)
                    
                    for data in podios_data[:10]:  # Top 10
                        main_text = f"{data['main_podiums']} principal{'es' if data['main_podiums'] != 1 else ''}" if data['main_podiums'] > 0 else ""
                        sprint_text = f"{data['sprint_podiums']} sprint{'s' if data['sprint_podiums'] != 1 else ''}" if data['sprint_podiums'] > 0 else ""
                        detail_text = " + ".join(filter(None, [main_text, sprint_text]))
                        
                        # Calcular porcentaje de podios
                        total_races_available = total_carreras + total_carreras_sprint
                        podium_percentage = (data['total_podiums'] / total_races_available * 100) if total_races_available > 0 else 0
                        
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {data['color']}22, {data['color']}11); 
                                   border-left: 4px solid {data['color']}; padding: 10px; margin: 5px 0; 
                                   border-radius: 8px;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <strong>{data['emoji']} {data['piloto']}</strong><br>
                                    <small style="color: #666;">{data['equipo']}</small>
                                </div>
                                <div style="text-align: right;">
                                    <strong style="color: {data['color']}; font-size: 1.2em;">{data['total_podiums']}</strong><br>
                                    <small style="color: #888;">{podium_percentage:.1f}% ratio</small>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
        
        with tab2:
            # Análisis de rendimiento avanzado
            st.markdown("### 📊 Análisis de Rendimiento")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🎯 Consistencia (Top 10)")
                
                # Calcular consistencia en puntos
                top10_finishes = {}
                for ronda_resultados in resultados.values():
                    for piloto, posicion in ronda_resultados:
                        if posicion <= 10:
                            top10_finishes[piloto] = top10_finishes.get(piloto, 0) + 1
                
                # Agregar finishes de sprint
                for ronda_resultados in resultados_sprint.values():
                    for piloto, posicion in ronda_resultados:
                        if posicion <= 8:  # Top 8 en sprint dan puntos
                            top10_finishes[piloto] = top10_finishes.get(piloto, 0) + 1
                
                if top10_finishes:
                    consistencia_data = []
                    for piloto, finishes in top10_finishes.items():
                        total_races = sum(1 for ronda_res in resultados.values() for p, _ in ronda_res if p == piloto)
                        total_races += sum(1 for ronda_res in resultados_sprint.values() for p, _ in ronda_res if p == piloto)
                        
                        if total_races > 0:
                            consistency_rate = (finishes / total_races) * 100
                            emoji_pais = pilotos_equipos[piloto]["emoji"]
                            color_equipo = pilotos_equipos[piloto]["color"]
                            
                            consistencia_data.append({
                                'piloto': piloto,
                                'emoji': emoji_pais,
                                'color': color_equipo,
                                'finishes': finishes,
                                'total_races': total_races,
                                'consistency_rate': consistency_rate
                            })
                    
                    # Ordenar por tasa de consistencia
                    consistencia_data.sort(key=lambda x: x['consistency_rate'], reverse=True)
                    
                    for data in consistencia_data[:8]:
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {data['color']}15, {data['color']}08); 
                                   border-left: 3px solid {data['color']}; padding: 8px; margin: 4px 0; 
                                   border-radius: 6px;">
                            <strong>{data['emoji']} {data['piloto']}</strong><br>
                            <span style="color: {data['color']}; font-weight: bold;">{data['consistency_rate']:.1f}%</span>
                            <small style="color: #666;"> ({data['finishes']}/{data['total_races']} carreras)</small>
                        </div>
                        """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("#### 📈 Promedio de Posición")
                
                # Calcular promedio de posición
                posicion_promedio = {}
                for piloto in pilotos_titulares:
                    posiciones = []
                    
                    # Posiciones en carreras principales
                    for ronda_resultados in resultados.values():
                        for p, pos in ronda_resultados:
                            if p == piloto:
                                posiciones.append(pos)
                    
                    # Posiciones en sprints
                    for ronda_resultados in resultados_sprint.values():
                        for p, pos in ronda_resultados:
                            if p == piloto:
                                posiciones.append(pos)
                    
                    if posiciones:
                        promedio = sum(posiciones) / len(posiciones)
                        posicion_promedio[piloto] = {
                            'promedio': promedio,
                            'carreras': len(posiciones),
                            'mejor': min(posiciones),
                            'peor': max(posiciones)
                        }
                
                if posicion_promedio:
                    # Ordenar por mejor promedio
                    sorted_promedio = sorted(posicion_promedio.items(), key=lambda x: x[1]['promedio'])
                    
                    for piloto, stats in sorted_promedio[:8]:
                        emoji_pais = pilotos_equipos[piloto]["emoji"]
                        color_equipo = pilotos_equipos[piloto]["color"]
                        
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {color_equipo}15, {color_equipo}08); 
                                   border-left: 3px solid {color_equipo}; padding: 8px; margin: 4px 0; 
                                   border-radius: 6px;">
                            <strong>{emoji_pais} {piloto}</strong><br>
                            <span style="color: {color_equipo}; font-weight: bold;">P{stats['promedio']:.1f}</span>
                            <small style="color: #666;"> (mejor: P{stats['mejor']}, peor: P{stats['peor']})</small>
                        </div>
                        """, unsafe_allow_html=True)
        
        with tab3:
            # Estadísticas por equipo
            st.markdown("### 🏎️ Clasificación de Constructores")
            
            if clasificacion_equipos:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("#### 🏆 Puntos por Equipo")
                    for i, (equipo, puntos) in enumerate(sorted(clasificacion_equipos.items(), key=lambda x: x[1], reverse=True), 1):
                        # Buscar color del equipo
                        color_equipo = next((data["color"] for data in pilotos_equipos.values() if data["equipo"] == equipo), "#666")
                        
                        # Calcular diferencia con el líder
                        lider_puntos = max(clasificacion_equipos.values())
                        diferencia = lider_puntos - puntos if i > 1 else 0
                        diferencia_text = f"-{diferencia}" if diferencia > 0 else "Líder"
                        
                        # Iconos de posición
                        emoji_pos = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}º")
                        
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {color_equipo}22, {color_equipo}11); 
                                   border-left: 4px solid {color_equipo}; padding: 12px; margin: 8px 0; 
                                   border-radius: 8px;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <strong style="font-size: 1.1em;">{emoji_pos} {equipo}</strong>
                                </div>
                                <div style="text-align: right;">
                                    <strong style="color: {color_equipo}; font-size: 1.3em;">{puntos}</strong><br>
                                    <small style="color: #888;">{diferencia_text}</small>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("#### 📊 Estadísticas por Equipo")
                    
                    # Calcular estadísticas detalladas por equipo
                    equipos_stats = {}
                    
                    for equipo in set(data["equipo"] for data in pilotos_equipos.values()):
                        pilotos_equipo = [piloto for piloto, data in pilotos_equipos.items() if data["equipo"] == equipo and piloto in pilotos_titulares]
                        
                        stats = {
                            'victorias': 0,
                            'podios': 0,
                            'puntos_scored': 0,
                            'mejor_posicion': 21
                        }
                        
                        # Contar estadísticas en carreras principales
                        for ronda_resultados in resultados.values():
                            for piloto, posicion in ronda_resultados:
                                if piloto in pilotos_equipo:
                                    if posicion == 1:
                                        stats['victorias'] += 1
                                    if posicion <= 3:
                                        stats['podios'] += 1
                                    if posicion <= 10:
                                        stats['puntos_scored'] += 1
                                    stats['mejor_posicion'] = min(stats['mejor_posicion'], posicion)
                        
                        # Contar estadísticas en sprints
                        for ronda_resultados in resultados_sprint.values():
                            for piloto, posicion in ronda_resultados:
                                if piloto in pilotos_equipo:
                                    if posicion == 1:
                                        stats['victorias'] += 1
                                    if posicion <= 3:
                                        stats['podios'] += 1
                                    if posicion <= 8:
                                        stats['puntos_scored'] += 1
                                    stats['mejor_posicion'] = min(stats['mejor_posicion'], posicion)
                        
                        if stats['mejor_posicion'] == 21:
                            stats['mejor_posicion'] = '-'
                        
                        equipos_stats[equipo] = stats
                    
                    # Mostrar estadísticas
                    for equipo, stats in sorted(equipos_stats.items(), key=lambda x: equipos_stats.get(x[0], {}).get('victorias', 0), reverse=True):
                        color_equipo = next((data["color"] for data in pilotos_equipos.values() if data["equipo"] == equipo), "#666")
                        
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {color_equipo}15, {color_equipo}08); 
                                   border: 1px solid {color_equipo}; padding: 10px; margin: 6px 0; 
                                   border-radius: 6px;">
                            <strong style="color: {color_equipo};">{equipo}</strong><br>
                            <small>
                                🏆 {stats['victorias']} victorias | 🥇 {stats['podios']} podios<br>
                                🎯 {stats['puntos_scored']} en puntos | 📈 Mejor: P{stats['mejor_posicion']}
                            </small>
                        </div>
                        """, unsafe_allow_html=True)
        
        with tab4:
            # Récords y rachas
            st.markdown("### 🎯 Récords y Rachas de la Temporada")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🔥 Rachas Actuales")
                
                # Calcular racha de podios actual
                rachas_podios = {}
                for piloto in pilotos_titulares:
                    racha_actual = 0
                    
                    # Verificar las últimas carreras en orden
                    rondas_ordenadas = sorted(resultados.keys(), reverse=True)
                    
                    for ronda in rondas_ordenadas:
                        if ronda in resultados:
                            piloto_en_carrera = False
                            en_podio = False
                            
                            for p, pos in resultados[ronda]:
                                if p == piloto:
                                    piloto_en_carrera = True
                                    if pos <= 3:
                                        en_podio = True
                                    break
                            
                            if piloto_en_carrera:
                                if en_podio:
                                    racha_actual += 1
                                else:
                                    break
                    
                    if racha_actual > 0:
                        rachas_podios[piloto] = racha_actual
                
                if rachas_podios:
                    st.write("**🥇 Racha de Podios:**")
                    for piloto, racha in sorted(rachas_podios.items(), key=lambda x: x[1], reverse=True)[:5]:
                        emoji_pais = pilotos_equipos[piloto]["emoji"]
                        color_equipo = pilotos_equipos[piloto]["color"]
                        st.markdown(f"• **{emoji_pais} {piloto}**: {racha} carreras consecutivas")
                
                # Racha de puntos
                st.markdown("**🎯 Racha de Puntos:**")
                rachas_puntos = {}
                for piloto in pilotos_titulares:
                    racha_actual = 0
                    
                    rondas_ordenadas = sorted(resultados.keys(), reverse=True)
                    
                    for ronda in rondas_ordenadas:
                        if ronda in resultados:
                            piloto_en_carrera = False
                            en_puntos = False
                            
                            for p, pos in resultados[ronda]:
                                if p == piloto:
                                    piloto_en_carrera = True
                                    if pos <= 10:
                                        en_puntos = True
                                    break
                            
                            if piloto_en_carrera:
                                if en_puntos:
                                    racha_actual += 1
                                else:
                                    break
                    
                    if racha_actual > 0:
                        rachas_puntos[piloto] = racha_actual
                
                if rachas_puntos:
                    for piloto, racha in sorted(rachas_puntos.items(), key=lambda x: x[1], reverse=True)[:5]:
                        emoji_pais = pilotos_equipos[piloto]["emoji"]
                        st.markdown(f"• **{emoji_pais} {piloto}**: {racha} carreras consecutivas")
            
            with col2:
                st.markdown("#### 🏆 Récords de la Temporada")
                
                # Mejores actuaciones por carrera
                if resultados:
                    # Ganador con más pole positions (simulado con primera posición)
                    poles = {}
                    for ronda_resultados in resultados.values():
                        if ronda_resultados:
                            # Simulamos que el ganador tuvo pole
                            ganador = min(ronda_resultados, key=lambda x: x[1])[0]
                            poles[ganador] = poles.get(ganador, 0) + 1
                    
                    if poles:
                        top_pole = max(poles.items(), key=lambda x: x[1])
                        emoji_pais = pilotos_equipos[top_pole[0]]["emoji"]
                        st.markdown(f"**🏎️ Más Poles (simulado):**\n{emoji_pais} {top_pole[0]} - {top_pole[1]} poles")
                    
                    # Mejor debut (primer piloto en lograr podio)
                    debuts_podio = {}
                    for ronda in sorted(resultados.keys()):
                        top3 = sorted(resultados[ronda], key=lambda x: x[1])[:3]
                        for piloto, pos in top3:
                            if piloto not in debuts_podio:
                                debuts_podio[piloto] = ronda
                    
                    if debuts_podio:
                        primer_podio = min(debuts_podio.items(), key=lambda x: x[1])
                        emoji_pais = pilotos_equipos[primer_podio[0]]["emoji"]
                        st.markdown(f"**🌟 Primer Podio:**\n{emoji_pais} {primer_podio[0]} (Ronda {primer_podio[1]})")
                    
                    # Carrera con más adelantamientos (variabilidad en posiciones)
                    variabilidad_rondas = {}
                    for ronda, resultados_ronda in resultados.items():
                        posiciones = [pos for _, pos in resultados_ronda]
                        if len(posiciones) > 10:
                            # Calcular variabilidad como dispersión de posiciones top 10
                            top10_pos = sorted(posiciones)[:10]
                            variabilidad = max(top10_pos) - min(top10_pos)
                            variabilidad_rondas[ronda] = variabilidad
                    
                    if variabilidad_rondas:
                        carrera_mas_variada = max(variabilidad_rondas.items(), key=lambda x: x[1])
                        st.markdown(f"**🎢 Carrera Más Disputada:**\nRonda {carrera_mas_variada[0]} (variabilidad: {carrera_mas_variada[1]})")
        
        with tab5:
            # Tendencias y proyecciones
            st.markdown("### 📈 Tendencias de la Temporada")
            
            if len(resultados) >= 3:
                # Análisis de tendencias de puntos
                st.markdown("#### 📊 Evolución de Puntos por Piloto")
                
                # Crear gráfico de evolución mejorado
                fig_tendencias = crear_grafico_evolucion_detallado(resultados, resultados_sprint)
                if fig_tendencias:
                    st.plotly_chart(fig_tendencias, use_container_width=True)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("#### 🔥 Pilotos en Forma")
                    
                    # Calcular tendencia reciente (últimas 3 carreras)
                    ultimas_rondas = sorted(resultados.keys())[-3:]
                    tendencias = {}
                    
                    for piloto in pilotos_titulares:
                        puntos_recientes = []
                        for ronda in ultimas_rondas:
                            if ronda in resultados:
                                for p, pos in resultados[ronda]:
                                    if p == piloto:
                                        puntos_recientes.append(puntos_por_posicion.get(pos, 0))
                                        break
                        
                        if len(puntos_recientes) >= 2:
                            # Tendencia simple: comparar últimas carreras
                            tendencia = sum(puntos_recientes[-2:]) - sum(puntos_recientes[:-2]) if len(puntos_recientes) > 2 else puntos_recientes[-1]
                            tendencias[piloto] = tendencia
                    
                    # Mostrar pilotos con mejor tendencia
                    if tendencias:
                        for piloto, tend in sorted(tendencias.items(), key=lambda x: x[1], reverse=True)[:5]:
                            emoji_pais = pilotos_equipos[piloto]["emoji"]
                            color_equipo = pilotos_equipos[piloto]["color"]
                            if tend > 0:
                                st.markdown(f"📈 **{emoji_pais} {piloto}**: +{tend:.1f} pts (últimas carreras)")
                            elif tend < 0:
                                st.markdown(f"📉 **{emoji_pais} {piloto}**: {tend:.1f} pts (últimas carreras)")
                
                with col2:
                    st.markdown("#### 🎯 Proyección de Campeonato")
                    
                    # Proyección simple basada en tendencia actual
                    if clasificacion:
                        carreras_restantes = len(calendario) - total_carreras
                        
                        if carreras_restantes > 0:
                            st.write(f"**Carreras restantes: {carreras_restantes}**")
                            
                            # Calcular puntos promedio por carrera para top 5
                            top5_actual = sorted(clasificacion.items(), key=lambda x: x[1], reverse=True)[:5]
                            
                            for piloto, puntos_actuales in top5_actual:
                                if total_carreras > 0:
                                    promedio_por_carrera = puntos_actuales / total_carreras
                                    proyeccion = puntos_actuales + (promedio_por_carrera * carreras_restantes)
                                    
                                    emoji_pais = pilotos_equipos[piloto]["emoji"]
                                    color_equipo = pilotos_equipos[piloto]["color"]
                                    
                                    st.markdown(f"""
                                    <div style="background: linear-gradient(135deg, {color_equipo}15, {color_equipo}08); 
                                               border-left: 3px solid {color_equipo}; padding: 8px; margin: 4px 0; 
                                               border-radius: 6px;">
                                        <strong>{emoji_pais} {piloto}</strong><br>
                                        <span style="color: {color_equipo};">Proyección: {proyeccion:.0f} pts</span>
                                        <small style="color: #666;"> ({promedio_por_carrera:.1f} pts/carrera)</small>
                                    </div>
                                    """, unsafe_allow_html=True)
            else:
                st.info("📊 Se necesitan al menos 3 carreras para mostrar tendencias detalladas.")
    
    else:
        st.info("📊 No hay datos suficientes para mostrar análisis detallado.")

# -----------------------------
# 📥 GESTIÓN DE RESULTADOS
# -----------------------------
elif seccion == "📥 Gestión de Resultados":
    st.header("📥 Gestión de Resultados de Carreras")

    
    # Selección del GP
    opciones_gp = []
    for c in calendario:
        sprint_text = " 🐛 (Sprint)" if c['sprint'] else ""
        opciones_gp.append(f" 🚀 Ronda {c['ronda']}: {c['gran_premio']} - {c['circuito']} ({c['fecha_completa']}){sprint_text}")
    
    seleccion = st.selectbox("🏎️ Selecciona el Gran Premio:", opciones_gp)
    indice = opciones_gp.index(seleccion)
    ronda = calendario[indice]["ronda"]
    es_weekend_sprint = calendario[indice]["sprint"]
    
    # Verificar si ya hay resultados
    existen_resultados = ronda in resultados
    existen_resultados_sprint = ronda in resultados_sprint if es_weekend_sprint else False
    
    # Mostrar información sobre formato Sprint
    if es_weekend_sprint:
        st.info("🏃‍♂️ **Fin de semana Sprint**: Este Gran Premio incluye carrera Sprint el sábado y carrera principal el domingo.")
        
        # Selector de tipo de evento
        tipo_evento = st.radio(
            "Selecciona el evento a gestionar:",
            ["🏁 Carrera Principal (Domingo)", "🏃‍♂️ Carrera Sprint (Sábado)"],
            horizontal=True
        )
        
        es_sprint = "Sprint" in tipo_evento
        
        if es_sprint:
            modo = "🔄 Actualizar" if existen_resultados_sprint else "💾 Registrar"
            resultados_actuales_mostrar = resultados_sprint.get(ronda, [])
            sistema_puntos = puntos_sprint
            st.warning("⚠️ Carrera Sprint: Solo los primeros 8 puestos otorgan puntos (8-7-6-5-4-3-2-1)")
        else:
            modo = "🔄 Actualizar" if existen_resultados else "💾 Registrar"
            resultados_actuales_mostrar = resultados.get(ronda, [])
            sistema_puntos = puntos_por_posicion
    else:
        es_sprint = False
        modo = "🔄 Actualizar" if existen_resultados else "💾 Registrar"
        resultados_actuales_mostrar = resultados.get(ronda, [])
        sistema_puntos = puntos_por_posicion
    
    # Mostrar estado de resultados
    if es_weekend_sprint:
        estado_carrera = "✅ Registrada" if existen_resultados else "⏳ Pendiente"
        estado_sprint = "✅ Registrada" if existen_resultados_sprint else "⏳ Pendiente"
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🏁 Carrera Principal", estado_carrera)
        with col2:
            st.metric("🏃‍♂️ Carrera Sprint", estado_sprint)
    else:
        if existen_resultados:
            st.warning(f"⚠️ Ya hay resultados registrados para este GP. Puedes actualizarlos.")
        else:
            st.info(f"ℹ️ No hay resultados registrados aún para este GP.")
    
    # CSS adicional para los resultados actuales
    st.markdown("""
    <style>
    .result-card {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        border-left: 4px solid;
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s ease;
    }
    .result-card:hover {
        transform: translateX(5px);
    }
    .position-1 { border-left-color: #FFD700; background: linear-gradient(135deg, #FFF8DC, #FFFACD); }
    .position-2 { border-left-color: #C0C0C0; background: linear-gradient(135deg, #F5F5F5, #E8E8E8); }
    .position-3 { border-left-color: #CD7F32; background: linear-gradient(135deg, #FDF5E6, #F5DEB3); }
    .points-zone { border-left-color: #32CD32; }
    .no-points { border-left-color: #FF6B6B; }
    .sprint-points { border-left-color: #FF8C00; }
    .driver-name {
        font-size: 1.1em;
        font-weight: bold;
        color: #2c3e50;
    }
    .team-name {
        font-size: 0.9em;
        color: #7f8c8d;
        font-style: italic;
    }
    .points-earned {
        font-size: 1.2em;
        font-weight: bold;
        color: #e74c3c;
    }
    .position-number {
        font-size: 1.3em;
        font-weight: bold;
        color: #34495e;
    }
    </style>
    """, unsafe_allow_html=True)

    # Mostrar resultados existentes - Si es weekend Sprint, mostrar ambos
    resultados_carrera_main = resultados.get(ronda, [])
    resultados_sprint_main = resultados_sprint.get(ronda, [])
    
    if es_weekend_sprint and (resultados_carrera_main or resultados_sprint_main):
        st.subheader("📋 Resultados Actuales del Weekend")
        
        # Mostrar en columnas si ambos existen
        if resultados_carrera_main and resultados_sprint_main:
            col1, col2 = st.columns(2)
            
            # Columna Sprint
            with col1:
                st.markdown("### 🏃‍♂️ Carrera Sprint")
                mostrar_resultados_carrera(resultados_sprint_main, puntos_sprint, True)
            
            # Columna Carrera Principal
            with col2:
                st.markdown("### 🏁 Carrera Principal")
                mostrar_resultados_carrera(resultados_carrera_main, puntos_por_posicion, False)
        
        elif resultados_sprint_main:
            st.markdown("### 🏃‍♂️ Carrera Sprint")
            mostrar_resultados_carrera(resultados_sprint_main, puntos_sprint, True)
            
        elif resultados_carrera_main:
            st.markdown("### 🏁 Carrera Principal")
            mostrar_resultados_carrera(resultados_carrera_main, puntos_por_posicion, False)
            
    elif resultados_actuales_mostrar:
        evento_nombre = "🏃‍♂️ Sprint" if es_sprint else "🏁 Carrera Principal"
        st.subheader(f"📋 Resultados Actuales - {evento_nombre}")
        mostrar_resultados_carrera(resultados_actuales_mostrar, sistema_puntos, es_sprint)

    st.subheader(f"{modo} Resultados de la Carrera")
    
    # Formulario mejorado para 20 pilotos con parrilla de salida
    pilotos_resultado = []
    pilotos_usados = set()
    
    # Crear formulario en estilo parrilla de salida
    st.write("🏁 **Selecciona las posiciones de cada piloto (Parrilla de Salida):**")
    
    # CSS para la parrilla de salida
    st.markdown("""
    <style>
    .grid-position {
        background: linear-gradient(135deg, #f0f0f0, #e0e0e0);
        border: 2px solid #ccc;
        border-radius: 10px;
        padding: 10px;
        margin: 5px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .podium-position {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        border: 2px solid #FF8C00;
    }
    .points-position {
        background: linear-gradient(135deg, #98FB98, #90EE90);
        border: 2px solid #32CD32;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Crear la parrilla de 2 en 2
    for fila in range(10):  # 10 filas de 2 posiciones cada una
        col1, col2 = st.columns(2)
        
        # Posición izquierda (impares: 1, 3, 5, etc.)
        pos_izq = (fila * 2) + 1
        # Posición derecha (pares: 2, 4, 6, etc.)
        pos_der = (fila * 2) + 2
        
        with col1:
            opciones_disponibles = [""] + [p for p in pilotos_titulares if p not in pilotos_usados]
            
            # Valor por defecto si ya existe resultado
            valor_defecto = ""
            # Cargar del archivo correcto según el tipo de carrera
            resultados_a_usar = resultados_sprint.get(ronda, []) if es_sprint else resultados.get(ronda, [])
            if resultados_a_usar:
                for piloto_actual, pos_actual in resultados_a_usar:
                    if pos_actual == pos_izq:
                        valor_defecto = piloto_actual
                        break
            
            indice_defecto = 0
            if valor_defecto and valor_defecto in opciones_disponibles:
                indice_defecto = opciones_disponibles.index(valor_defecto)
            
            emoji_pos = {1: "🥇", 2: "🥈", 3: "🥉"}.get(pos_izq, f"{pos_izq}º")
            
            # Crear el contenedor visual para la posición
            if pos_izq <= 3:
                css_class = "podium-position"
            elif pos_izq <= 10:
                css_class = "points-position"
            else:
                css_class = "grid-position"
            
            st.markdown(f'<div class="grid-position {css_class}"><strong>P{pos_izq} {emoji_pos}</strong></div>', unsafe_allow_html=True)
            
            piloto_izq = st.selectbox(
                f"Posición {pos_izq}",
                opciones_disponibles,
                key=f"pos_{pos_izq}",
                index=indice_defecto,
                format_func=lambda x: f"{pilotos_equipos[x]['emoji']} {x}" if x else "Seleccionar piloto...",
                label_visibility="collapsed"
            )
            
            if piloto_izq:
                pilotos_resultado.append((piloto_izq, pos_izq))
                pilotos_usados.add(piloto_izq)
        
        with col2:
            opciones_disponibles = [""] + [p for p in pilotos_titulares if p not in pilotos_usados]
            
            # Valor por defecto si ya existe resultado
            valor_defecto = ""
            # Cargar del archivo correcto según el tipo de carrera
            resultados_a_usar = resultados_sprint.get(ronda, []) if es_sprint else resultados.get(ronda, [])
            if resultados_a_usar:
                for piloto_actual, pos_actual in resultados_a_usar:
                    if pos_actual == pos_der:
                        valor_defecto = piloto_actual
                        break
            
            indice_defecto = 0
            if valor_defecto and valor_defecto in opciones_disponibles:
                indice_defecto = opciones_disponibles.index(valor_defecto)
            
            emoji_pos = {1: "🥇", 2: "🥈", 3: "🥉"}.get(pos_der, f"{pos_der}º")
            
            # Crear el contenedor visual para la posición
            if pos_der <= 3:
                css_class = "podium-position"
            elif pos_der <= 10:
                css_class = "points-position"
            else:
                css_class = "grid-position"
            
            st.markdown(f'<div class="grid-position {css_class}"><strong>P{pos_der} {emoji_pos}</strong></div>', unsafe_allow_html=True)
            
            piloto_der = st.selectbox(
                f"Posición {pos_der}",
                opciones_disponibles,
                key=f"pos_{pos_der}",
                index=indice_defecto,
                format_func=lambda x: f"{pilotos_equipos[x]['emoji']} {x}" if x else "Seleccionar piloto...",
                label_visibility="collapsed"
            )
            
            if piloto_der:
                pilotos_resultado.append((piloto_der, pos_der))
                pilotos_usados.add(piloto_der)
    
    # Botón para guardar con estilo
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        evento_texto = f"🏃‍♂️ Sprint" if es_sprint else f"🏁 Carrera Principal"
        if st.button(f"{modo} Resultados {evento_texto}", type="primary", use_container_width=True):
            if len(set(p[0] for p in pilotos_resultado if p[0])) < 20:
                st.error("❌ Debes seleccionar 20 pilotos distintos para todas las posiciones.")
            else:
                # Determinar qué archivo usar
                archivo_usar = archivo_resultados_sprint if es_sprint else archivo_resultados
                
                # Cargar líneas existentes
                nuevas_lineas = []
                if os.path.exists(archivo_usar):
                    with open(archivo_usar, "r", encoding="utf-8") as f:
                        for linea in f:
                            r, piloto, posicion = linea.strip().split(",")
                            if int(r) != ronda:
                                nuevas_lineas.append(linea)
                
                # Agregar nuevos resultados para la ronda seleccionada
                for piloto, posicion in pilotos_resultado:
                    if piloto:  # Solo agregar si hay piloto seleccionado
                        nuevas_lineas.append(f"{ronda},{piloto},{posicion}\n")
                
                # Escribir el archivo completo actualizado
                with open(archivo_usar, "w", encoding="utf-8") as f:
                    f.writelines(nuevas_lineas)
                
                evento_guardado = "Sprint" if es_sprint else "Carrera Principal"
                existe_previo = existen_resultados_sprint if es_sprint else existen_resultados
                st.success(f"✅ Resultados del {evento_guardado} de la Ronda {ronda} {'actualizados' if existe_previo else 'guardados'} correctamente.")
                
                # Mostrar podio con estilo
                podio = sorted(pilotos_resultado, key=lambda x: x[1])[:3]
                st.subheader(f"🏆 Podio del {evento_guardado}")
                
                col1, col2, col3 = st.columns(3)
                for i, (col, (piloto, _)) in enumerate(zip([col2, col1, col3], podio), 1):
                    with col:
                        emoji_pos = {1: "🥇", 2: "🥈", 3: "🥉"}[i]
                        emoji_pais = pilotos_equipos[piloto]["emoji"]
                        puntos = sistema_puntos.get(i, 0)
                        st.markdown(f"""
                        <div class="podium-card">
                            <h2>{emoji_pos}</h2>
                            <h3>{emoji_pais} {piloto}</h3>
                            <p>{pilotos_equipos[piloto]['equipo']}</p>
                            <p><strong>{puntos} puntos {('(Sprint)' if es_sprint else '')}</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Forzar recarga de la página para mostrar datos actualizados
                st.rerun()

# -----------------------------
# 📅 CALENDARIO
# -----------------------------
elif seccion == "📅 Calendario":
    st.header("📅 Calendario F1 2025")
    
    st.markdown("### 🏁 Temporada Completa")
    
    # Crear DataFrame del calendario
    df_calendario = []
    for carrera in calendario:
        ronda = carrera["ronda"]
        completada = "✅" if ronda in resultados else "⏳"
        estado = "Completada" if ronda in resultados else "Pendiente"
        formato = "🏃‍♂️ Sprint" if carrera["sprint"] else "🏁 Tradicional"
        
        # Para weekends Sprint, verificar ambos eventos
        if carrera["sprint"]:
            carrera_principal = "✅" if ronda in resultados else "⏳"
            carrera_sprint = "✅" if ronda in resultados_sprint else "⏳"
            estado_detallado = f"Principal: {carrera_principal} | Sprint: {carrera_sprint}"
        else:
            estado_detallado = estado
        
        df_calendario.append({
            "Estado": completada,
            "Ronda": ronda,
            "Gran Premio": carrera["gran_premio"],
            "Circuito": carrera["circuito"],
            "Formato": formato,
            "Fecha Carrera": carrera["fecha"],
            "Fin de Semana": carrera["fecha_completa"],
            "Estado Detalle": estado_detallado
        })
    
    df_cal = pd.DataFrame(df_calendario)
    
    # Configurar el DataFrame para mejor visualización
    st.dataframe(
        df_cal, 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "Estado": st.column_config.TextColumn("Estado", width="small"),
            "Ronda": st.column_config.NumberColumn("Ronda", width="small"),
            "Gran Premio": st.column_config.TextColumn("Gran Premio", width="medium"),
            "Circuito": st.column_config.TextColumn("Circuito", width="medium"),
            "Formato": st.column_config.TextColumn("Formato", width="small"),
            "Fecha Carrera": st.column_config.TextColumn("Fecha Carrera", width="small"),
            "Fin de Semana": st.column_config.TextColumn("Fin de Semana", width="medium"),
            "Estado Detalle": st.column_config.TextColumn("Estado Detalle", width="large"),
        }
    )
    
    # Progreso de la temporada
    carreras_completadas = len([r for r in resultados.keys()])
    progreso = (carreras_completadas / len(calendario)) * 100
    
    st.subheader("📊 Progreso de la Temporada")
    st.progress(progreso / 100)
    st.write(f"**{carreras_completadas}** de **{len(calendario)}** carreras completadas ({progreso:.1f}%)")
    
    # Próxima carrera
    proxima_carrera = None
    for carrera in calendario:
        if carrera["ronda"] not in resultados:
            proxima_carrera = carrera
            break
    
    if proxima_carrera:
        st.markdown("### 🏎️ Próxima Carrera")
        formato_info = " 🏃‍♂️ (Formato Sprint)" if proxima_carrera["sprint"] else ""
        st.info(f"**Ronda {proxima_carrera['ronda']}**: {proxima_carrera['gran_premio']} - {proxima_carrera['circuito']}{formato_info}")
        st.write(f"📅 **Fin de semana**: {proxima_carrera['fecha_completa']}")
        st.write(f"🏁 **Carrera**: {proxima_carrera['fecha']}")
        
        if proxima_carrera["sprint"]:
            st.markdown("""
            **🏃‍♂️ Formato Sprint:**
            - **Viernes**: Entrenamientos libres y clasificación Sprint
            - **Sábado**: Carrera Sprint (puntos: 8-7-6-5-4-3-2-1)
            - **Domingo**: Carrera principal (puntos completos)
            """)
    else:
        st.success("🏁 ¡Temporada completada! Todas las carreras han sido registradas.")
