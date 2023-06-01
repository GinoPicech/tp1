from funciones.herramientas import dif_porcentual, leer_csv, agregar_a_lista, rematriz
import matplotlib.pyplot as plt


datos_google_01=[]
datos_google_trimestre=[]
datos_google=[]
datos_nike_01=[]   
datos_nike_variacion=[]  


todo_google = leer_csv("google.csv")[1:]

mat_rep_google=todo_google.copy()
mat_rep_google.sort(key=lambda x:x[1],reverse=True)
maxi_g=float(mat_rep_google[0][1])
mini_g=float(mat_rep_google[-1][1])

for i in todo_google:   
       datos_google_01.append([i[0],((float(i[1])-mini_g)/(maxi_g-mini_g))]) 
       datos_google.append(i)
       
for i in datos_google:
    dia,mes,año=i[0].split("/")
    if int(mes)<4:
        datos_google_trimestre.append(i)

      
todo_nike=leer_csv("nike.csv")[1:]

mat_rep_nike=[]
for i in todo_nike:
    mat_rep_nike.append([i[0],float(i[1])])
    
mat_rep_nike.sort(key=lambda x:x[1],reverse=True)
maxi_nike=mat_rep_nike[0][1]
mini_nike=mat_rep_nike[-1][1]

for i in todo_nike:
    if len(i)>1:
        datos_nike_01.append([i[0],((float(i[1])-mini_nike)/(maxi_nike-mini_nike))]) #max y mini de nike
        datos_nike_variacion.append(i)
           
#%%    #ej 1  

primer=float(datos_google_trimestre[0][1])   
datos_google_2=datos_google_trimestre.copy()
datos_google_2.sort(key=lambda x: x[1], reverse=False)
minimo=float(datos_google_2[0][1])
maximo=float(datos_google_2[-1][1])

print("a)  La caida fue de un", round(dif_porcentual(minimo,primer) , 2) , "porciento")          
#  b) si se corresponde a comparacion de la grafica
ultimo_valor=float(datos_google[-1][1])

print("c)  La subida fue de un", round(dif_porcentual(ultimo_valor, minimo) , 2) , "porciento")     
# d) si corresponde a comparacion de la grafica

#%%

val_inic_google=float(datos_google[0][1])
variaciones_google=rematriz(val_inic_google,datos_google)
val_inic_nike=float(datos_nike_variacion[0][1])
variaciones_nike=rematriz(val_inic_nike,datos_nike_variacion)    
                 
#Correccion abajo                     
"""
valor_inicial_google = float(datos_google[0][1])

variaciones_google = [[None, None] for i in range(len(datos_google)-1)]

for i in range(1, len(datos_google)):
    variaciones_google[i-1][0] = datos_google[i][0]
    variaciones_google[i-1][1] = ((float(datos_google[i][1]) - valor_inicial_google) / valor_inicial_google) * 100


-----------------------------------Correccion-------------------------------------
 

valor_inicial_nike = float(datos_nike_variacion[0][1])

variaciones_nike = [[None, None] for i in range(len(datos_nike_variacion)-1)]

for i in range(1, len(datos_nike_variacion)):
    variaciones_nike[i-1][0] = datos_nike_variacion[i][0]
    variaciones_nike[i-1][1] = ((float(datos_nike_variacion[i][1]) - valor_inicial_nike) / valor_inicial_nike) * 100
"""

acciones_google=agregar_a_lista(datos_google_01, 1)  # cargar a una lista los valores de 01 de google
acciones_nike=agregar_a_lista(datos_nike_01, 1) # cargar a una lista los valores de 01 de nike
lista_variacion_google=agregar_a_lista(variaciones_google, 1) # cargar a una lista los valores de porcentuales de google
lista_variacion_nike=agregar_a_lista(variaciones_nike, 1) # cargar a una lista los valores de porcentuales de nike    

# Crear la figura y los ejes
fig, ax = plt.subplots(1,2,figsize=(10, 5))

#plt.subplot(1,2,1)    
ax[0].plot(acciones_google)
ax[0].plot(acciones_nike)

ax[0].set_xlabel('Días')
ax[0].set_ylabel('Acciones')
ax[0].set_title("Precios normalizados entre 0 y 1")
ax[0].legend(["Google", "Nike"])
ax[0].grid()

ax[1].plot(lista_variacion_google)
ax[1].plot(lista_variacion_nike)
plt.xlabel('Días')
plt.ylabel('Acciones')
plt.title("Tasa de variacion como porcentaje del precio inicial")
plt.legend(["Google", "Nike"])
plt.grid()

plt.show()
