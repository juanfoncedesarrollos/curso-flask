from flask import Flask
from flask import render_template

app=Flask(__name__) 

default='no se ingreso ningun parametro'
# los templates siempres son buscados en la tuta templates que se encuentre a la misma altura del archivo que se esta ejecutando
# para seleccionar otra carpeta de templates es necesario enviar como argumento template_folder=ruta/template en la instancia de la clase de flask

@app.route('/inicio')
@app.route('/inicio/<name>')
def templates(name=default):
    name = name
    return render_template('index.html')

@app.route('/template_variable')
@app.route('/template_variable/<name>')
def template_vatiable(name=default):
    edad = 20 
    list = [1,2350,23,2,3,4,5,6,7,20]
    return render_template('user.html', 
                           nombre=name,
                           edad=edad, 
                           list=list)


if __name__ == '__main__':
    app.run(debug=True, port=8000)