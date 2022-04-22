#python index.py --->para ejecutar
#crtl+shift+R   para desactivar el cache

#necesitamos un framework o biblioteca
#frameworks: flask, django

#llamando al framework
from flask import Flask
#para retornar templates en las funciones
from flask import render_template

#para confirmar que este es el arhivo principal
app = Flask(__name__)  #creamos un objeto

#pasar un nombre para crear una url
@app.route('/') #ruta para la pagina principal
def home():
    return render_template('home.html')

#creando otra ruta
@app.route('/about')
def about():
    return render_template('about.html')

#para que la aplicacion siempre este ejecutandose

#validamos
if __name__ == '__main__':
    app.run(debug=True)   
    #debug =True para que no se reinicie el servidor
    #para cambiar codigo
    #se debe escribir esta linea y recien correr el servidor

