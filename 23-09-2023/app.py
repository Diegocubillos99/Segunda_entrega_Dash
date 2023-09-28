import dash #importa dash
import dash_bootstrap_components as dbc #importa los componentes bootstrap de das como dbc
from dash.dependencies import Input, Output #de dash.dependencies se importa input y output
import math #se importa math

#Se importa frontend
from frontend.main import layout

app=dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#crea la variable app y agrega __name__ y los estilos con bootstrap

app.layout = layout #se asigna el layout en la variable layout de app

@app.callback(#llama de app
    Output('salidaCirculo', 'children'), #llama en output la salidaCirculo como children
    Input('entradaCirculo', 'value'), #llama en input la entradaCirculo como value
)

def areaCirculo(entradaCirculo):#crea la función areaCirculo con dato de entrada entradaCirculo
    areaCalculadaCirculo = math.pi * (entradaCirculo**2) #Hace la operación y la guarda en la variable areaCalculadaCirculo
    return 'El área del círculo es: ' + str(areaCalculadaCirculo) #retorna la respuesta con el resultado

if __name__ == '__main__': #si __name__ y __main__ son iguales
    app.run_server(debug=True) #Ejecuta la app