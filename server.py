from flask import Flask, render_template #Importamos Flask para permitirnos crear una aplicación
app = Flask(__name__) #Creando una instancia de Flask y la llamo app

@app.route('/') #En la ruta '/' me va a ejecutar la función que vaya en la siguiente línea
def hola_mundo():
    return "<h1>Hola Mundo!</h1>" #Al acceder a mi ruta / me regresa un Hola Mundo

@app.route('/hola/<nombre>') #Para una ruta /hola/______ lo que me regresa después de /hola/ lo considero como variable
def hola_nombre(nombre):
    return "Hola "+nombre

@app.route('/hello')
def hola_mundo2():
    #En lugar de devolver una cadena/texto
    #Devolviendo el resultado del método render_template, pasando el nombre de mi archivo HTML
    return render_template('index.html', nombre="John") #JINJA

@app.route('/hello2')
def base():
    return render_template('child.html')

@app.route('/repeat/<int:num>/<palabra>')
def repite_palabra(num, palabra):
    output = ''
    output = palabra*num
    # for i in range(0, num):
    #     output += '<p>'+palabra+'</p>'
    return output 


if __name__ == "__main__":  #Asegurando de que el archivo se esté ejecutando directamente y NO desde otro módulo
    app.run(debug=True)     #Ejecute mi aplicación
