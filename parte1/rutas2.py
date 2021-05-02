from flask import Flask
from flask import request

app = Flask(__name__)
default = 'no existe parametro'

@app.route('/parametrosslash')
@app.route('/parametrosslash/<name>')
@app.route('/parametrosslash/<name>/<int:num>')
### url/parametosslash/parametro/parametro .... recibe parametros por medio de un slash
# se pueden colocar los tipos de dato para que me reciba solo ese tipo de datos 
def parametrosslash(name=default, num=default):
    return 'el parametro es: {}, {}'.format(name, num)

if __name__ == '__main__':
    app.run(debug=True, port=8000)