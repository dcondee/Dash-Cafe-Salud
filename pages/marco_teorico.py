import dash
from dash import html, dcc # Importamos dcc para usar Markdown

dash.register_page(__name__, path="/marco-teorico", name="Marco Teórico", order=3)

# La imagen que generamos anteriormente para el Marco Teórico es la de la molécula y los efectos.
# Usaremos 'caffeine_diagram.png' como nombre.

layout = html.Div(
    # Estilo del contenedor principal: limita el ancho para mejor lectura y lo centra
    style={"padding": "40px", "maxWidth": "850px", "margin": "0 auto", "textAlign": "justify"},
    children=[
        
        # Título principal con estilo de encabezado de página
        html.H1("Marco Teórico y Fundamentos", className="display-5", style={'textAlign': 'center', 'marginBottom': '30px'}),
        html.Hr(),
        
        # 1. Sección: El consumo de café como indicador
        html.H3("El Consumo de Café como Indicador Cultural y Económico ☕"),
        dcc.Markdown("""
            El café representa más que una bebida: constituye un indicador del **estilo de vida** y del **desarrollo económico** en diversas regiones del mundo. Su alta demanda global 
            lo posiciona como un *commodity* vital, cuyo consumo refleja patrones culturales 
            y socioeconómicos que pueden influir indirectamente en las métricas de salud poblacional.
        """, className="lead"), # La clase "lead" de Bootstrap hace que el texto sea ligeramente más grande
        
        html.Br(),
        
        # 2. Sección: Relación entre consumo de café y salud
        html.H3("Relación entre Consumo de Café y Salud 🔬"),
        
        # Contenedor para hacer flotar la imagen junto al texto (referente a la cafeína/salud)
        html.Div(
            style={'overflow': 'auto', 'marginBottom': '20px'},
            children=[
                # Imagen del diagrama de cafeína (asumiendo que la guardaste como tal)
                html.Img(
                    src='/assets/marco_teorico.png', 
                    alt='Diagrama de efectos de la Cafeína',
                    style={
                        'height': '200px', # Tamaño ligeramente reducido
                        'float': 'right',   # Flotar a la derecha
                        'marginLeft': '25px', # Espacio a la izquierda
                        'borderRadius': '8px', # Esquinas redondeadas
                        'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)' # Sombra sutil
                    }
                ),
                dcc.Markdown("""
                    Estudios científicos han demostrado asociaciones entre el consumo moderado de café 
                    y beneficios como menor riesgo de enfermedades cardiovasculares y neurodegenerativas. 
                    
                    No obstante, la relación debe ser analizada con cautela, ya que el exceso de cafeína 
                    puede afectar indicadores directos como la **Frecuencia Cardíaca** y la calidad del **Sueño**. 
                    
                    La interacción con indicadores de estilo de vida como el **BMI** y el **Nivel de Estrés** sigue siendo el foco central de nuestra investigación.
                """, style={'textAlign': 'justify'}, className="lead")
            ]
        ),
        
        html.Br(),
        
        # 3. Sección: Visualización de Datos
        html.H3("Fundamentos de la Visualización de Datos 📊"),
        dcc.Markdown("""
            La visualización de datos permite explorar grandes volúmenes de información, 
            comprender **patrones ocultos** y comunicar hallazgos de manera efectiva y accesible. 
            
            En este proyecto, utilizamos **gráficos Plotly** para generar visualizaciones 
            interactivas, siendo el **mapa coroplético** un componente clave para facilitar la 
            interpretación espacial del consumo de café a nivel mundial.
        """, className="lead"),
        
        html.Hr(style={'marginTop': '40px'}),
        html.P("El marco teórico proporciona la base conceptual para la interpretación de los resultados analíticos.", 
               style={'textAlign': 'center', 'color': '#6c757d'})
    ]
)