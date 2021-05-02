from flask import Flask
from flask import request # con la libreria request se pueden recibir los parametros 

app = Flask(__name__) 

@app.route('/') 
def index(): 
    return 'cambio ' 

@app.route('/saludo')
def saludo():
    return 'holi :)'

@app.route('/parametros')
def parametros():
    ### url/parametros?params=juan.... recive el parametrso con nombre de variable params
    param = request.args.get('params', 'no viene el parametro') # el segundo valor del argumento del get es el valor por defecto que va a colocar
    param_2 = request.args.get('params2', 'no viene el parametro')
    # se almacena el parametro que viene en params 
    # url/parametros?params=hola
    return 'el parametro es {}, {}'.format(param, param_2)
    # dentro de las rutas se pueden recibir parametros     
    #comunmente se reciben parametros como params o data, 
    # lo que se parece a django reques.params o request.data

if __name__ == '__main__':
    app.run(debug=True, port=8000) 
    # se puede dar el numero de puerto por el que va a escuchar
    # con debug = True se deja el servidor listo para que escuche 
    # los cambios sin necesidad de reiniciar el servidor


