# 🏎️ Aplicación F1 Championship 2025

Una aplicación web interactiva avanzada para seguir y gestionar los resultados del Campeonato de Fórmula 1 2025, incluyendo soporte completo para **carreras Sprint**.

## ✨ Características Principales

### 🏆 Dashboard Principal
- **Métricas en tiempo real**: Carreras completadas, carreras Sprint, líder del campeonato, equipo líder
- **Gráfico de evolución avanzado**: Seguimiento de puntos acumulados incluyendo Sprint races
- **Top 5 pilotos mejorado** con diferencias de puntos, información de equipos y banderas de países
- **Clasificación visual interactiva** con gráficos de barras y colores de equipos
- **Clasificación de constructores** con estadísticas detalladas
- **Próxima carrera destacada** con información de Sprint si aplica

### 📊 Análisis Detallado
- **Resultados por carrera** con podios destacados y tarjetas visuales
- **Estadísticas completas** de victorias y podios (principales + Sprint)
- **Análisis carrera por carrera** con datos detallados y métricas avanzadas
- **Gráficos interactivos** de evolución de puntos por piloto

### 📈 Estadísticas Generales (NUEVAS)
Sección completamente renovada con 5 pestañas especializadas:

#### 🏆 **Victorias & Podios**
- **Victorias combinadas**: Principales + Sprint con desglose detallado
- **Podios totales**: Estadísticas completas con porcentajes de éxito
- **Tarjetas visuales** con colores de equipos y métricas avanzadas

#### 📊 **Análisis de Rendimiento**
- **Consistencia Top 10**: Porcentaje de carreras en puntos
- **Promedio de posición**: Análisis estadístico con mejor/peor resultado
- **Rendimiento comparativo** entre pilotos

#### 🏎️ **Estadísticas por Equipo**
- **Clasificación de constructores** con diferencias de puntos
- **Estadísticas detalladas**: Victorias, podios, puntos scored por equipo
- **Mejor posición** y análisis comparativo entre equipos

#### 🎯 **Récords & Rachas**
- **Rachas actuales**: Podios y puntos consecutivos
- **Récords de temporada**: Poles, debuts, carreras más disputadas
- **Análisis de tendencias** y momentos destacados

#### 📈 **Tendencias**
- **Evolución gráfica detallada** con marcadores de Sprint
- **Pilotos en forma**: Análisis de últimas 3 carreras
- **Proyección de campeonato**: Estimación basada en tendencia actual
- **Análisis predictivo** para carreras restantes

### 📥 Gestión de Resultados (MEJORADA)
- **Soporte completo para Sprint**: Gestión independiente de Sprint y carrera principal
- **Interfaz de parrilla visual**: Layout 2x2 como la F1 real
- **Carga automática dual**: Muestra ambos resultados (Sprint + Principal) cuando existen
- **Validación inteligente**: Manejo robusto de archivos y datos
- **Vista previa mejorada**: Podios y estadísticas inmediatas tras guardar
- **Formularios inteligentes**: Cargan resultados existentes automáticamente

### 📅 Calendario Completo
- **Calendario completo 2025**: 24 carreras con 6 weekends Sprint
- **Progreso visual avanzado**: Estado detallado de cada carrera
- **Información de circuitos**: Datos completos de cada Gran Premio
- **Próxima carrera**: Destacada con información de Sprint si aplica
- **Indicadores visuales**: Sprint races claramente marcados

## 🏃‍♂️ Soporte para Carreras Sprint

### Weekends Sprint 2025
- **Ronda 2**: Gran Premio de China 🇨🇳
- **Ronda 6**: Gran Premio de Miami 🇺🇸  
- **Ronda 12**: Gran Premio de Bélgica 🇧🇪
- **Ronda 19**: Gran Premio de Estados Unidos 🇺🇸
- **Ronda 21**: Gran Premio de São Paulo 🇧🇷
- **Ronda 23**: Gran Premio de Qatar 🇶🇦

### Sistema de Puntos Sprint
- **1º lugar**: 8 puntos
- **2º lugar**: 7 puntos
- **3º lugar**: 6 puntos
- **4º lugar**: 5 puntos
- **5º lugar**: 4 puntos
- **6º lugar**: 3 puntos
- **7º lugar**: 2 puntos
- **8º lugar**: 1 punto

### Funcionalidades Sprint
- **Gestión independiente**: Sprint y carrera principal por separado
- **Visualización dual**: Ambos resultados mostrados lado a lado
- **Estadísticas combinadas**: Puntos y logros unificados
- **Archivos separados**: `resultados.txt` y `resultados_sprint.txt`
- **Estado de cada carrera** (completada/pendiente)
- **Próxima carrera** destacada

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación Completa

