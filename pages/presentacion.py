# pages/presentacion.py

import dash
from dash import html, dcc

# Registrar la página y establecerla como la página de inicio (path="/")
dash.register_page(__name__, path="/", name="Presentación", order=1)

def layout():
    return html.Div(
        style={"padding": "40px", "maxWidth": "800px", "margin": "0 auto", "textAlign": "center"},
        children=[
            # --- LOGO DE LA UNIVERSIDAD ---
            html.Img(
                src='/assets/logo_universidad.jpg', 
                alt='Logo de la Universidad',
                style={'height': '240px', 'margin': '0 auto', 'marginBottom': '40px'}
            ),
            
            html.H1("Análisis del Impacto del Consumo de Café en la Salud", 
                    className="display-4", style={'color': '#007bff'}),
            html.H2("Dashboard de Visualización de Datos", className="text-secondary"),

            html.Hr(),

            html.Div(
                style={'textAlign': 'left', 'marginTop': '30px'},
                children=[
                    html.H3("👥 Autores del Proyecto", style={'marginTop': '30px'}),
                    html.Ul([
                        html.Li("Danier Conde"),
                        html.Li("Jerónimo Dommínguez")
                    ]),
                    
                    html.H3("📚 Curso y Profesora", style={'marginTop': '30px'}),
                    html.P("Curso: Visualización de Datos y Toma de Decisiones"),
                    html.P("Profesora: Keyla Alba"),
                ]
            ),
            
            html.Div(
                style={'marginTop': '50px'},
                children=[
                    html.H4("¡Bienvenido al Análisis!", className="text-info"),
                    html.P("Utiliza el menú de navegación superior para explorar los resultados del análisis univariado, bivariado, el mapa geográfico y las conclusiones obtenidas.", className="lead")
                ]
            )
        ]
    )