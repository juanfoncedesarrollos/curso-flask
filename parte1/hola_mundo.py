from flask import Flask

app = Flask(__name__) # se hace una instancia del objeto recibiendo como parametro name


@app.route('/') # se usa el decorador para colocarle la ruta a la siguiente funcion
def index(): # se crea la funcion que va a retornar en el serfvicio con la url que se le dio en el decorador
    return 'hola mundo' # codigo de la fucnion

app.run() # se da el punto de partida para el servicio