#### Opción 1: Instalación con Entorno Virtual (Recomendado)
1. **Clona o descarga** este repositorio
   ```bash
   git clone https://github.com/millanda29/Formula1-App.git
   ```
2. **Navega al directorio** del proyecto:
   ```bash
   cd Formula1-App
   ```
3. **Crea un entorno virtual**:
   ```bash
   # En Windows
   python -m venv .venv
   
   # En macOS/Linux
   python3 -m venv .venv
   ```
4. **Activa el entorno virtual**:
   ```bash
   # En Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   
   # En Windows (Command Prompt)
   .venv\Scripts\activate.bat
   
   # En macOS/Linux
   source .venv/bin/activate
   ```
5. **Instala las dependencias**:
   ```bash
   # Opción recomendada (usar archivo existente)
   pip install -r requirements.txt
   
   # Opción alternativa (manual)
   pip install streamlit plotly pandas numpy
   ```

#### Opción 2: Instalación Global (Alternativa)
1. **Navega al directorio** del proyecto:
   ```bash
   cd Formula1-App
   ```
2. **Instala las dependencias** directamente:
   ```bash
   # Usar el archivo requirements.txt incluido
   pip install -r requirements.txt
   
   # O instalar manualmente
   pip install streamlit plotly pandas numpy
   ```

### Verificar la Instalación
Para verificar que todo esté instalado correctamente:
```bash
# Verificar Python
python --version

# Verificar Streamlit
streamlit --version

# Verificar paquetes instalados
pip list | findstr -i "streamlit plotly pandas"
```

### Ejecutar la aplicación
Con el entorno virtual activado:
```bash
streamlit run app.py
```
O alternativamente:
```bash
python -m streamlit run app.py
```

**Nota**: Si usaste entorno virtual, recuerda activarlo cada vez que quieras ejecutar la aplicación.

### Crear archivo requirements.txt (Opcional)
**Nota**: El proyecto ya incluye un archivo `requirements.txt` actualizado.

Si quieres generar tu propio archivo de requisitos:
```bash
# Con entorno virtual activado
pip freeze > requirements.txt
```

Contenido actual del `requirements.txt`:
```
streamlit==1.30.0
plotly==5.17.0
pandas==2.1.4
numpy==1.26.2
```

### Desactivar Entorno Virtual
Cuando termines de usar la aplicación:
```bash
# En Windows y macOS/Linux
deactivate
```

### 🔄 Uso Diario
Para usar la aplicación después de la instalación inicial:
1. **Navega al directorio**:
   ```bash
   cd Formula1-App
   ```
2. **Activa el entorno virtual** (si lo usaste):
   ```bash
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```
3. **Ejecuta la aplicación**:
   ```bash
   streamlit run app.py
   ```

## 🎮 Cómo usar la aplicación

### 1. Dashboard Principal
- Al abrir la aplicación, verás el dashboard con todas las estadísticas actuales
- **Nuevas estadísticas generales** con 5 pestañas especializadas
- Los gráficos se actualizan automáticamente cuando agregas nuevos resultados
- **Métricas en tiempo real** incluyendo carreras Sprint

### 2. Agregar Resultados (MEJORADO)
1. Ve a la sección "📥 Gestión de Resultados"
2. Selecciona el Gran Premio (weekends Sprint claramente marcados)
3. **Para weekends Sprint**: Elige entre "Sprint" o "Carrera Principal"
4. **Parrilla visual**: Asigna cada piloto a su posición (diseño 2x2 real)
5. **Carga automática**: Los resultados existentes se cargan automáticamente
6. Haz clic en "Registrar/Actualizar Resultados"
7. **Vista dual**: Si es weekend Sprint, verás ambos resultados lado a lado

### 3. Ver Análisis Avanzado
- **"📊 Análisis Detallado"**: Estadísticas específicas de cada carrera
- **"📈 Estadísticas Generales"**: 5 pestañas con análisis profundo:
  - 🏆 Victorias & Podios (principales + Sprint)
  - 📊 Análisis de Rendimiento (consistencia, promedios)
  - 🏎️ Estadísticas por Equipo (constructores detallado)
  - 🎯 Récords & Rachas (tendencias actuales)
  - 📈 Tendencias (proyecciones y análisis predictivo)

### 4. Consultar Calendario Sprint
- En "📅 Calendario" identifica weekends Sprint con 🐛
- **Progreso visual** con estado de Sprint y carrera principal
- **Próxima carrera** destacada con información completa

## 🏁 Características Técnicas

