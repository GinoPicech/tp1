from flask import * 

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

for i in listapeli:
    i = i.rstrip()
    i = i.split(";")
    frasespeliculas.append(i)
    peliculas.append(i[1])
    
    
frasespeliculas=ordenador(frasespeliculas)
peliculas= sacar_repetidos(peliculas)
import random
pelis=[]
for i in frasespeliculas:
    pelis.append(i[1])


@app.route("/")
def index():  
    return render_template("index.html")


@app.route("/juego")
def juego():
    peli_1,peli_2,peli_3=random.sample(pelis,3)

    lista_pelis=[peli_1,peli_2,peli_3]
    a=random.choice(lista_pelis)
    for i in range(len(frasespeliculas)):
        if frasespeliculas[i][1]==a:
            frase=frasespeliculas[i][0]
            peli_frase=frasespeliculas[i][1] 
                        
    return render_template("juego.html" , frase=frase , peli_frase=peli_frase)

@app.route("/correcto")
def correcto():
     return render_template("correcto.html")

if __name__ == "__main__":
    app.run(debug = True)
#que si esta en name corra
