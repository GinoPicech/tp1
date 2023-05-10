from flask import * 
#from datos import * 
app = Flask(__name__)

def lector_txt(archivo):
    """Esta funcion lee un archivo txt y lo almacena en una lista"""
    archi = open( archivo , "r", encoding="UTF-8")
    datos_archivo = archi.readlines()
    return datos_archivo

def ordenador(matriz):
    """Esta funcion ordena una matriz a partir del elemento 1 de forma alfabetica decreciente"""
    matriz.sort(key=lambda x:x[1],reverse=True)
    return matriz

def sacar_repetidos(lista):
    """esta funcion saca los repetidos de una lista de str"""
    lista=list(set(lista))
    lista.sort()
    return lista

frasespeliculas = []
peliculas = []
listapeli=lector_txt("frases_de_peliculas.txt")


peli_frase = ""  # variable global
frase = ""
cont2 = 0
puntos = 0

for i in listapeli:
    i = i.rstrip()
    i = i.split(";")
    frasespeliculas.append(i)
    peliculas.append(i[1])

#acomodar carpetas    
#crear una carpeta de ide de desarrollo, proyecto vs code para que se reconozcan todas las rutas en el proyecto    
frasespeliculas=ordenador(frasespeliculas)
peliculas= sacar_repetidos(peliculas)
import random
pelis=[]
for i in frasespeliculas:
    pelis.append(i[1])


@app.route("/", methods=['GET', 'POST'])
def index():  
    global frase 
    global peli_frase
    global puntos
    global cont2
    cont2 = 0
    puntos = 0 
    return render_template("indexxx.html")

lista_pelis=[]

# @app.route("/guardarnombre", methods=['POST'])
# def guardarnombre():
#     with open historial as archi 
#     archi.write(nombre)
#     return()


@app.route("/juego", methods=['GET', 'POST'])
def juego():
    global frase 
    global peli_frase
    global cont2
    global puntos 
    condicion = ""
    peli_1,peli_2,peli_3=random.sample(pelis,3)

    lista_pelis=[peli_1,peli_2,peli_3]
    a=random.choice(lista_pelis)
    for i in range(len(frasespeliculas)):
        if frasespeliculas[i][1]==a:
            lista_pelis.append(a)
            frase=frasespeliculas[i][0]
            peli_frase=frasespeliculas[i][1]

    if cont2 <5:   
        return render_template("juego.html" , cont2 = cont2 , condicion=condicion , frase=frase , peli_frase=peli_frase, lista_pelis=lista_pelis)
    if cont2 == 5:
        return render_template("resultados.html", puntos=puntos)
    


import time
@app.route('/guardar_boton', methods=['GET', 'POST'])
def guardar_boton():
    global peli_frase
    global frase 
    global cont2
    global puntos
    boton_oprimido = request.form["boton"]
    cont2 += 1
    # aquí puedes hacer lo que necesites con el botón oprimido por el usuario
    while cont2 <= 5:
        if boton_oprimido == peli_frase:
            print(puntos)
            puntos += 1
            return render_template("correcto.html" , peli_frase=peli_frase , frase=frase )
        else:
            print(puntos)
            return render_template("incorrecto.html", peli_frase=peli_frase , frase=frase )
    
@app.route("/resultado", methods=['GET', 'POST'])
def resultado():
    global puntos
    return render_template("resultados.html" , puntos=puntos)


    

if __name__ == "__main__":
    app.run(debug = True)
#que si esta en name corra