### Pilotos y Equipos Incluidos
- **Red Bull Racing**: Max Verstappen 🇳🇱, Liam Lawson 🇳🇿
- **Ferrari**: Charles Leclerc 🇲🇨, Lewis Hamilton 🇬🇧
- **Mercedes**: George Russell 🇬🇧, Andrea Kimi Antonelli 🇮🇹
- **McLaren**: Lando Norris 🇬🇧, Oscar Piastri 🇦🇺
- **Aston Martin**: Fernando Alonso 🇪🇸, Lance Stroll 🇨🇦
- **Alpine**: Pierre Gasly 🇫🇷, Jack Doohan 🇦🇺
- **Haas**: Esteban Ocon 🇫🇷, Oliver Bearman 🇬🇧
- **RB**: Yuki Tsunoda 🇯🇵, Isack Hadjar 🇫🇷
- **Williams**: Alexander Albon 🇹🇭, Carlos Sainz 🇪🇸
- **Sauber**: Nico Hülkenberg 🇩🇪, Gabriel Bortoleto 🇧🇷, Franco Colapinto 🇦🇷

### Sistema de Puntuación F1

#### Carreras Principales
- **1º lugar**: 25 puntos
- **2º lugar**: 18 puntos
- **3º lugar**: 15 puntos
- **4º lugar**: 12 puntos
- **5º lugar**: 10 puntos
- **6º lugar**: 8 puntos
- **7º lugar**: 6 puntos
- **8º lugar**: 4 puntos
- **9º lugar**: 2 puntos
- **10º lugar**: 1 punto

#### Carreras Sprint
- **1º lugar**: 8 puntos
- **2º lugar**: 7 puntos
- **3º lugar**: 6 puntos
- **4º lugar**: 5 puntos
- **5º lugar**: 4 puntos
- **6º lugar**: 3 puntos
- **7º lugar**: 2 puntos
- **8º lugar**: 1 punto

## 📊 Tecnologías Utilizadas
- **Streamlit**: Framework de aplicaciones web con interfaz moderna
- **Plotly**: Gráficos interactivos avanzados
- **Pandas**: Manipulación y análisis de datos
- **Python**: Lógica de backend y cálculos

## 💾 Almacenamiento de Datos
Los resultados se almacenan en archivos CSV optimizados:
- **`resultados.txt`**: Carreras principales
- **`resultados_sprint.txt`**: Carreras Sprint

Beneficios:
- **Persistencia** de datos entre sesiones
- **Fácil backup** y restauración
- **Portabilidad** de datos
- **Manejo robusto** de errores y líneas vacías

## 🎨 Personalización y Diseño
La aplicación incluye:
- **Tema F1 auténtico** con colores oficiales de equipos
- **Emojis de países** para cada piloto con representación visual
- **Colores de equipos reales** para mejor identificación
- **Diseño responsive** que se adapta a diferentes pantallas
- **Interfaz de parrilla visual** simulando el formato real de F1
- **Gradientes y animaciones** para una experiencia premium
- **CSS personalizado** para tarjetas y métricas interactivas

## 🔧 Solución de Problemas

### La aplicación no inicia
- **Verifica Python**: `python --version` (debe ser 3.8+)
- **Activa el entorno virtual** si lo usaste: `.venv\Scripts\activate`
- **Instala las dependencias**: `pip install streamlit plotly pandas`
- **Verifica la instalación**: `streamlit --version`

### Problemas con Entorno Virtual
- **Error al crear .venv**: Verifica que tengas permisos de escritura
- **Script de activación no funciona**: 
  ```bash
  # Intenta con diferentes métodos:
  .venv\Scripts\activate.bat    # Command Prompt
  .venv\Scripts\Activate.ps1    # PowerShell
  ```
- **Entorno no se activa**: Verifica que estés en el directorio correcto
- **Comando python no encontrado**: Usa `python3` en lugar de `python`

### Problemas de Dependencias
- **ModuleNotFoundError**: 
  ```bash
  # Instala específicamente el módulo faltante
  pip install streamlit
  pip install plotly
  pip install pandas
  ```
- **Versiones incompatibles**: 
  ```bash
  # Actualiza pip y reinstala
  python -m pip install --upgrade pip
  pip install --upgrade streamlit plotly pandas
  ```

### Los gráficos no se muestran
- Verifica tu **conexión a internet** (Plotly puede requerir recursos externos)
- Intenta **refrescar la página** del navegador (F5)
- Verifica que Plotly esté instalado: `pip install plotly`
- **Limpia caché del navegador** si persiste el problema

### Los datos no se guardan
- Verifica **permisos de escritura** en el directorio de la aplicación
- Los archivos `resultados.txt` y `resultados_sprint.txt` deben poder crearse
- Verifica que no haya **archivos bloqueados** por antivirus

### Error "ValueError: not enough values to unpack"
- **Solución automática**: La aplicación ahora maneja líneas vacías
- Si persiste, verifica que los archivos CSV tengan formato correcto: `ronda,piloto,posicion`

