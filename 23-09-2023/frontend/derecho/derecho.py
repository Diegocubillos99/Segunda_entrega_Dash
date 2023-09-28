import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
#importa las librerías necesarias

derecho=dbc.Container([#crea la variable derecho y en ella un Container
    html.H1('Datos del Proyecto', style={'color':'#17242d'}),#crea un titulo 1 y define el color del texto
    html.Hr(),#añade un espacio
    html.Div([#crea una división
        html.Label('Radio del círculo', style={'color':'#17242d'}), 
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='entradaCirculo', value=5, type='number')]), 
        #se crea un Input con identificador, valor por defecto 5 y tipo numero
        html.Label(id='salidaCirculo'), #se crea una etiqueta (texto) con identificador
])