import dash
from dash import html, dcc

dash.register_page(__name__, path="/introduccion", name="Introducción", order=2)

layout = html.Div(
    # Limitar el ancho y centrar el contenido para mejor lectura
    style={"padding": "40px", "maxWidth": "850px", "margin": "0 auto", "textAlign": "justify"},
    children=[
        
        html.H1("Introducción del Proyecto", className="display-5", style={'textAlign': 'center', 'marginBottom': '30px'}),
        html.Hr(),
        
        # Imagen central mejorada
        html.Img(
            src='/assets/cafe_intro.jpg', 
            alt='Análisis del Café y Salud',
            style={
                'display': 'block',
                'margin': '20px auto 40px auto', # Más margen inferior
                'height': '250px', 
                'maxWidth': '100%',
                'borderRadius': '8px', # Esquinas redondeadas
                'boxShadow': '0 4px 8px rgba(0,0,0,0.15)' # Sombra para destacar
            }
        ),
        
        # Párrafo principal usando dcc.Markdown
        dcc.Markdown("""
            Este proyecto busca analizar el **consumo mundial de café** y su relación con diversas **variables de salud**. 
            A través de técnicas de visualización de datos avanzadas, se construye un dashboard interactivo que permite 
            comprender patrones globales y diferencias entre países. 
            
            Además, se emplean métodos de **machine learning** (modelos predictivos) para identificar y predecir posibles 
            problemas de salud asociados al consumo de café y otros factores de estilo de vida.
        """, className="lead"),
        
        html.Br(),
        
        # Propósito General
        html.H3("Propósito General del Dashboard 🎯"),
        dcc.Markdown("""
            > Proveer una herramienta visual analítica que facilite la **toma de decisiones basada en datos**, 
            > especialmente en temas relacionados con hábitos de consumo, salud pública y tendencias globales de bienestar.
        """, className="blockquote"), # Clase blockquote le dará un estilo de cita (barra lateral)
        
        html.Br(),

        # Estructura del Dashboard (Mejor presentación de lista)
        html.H3("Estructura y Flujo del Proyecto 🧭"),
        html.Ul(
            style={'listStyleType': 'none', 'paddingLeft': '0'}, # Elimina el bullet por defecto
            children=[
                html.Li("Contexto Global: Presentación e Introducción."),
                html.Li("Fundamentos: Marco Teórico, Problema y Objetivos."),
                html.Li("Resultados y Modelo: Metodología, Análisis y Visualización Geográfica."),
                html.Li("Conclusiones: Resumen y Recomendaciones Clave."),
            ]
        ),
        
        html.Br(),
        html.Hr()
    ]
)