### Los resultados Sprint no se muestran
- Verifica que hayas seleccionado **"Sprint"** en el tipo de evento
- Los weekends Sprint están marcados con 🐛 en el calendario
- Ambos archivos (`resultados.txt` y `resultados_sprint.txt`) son independientes

## 📝 Notas Técnicas

### Nuevas Funcionalidades 2025
- ✅ **Soporte completo Sprint**: 6 weekends con gestión independiente
- ✅ **Estadísticas avanzadas**: 5 pestañas especializadas con análisis profundo
- ✅ **Interfaz mejorada**: Parrilla visual 2x2 como la F1 real
- ✅ **Carga dual automática**: Muestra Sprint + Principal simultáneamente
- ✅ **Manejo robusto de errores**: Ignora líneas vacías y archivos malformados
- ✅ **Proyecciones de campeonato**: Análisis predictivo basado en tendencias

### Configuración Técnica
- **Temporada**: 2025 (24 carreras, 6 Sprint)
- **Equipos y pilotos**: Alineación oficial esperada para 2025
- **Archivos de datos**: CSV simples para fácil manipulación
- **Rendimiento**: Optimizado para hasta 24 carreras completas

### Personalización Avanzada
Puedes modificar fácilmente:
- **Pilotos y equipos**: Edita el diccionario `pilotos_equipos` en `app.py`
- **Colores de equipos**: Cambia los valores hexadecimales en la configuración
- **Calendario**: Modifica la lista `calendario` para temporadas futuras
- **Sistema de puntos**: Ajusta `puntos_por_posicion` y `puntos_sprint`

## 💡 Mejores Prácticas

### Uso de Entorno Virtual
**¿Por qué usar entorno virtual?**
- ✅ **Aislamiento**: Evita conflictos entre proyectos
- ✅ **Control de versiones**: Cada proyecto tiene sus dependencias específicas  
- ✅ **Reproducibilidad**: Fácil compartir el proyecto con mismo entorno
- ✅ **Limpieza**: No contamina la instalación global de Python

### Gestión de Dependencias
**Consejos importantes:**
- 📝 **Documenta versiones**: Siempre especifica versiones en `requirements.txt`
- 🔄 **Actualiza regularmente**: Mantén las dependencias actualizadas
- 🧪 **Prueba actualizaciones**: Verifica compatibilidad antes de actualizar
- 💾 **Backup de entorno**: Guarda `requirements.txt` en control de versiones

### Estructura de Proyecto Recomendada
```
Formula1-App/
├── .venv/                 # Entorno virtual (no subir a git)
├── app.py                 # Aplicación principal
├── requirements.txt       # Dependencias
├── README.md             # Documentación
├── resultados.txt        # Datos carreras principales
├── resultados_sprint.txt # Datos carreras sprint
└── .gitignore           # Archivos a ignorar en git
```

### Comandos Útiles
```bash
# Verificar entorno activo
where python        # Windows
which python        # macOS/Linux

# Listar paquetes instalados
pip list

# Verificar versión de un paquete específico
pip show streamlit

# Actualizar un paquete específico
pip install --upgrade streamlit

# Crear requirements desde entorno actual
pip freeze > requirements.txt
```

---

## 🏆 Resumen de Mejoras 2025

### ✨ Funcionalidades Principales
- 🏃‍♂️ **Soporte completo Sprint**: 6 weekends con gestión independiente
- 📈 **Estadísticas generales renovadas**: 5 pestañas especializadas
- 🎯 **Análisis predictivo**: Proyecciones de campeonato y tendencias
- 🏁 **Interfaz de parrilla visual**: Layout 2x2 auténtico de F1
- 🔄 **Carga dual automática**: Sprint + Principal simultáneamente

### 🚀 Mejoras Técnicas
- 🛠️ **Manejo robusto de errores**: Archivos malformados y líneas vacías
- 📊 **Gráficos avanzados**: Marcadores Sprint y evolución detallada
- 🎨 **Diseño premium**: Gradientes, animaciones y colores oficiales
- 📱 **Responsive mejorado**: Adaptación perfecta a cualquier pantalla

### 📊 Análisis Avanzado
- 🏆 **Victorias & Podios combinados**: Principales + Sprint unificados
- 📈 **Consistencia y rendimiento**: Métricas estadísticas profundas
- 🏎️ **Análisis por equipos**: Constructores con estadísticas detalladas
- 🎯 **Récords y rachas**: Tendencias actuales y históricos
- 🔮 **Proyecciones**: Estimaciones basadas en análisis de datos

¡Disfruta la temporada 2025 de Fórmula 1 con la aplicación más completa! 🏁🏆🏃‍♂️
