##Calculadora de cantidades
##Elaborado por: Juan Sebastian Leal 
import pandas as pd
from openpyxl import load_workbook
import os

###Funcion para exportar a excel, nos permite dividir en cada pagina las diferentes areas que vamos a sacar
###perimetros y datos que vamos a usar en dado caso de que se quiera manejar desde excel
def exportar_excel(muros_ladrillo,muros_fachada,ventanas_ladrillo,ventanas_fachada,metros_baranda):
    ###Si no hay datos para exportar nos devolvemos al menu automaticamente
    if not (muros_ladrillo or muros_fachada or ventanas_ladrillo or ventanas_fachada):
        print("No hay datos para exportar")
        return
    nombre_archivo="Resumen_Cantidades.xlsx"
    ###Como en el punto anterior solo en el caso de que contenga algo las listas lo vamos a poder exportar
    ###en dado caso de que no haya no se va a crear la pestaña en excel.
    with pd.ExcelWriter(nombre_archivo, engine="openpyxl") as writer:
        if muros_ladrillo:
            pd.DataFrame(muros_ladrillo).to_excel(writer, sheet_name="Ladrillo",index=False)
        if muros_fachada:
            pd.DataFrame(muros_fachada).to_excel(writer, sheet_name="Pintura",index=False)
        if ventanas_ladrillo:
            pd.DataFrame(ventanas_ladrillo).to_excel(writer, sheet_name="V.Ladrillo",index=False)
        if ventanas_fachada:
            pd.DataFrame(ventanas_fachada).to_excel(writer, sheet_name="V.Fachada",index=False)
        if metros_baranda:
           pd.DataFrame(metros_baranda).to_excel(writer, sheet_name="Barandas",index=False)
    print("Archivo de excel creado correctamente")

def main():
    ###Todas estas listas que se crearon solo para almacenar los datos que nos arroja las funciones
    ###del menu.
    muros_ladrillo=[]
    muros_fachada=[]
    ventanas_ladrillo=[]
    ventanas_fachada=[]
    metros_baranda=[]
    total_ladrillo=0
    total_fachada=0
    
    print("="*50)
    print ("    BIENVENIDO A LA CALCULADORA DE CANTIDADES")
    print("="*50)
    while True:
        ###El ciclo siempre se cumplira siempre que el usuario no desee salir del programa, por eso se
        ###le añade la funcion al final de salir para poder romper el ciclo.
        print("MENU")
        print("Seleccione una opcion:")
        print("1. Calculo de area de ladrillo.")
        print("2. Calculo de area en graniplast u otro acabado.")
        print("3. Calculo de ventanas.")
        print("4. Calculo de metros lineales en barandas")
        print("5. Mostrar resumen: ")
        print("6. Eliminar algun elemento: ")
        print("7. Modificar algun elemento: ")
        print("8. Mostrar resumen descontando areas de ventanas: ")
        print("9. Exportar a Excel")
        print("0. Salir")
        ###Debido a que es el menu principal, se agrego esta funcion para que el usuario no pueda salir
        ###salir del menu a pesar de que haya puesto un numero erroneo.
        try: 
            opcion=int(input("Seleccione una opcion: "))
        except ValueError:
            print ("Por favor ingrese un numero valido")
            continue
        ###Las opciones de la 1 a la 4 practicamente sirven para reescribir todo lo que me retorna la funcion
        ###y meterlo dentro de una variable que esta ubicada en mi funcion principal.
        if opcion==1:
            nuevos=area_ladrillo()
            muros_ladrillo.extend(nuevos)
        elif opcion==2:
            fachada_nueva=area_fachada()
            muros_fachada.extend(fachada_nueva)
        elif opcion==3:
             v_ladrillo,v_fachada=area_ventana()
             ventanas_ladrillo.extend(v_ladrillo)
             ventanas_fachada.extend(v_fachada)               
        elif opcion==4:
            nuevo_baranda=metro_baranda()
            metros_baranda.extend(nuevo_baranda)
        elif opcion==5:
        ###Esta funcion va a recolectar todos los datos para organizados para mostrarle al usuario hasta ahora 
        ###todo lo que ha ingresado en el programa. Practicamente esta es la informacion que se exporta a excel
        ###a menos de que el usuario haya decidido modificar o eliminar algun datos.
            resumen_area_ladrillo(muros_ladrillo)
            resumen_fachada(muros_fachada)
            resumen_ventana(ventanas_ladrillo,ventanas_fachada)
            resumen_baranda(metros_baranda)
        ###Para esta opcion le daremos al usuario la decision de si quiere eliminar algun dato que no corresponda
        ###o si bien algo que este mal.
        elif opcion==6:
            eliminar_lista(muros_ladrillo,muros_fachada,ventanas_ladrillo,ventanas_fachada,metros_baranda)
        ###Si solo quiere modificar un valor en especifico utilizara esta opcion, no incluye ventanas debido a
        ###que son varios datos que debe ingresar y se considero mejor opcion borrar la lista exacta antes de
        ###modificar un pequeño dato.
        elif opcion==7:
            modificar_elemento(muros_ladrillo,muros_fachada,ventanas_ladrillo,ventanas_fachada,metros_baranda)
        ###Esta opcion permite al usuario conocer los resultados de las areas una vez que se hayan descontado 
        ###las ventanas. 
        elif opcion==8:
            t1=resumen_area_ladrillo(muros_ladrillo)
            t2=resumen_fachada(muros_fachada)
            t3,_=resumen_ventana(ventanas_ladrillo,ventanas_fachada)
            _,t4=resumen_ventana(ventanas_ladrillo,ventanas_fachada)
            if t1 or t2:
                total_ladrillo=t1-t3
                total_fachada=t2-t4
                print(f"El area total de ladrillo descontando ventanas={total_ladrillo}m2")
                print(f"El area total de pintura descontando ventanas={total_fachada}m2") 
            else: 
                print("No se puede hacer calculos sin los datos completos")
        ###Esta opcion sirve para exportar a excel en caso de querer trabajarlo desde otro programa.
        elif opcion==9:
            exportar_excel(muros_ladrillo,muros_fachada,ventanas_ladrillo,ventanas_fachada,metros_baranda)
        ### Esta opcion viene siendo la salida del programa.
        elif opcion==0:
            print("Saliendo...")
            print("Adios")
            break
        else:
            print("Opcion invalida, intente de nuevo")
###Con esta funcion sabremos cual es el area del ladrillo a partir de los datos ingresados por el usuario
def area_ladrillo():
    print("CALCULO DE AREA DE LADRILLO")
    ###Se creo uan variable para almacenar los datos que arrojara el calculo de ladrillo
    muros=[]
    while True:
        nombre=input("Nombre de la fachada o identificacion: (Area ladrillo Fachada Norte 1): ")
        print("Digite las dimensiones: ")
        
        altura_pisos=0
        largo=float(input("Largo (m): "))
        altura_pisos=input("Desea calcular la altura por numero de pisos (s/n): ").lower()
        ###Se le daran 2 alternativas al usuario, si prefiere calcular la altura manualmente o si bien
        ###desde un aproximado del numero de pisos del edificio.
        if altura_pisos=="s":
            print("Altura tipica de piso 2.5m")
            pisos=0
            pisos=int(input("Cuantos pisos tiene el edificio: "))
            altura=pisos*2.5
            print(f"Altura (m)={altura}")
        elif altura_pisos=="n":
            print("Digite la altura manualmente: ")
            altura=float(input("Altura: "))
        else: 
            print("Opcion invalida, intente de nuevo")
        ###En esta seccion se añadira todos los datos registrados por el usuario y los calculos automaticos
        ###que hace el programa.
        area=largo * altura
        muros.append({
            "nombre":nombre,
            "largo":largo,
            "altura":altura,
            "area":area,
        })
        ###Se le dara la opcion de añadir de una vez otra seccion de muro en dado caso de que sean continuas 
        ###o haya alguna dificultad para medirla toda completa.
        print(f"Area calculada: {area:.2f} m²")
        continuar=input("Desea agregar otro muro(s/n): ").lower()
        if continuar != "s":
            break
    ###Se le dara un resumen de todo lo que se ha calculado y lo que el usuario ingreso para que valide.
    print("Resumen de areas")
    total=0
    for i, muro in enumerate(muros, start=1):
        print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
        total=total+muro["area"]
    print(f"Area total= {total:.2f} m2")
    input("Presione enter para volver al menu")
    return muros
###Esta funcion le permite al usuario revisar que ha sido todo lo que ha ingresado.
def resumen_area_ladrillo(muros_ladrillo):
    if not muros_ladrillo:
        print("No hay datos registrados de areas de ladrillo")
        return 0
    print("Resumen de areas Ladrillo")
    total=0
    for i, muro in enumerate(muros_ladrillo, start=1):
        print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
        total=total+muro["area"]
    print(f"Area total= {total:.2f} m2")
    input("Presione enter para volver al menu")
    return total
###Funciona exactamente igual que la de ladrillo pero en esta se tomara solo la parte de la pintura        
def area_fachada():
    fachada=[]
    print("CALCULO AREA DE FACHADA PINTURA")
    while True:
        try: 
            nombre=input("Digite el nombre de la fachada (Ej: Fachada Norte 1): ")
            print("Digite las dimensiones: ")
            largo=float(input("Largo(m): "))
            altura_pisos=input("Desea calcular la altura por numero de pisos(s/n): ").lower()
            if altura_pisos=="s":
                print("Altura tipica de piso 2.5m")
                pisos=int(input("Cuantos pisos tiene el edificio: "))
                altura=pisos*2.5
            elif altura_pisos=="n":
                altura=float(input("Digita la altura manualmente: "))
            else: 
                print("Opcion invalida")
        except ValueError:
            print ("Por favor ingrese un numero valido")
            continue
        area=largo * altura
        fachada.append({
            "nombre":nombre,
            "largo":largo,
            "altura":altura,
            "area":area,
        })
        print(f"Area calculada: {area:.2f} m²")
        continuar=input("Desea agregar otro muro(s/n): ").lower()
        if continuar != "s":
            break
    if continuar.lower() == "n":
        print("Resumen de areas de fachada de pintura")
        total=0
        for i, muro in enumerate(fachada, start=1):
            print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
            total=total+muro["area"]
        print(f"Area total= {total:.2f} m2")
        input("Presione enter para volver al menu")
    return fachada
def resumen_fachada(muros_fachada):
    if not muros_fachada:
        print("No hay datos registrados de areas de pintura")
        return 0
    print("Resumen de area fachada en pintura")
    total=0
    for i, muro in enumerate(muros_fachada, start=1):
        print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
        total=total+muro["area"]
    print(f"Area total= {total:.2f} m2")
    input("Presione enter para volver al menu")
    return total
###Para esta funcion si la dividiremos en dos:
### 1. Ladrillo: Solo las ventanas que queden ubiacadas en la parte de ladrillo
### 2. Fachada: Solo las ventanas que queden ubicadas en la parte de la pintura u otro acabado.
def area_ventana():
    print("CALCULO DE AREA DE VENTANA")
    ventana_ladrillo=[]
    ventana_fachada=[]
    while True:
        print("A que material pertenece la ventana, seleccione una opcion: ")
        ventana=int(input("(1. Ladrillo) (2.Fachada): ")) 
        if ventana==1:
            nombre=input("Digite el nombre de la ventana ubicada en la fachada de ladrillo: ")
            print("Digite las dimensiones: ")
            largo=float(input("Largo(m): "))
            altura=float(input("Altura(m): "))
            perimetro_n=largo+2*altura
            perimetro_o=(largo+altura)*2
            area=largo*altura
            print(f"Area de una ventana: {area}m2")
            print(f"Metro lineal de una ventana en N: {perimetro_n}m")
            print(f"Metro lineal de una ventana en O: {perimetro_o}m")
            print("Digite el numero de pisos y ventanas por piso en la fachada: ")
            ###En este calculo solo necesitamos el numero de pisos que habran por ventana ademas de que si 
            ###son ventanas que se repiten. Tendremos resultados de area y perimetro tanto en forma de "N" y "O"
            pisos=int(input("Numero de pisos: "))
            n_ventanas=int(input("Numero de ventanas por piso: "))
            l_area_ventana=area*n_ventanas*pisos
            l_perimetro_ventana_n=perimetro_n*n_ventanas*pisos
            l_perimetro_ventana_o=perimetro_o*n_ventanas*pisos
            print(f"El area total de las ventanas en la fachada de ladrillo es igual: {l_area_ventana:.2f} m2")
            print(f"Los metros lineales en N de todas las ventanas en la fachada de ladrillo es igual: {l_perimetro_ventana_n:.2f} m")
            print(f"Los metros lineales en O de todas las ventanas en la fachada de ladrillo es igual: {l_perimetro_ventana_o:.2f} m")
            ventana_ladrillo.append({
                    "nombre":nombre,
                    "largo":largo,
                    "altura":altura,
                    "area (1 ventana)":area,
                    "Perimetro N (1 Ventana)":perimetro_n,
                    "Perimetro O (1 Ventana)":perimetro_o,
                    "area total":l_area_ventana,
                    "Perimetro N total":l_perimetro_ventana_n,
                    "Perimetro O total":l_perimetro_ventana_o,
                })
            continuar=input("Desea agregar otro tipo de ventana(s/n): ").lower()
            if continuar.lower() != "s":
                break
        if ventana==2:
            nombre=input("Digite el nombre de la ventana ubicada en la fachada de pintura: ")
            print("Digite las dimensiones: ")
            largo=float(input("Largo(m): "))
            altura=float(input("Altura(m): "))
            area=largo*altura
            perimetro_n=largo+2*altura
            perimetro_o=(largo+altura)*2
            print(f"Area de una ventana: {area}")
            print(f"Metro lineal de una ventana en N: {perimetro_n}")
            print(f"Metro lineal de una ventana en O: {perimetro_o}")
            print("Digite el numero de pisos y ventanas por piso en la fachada: ")
            pisos=int(input("Numero de pisos: "))
            n_ventanas=int(input("Numero de ventanas por piso: "))
            f_area_ventana=area*n_ventanas*pisos
            f_perimetro_ventana_n=perimetro_n*n_ventanas*pisos
            f_perimetro_ventana_o=perimetro_o*n_ventanas*pisos
            print(f"El area total de las ventanas en la fachada es igual: {f_area_ventana:.2f} m2")
            print(f"Los metros lineales en N de todas las ventanas en la fachada de ladrillo es igual: {f_perimetro_ventana_n:.2f} m")
            print(f"Los metros lineales en O de todas las ventanas en la fachada de ladrillo es igual: {f_perimetro_ventana_o:.2f} m")
            ventana_fachada.append({
                    "nombre":nombre,
                    "largo":largo,
                    "altura":altura,
                    "area (1 ventana)":area,
                    "Perimetro N (1 Ventana)":perimetro_n,
                    "Perimetro O (1 Ventana)":perimetro_o,
                    "area total":f_area_ventana,
                    "Perimetro N total":f_perimetro_ventana_n,
                    "Perimetro O total":f_perimetro_ventana_o,  
                    })  
            continuar=input("Desea agregar otro tipo de ventana(s/n): ").lower()
            if continuar.lower() != "s":
                break
    print("Resumen area ventanas ladrillo")
    total_area_l=0
    total_p_n=0
    total_p_o=0
    for i,ven in enumerate(ventana_ladrillo,start=1):
        print(f"{i}.,{ven['nombre']}:,Largo(m): {ven['largo']},Altura(m): {ven['altura']}:,Area (m2)(1 ventana): {ven['area (1 ventana)']},Perimetro N(m)(1 Ventana): {ven['Perimetro N (1 Ventana)']},Perimetro O(m)(1 Ventana): {ven['Perimetro O (1 Ventana)']},Area total(m2): {ven['area total']},Perimetro N total(m): {ven['Perimetro N total']},Perimetro O total(m): {ven['Perimetro O total']}")
        total_area_l=total_area_l+ven["area total"]
        total_p_n=total_p_o=total_p_n+ven["Perimetro N total"]
        total_p_o=total_p_o+ven["Perimetro O total"]
    print(f"Area total= {total_area_l:.2f} m2")
    print(f"Perimetro total N= {total_p_n:.2f} m")
    print(f"Perimetro total O= {total_p_o:.2f} m")
    input("Presione enter para volver al menu")

    print("Resumen area ventanas fachada pintura")
    total_area_f=0
    total_p_n=0
    total_p_o=0
    for i,ven in enumerate(ventana_fachada,start=1):
        print(f"{i}.,{ven['nombre']}:,Largo(m): {ven['largo']},Altura(m): {ven['altura']}:,Area (m2)(1 ventana): {ven['area (1 ventana)']},Perimetro N(m)(1 Ventana): {ven['Perimetro N (1 Ventana)']},Perimetro O(m)(1 Ventana): {ven['Perimetro O (1 Ventana)']},Area total(m2): {ven['area total']},Perimetro N total(m): {ven['Perimetro N total']},Perimetro O total(m): {ven['Perimetro O total']}")
        total_area_f=total_area_f+ven["area total"]
        total_p_n=total_p_o=total_p_n+ven["Perimetro N total"]
        total_p_o=total_p_o+ven["Perimetro O total"]
    print(f"Area total= {total_area_f:.2f} m2")
    print(f"Perimetro total N= {total_p_n:.2f} m")
    print(f"Perimetro total O= {total_p_o:.2f} m")
    input("Presione enter para volver al menu")
    return ventana_ladrillo, ventana_fachada
def resumen_ventana(ventanas_ladrillo,ventanas_fachada):
    if not ventanas_ladrillo and not ventanas_fachada:
        print("No hay datos registrados de areas de ventana")
        return 0,0
    if ventanas_ladrillo:
        print("Resumen area ventanas ladrillo")
    total_area_l=0
    total_p_n=0
    total_p_o=0
    for i,ven in enumerate(ventanas_ladrillo,start=1):
        print(f"{i}.,{ven['nombre']}:,Largo(m): {ven['largo']},Altura(m): {ven['altura']}:,Area (m2)(1 ventana): {ven['area (1 ventana)']},Perimetro N(m)(1 Ventana): {ven['Perimetro N (1 Ventana)']},Perimetro O(m)(1 Ventana): {ven['Perimetro O (1 Ventana)']},Area total(m2): {ven['area total']},Perimetro N total(m): {ven['Perimetro N total']},Perimetro O total(m): {ven['Perimetro O total']}")
        total_area_l=total_area_l+ven["area total"]
        total_p_n=total_p_o=total_p_n+ven["Perimetro N total"]
        total_p_o=total_p_o+ven["Perimetro O total"]
    print(f"Area total= {total_area_l:.2f} m2")
    print(f"Perimetro total N= {total_p_n:.2f} m")
    print(f"Perimetro total O= {total_p_o:.2f} m")
    input("Presione enter para volver al menu")
    if ventanas_fachada:
        print("Resumen area ventanas fachada pintura")
    total_area_f=0
    total_p_n=0
    total_p_o=0
    for i,ven in enumerate(ventanas_fachada,start=1):
        print(f"{i}.,{ven['nombre']}:,Largo(m): {ven['largo']},Altura(m): {ven['altura']}:,Area (m2)(1 ventana): {ven['area (1 ventana)']},Perimetro N(m)(1 Ventana): {ven['Perimetro N (1 Ventana)']},Perimetro O(m)(1 Ventana): {ven['Perimetro O (1 Ventana)']},Area total(m2): {ven['area total']},Perimetro N total(m): {ven['Perimetro N total']},Perimetro O total(m): {ven['Perimetro O total']}")
        total_area_f=total_area_f+ven["area total"]
        total_p_n=total_p_o=total_p_n+ven["Perimetro N total"]
        total_p_o=total_p_o+ven["Perimetro O total"]
    print(f"Area total= {total_area_f:.2f} m2")
    print(f"Perimetro total N= {total_p_n:.2f} m")
    print(f"Perimetro total O= {total_p_o:.2f} m")
    input("Presione enter para volver al menu")
    return total_area_l, total_area_f
###Con esta funcion sabremos el total de metros lineales que tienen las barandas.            
def metro_baranda():
    baranda=[]
    while True:
        nombre=input("Digite el nombre de la baranda: ")
        largo=float(input("Cual es el largo de la baranda (m): "))
        ###En este calculo debido a como son las barandas, es decir las secciones seran el numero de 
        ###partes que tengan en el balcon y el largo siempre sera el mismo, solo se neceistara saber
        ###la medida de ese largo y las secciones que posee un balcon.
        seccion=float(input("Cuantas secciones tiene la baranda: "))
        continuar=input("Quiere añadir otro tipo de baranda (s/n): ")
        metro=largo*seccion
        ###Igual que en los otros casos en la mayoria de casos los balcones no varian por lo que solamente
        ###necesitaremos el numero de pisos para saber el total de metros lineales.
        pisos=int(input("En cuantos pisos hay baranda: "))
        m_lineal=metro*pisos
        print(f"Los metros lineales de la baranda son {m_lineal}m") 
        baranda.append({
            "nombre":nombre,
            "largo":largo,
            "seccion":seccion,
            "pisos":pisos,
            "m_lineal":m_lineal,
        })
        if continuar !="s":
            break
    print("Resumen Metros lineales de baranda ")
    total=0
    for i,bar in enumerate(baranda, start=1):
        print(f"{i}.,{bar['nombre']},Largo(m){bar['largo']},Secciones: {bar['seccion']},Pisos: {bar['pisos']},Metro lineal(m): {bar['m_lineal']}")
        total=total+bar['m_lineal']
    print(f"Total de metros lineales= {total:.2f}m")
    print("Presione enter para volver al menu")
    return baranda
def resumen_baranda(metros_baranda):
    if not metros_baranda:
        print("No hay datos registrados de baranda")
        return
    print("Resumen Metros lineales de baranda ")
    total=0
    for i,bar in enumerate(metros_baranda, start=1):
        print(f"{i}.,{bar['nombre']},Largo(m){bar['largo']},Secciones: {bar['seccion']},Pisos: {bar['pisos']},Metro lineal(m): {bar['m_lineal']}")
        total=total+bar['m_lineal']
    print(f"Total de metros lineales= {total:.2f}m")
    print("Presione enter para volver al menu")    
###Se le dara la opcion al usuario de eliminar algun dato mal ingresado o si quiere modificar uno completo
###solo se le da la opcion de elimianrlo de acuerdo al nombre que ingreso.
def eliminar_lista(muros_ladrillo,muros_fachada,ventanas_ladrillo,ventanas_fachada,metros_baranda):
    print("Que desea eliminar? ")
    print("Seleccione una opcion: ")
    print("1.Muros de ladrillo")
    print("2.Muros de pintura")
    print("3.Ventanas ubicadas en la parte de ladrillo")
    print("4.Ventanas ubicadas en la parte de pintura")
    print("5.Barandas")
    print("0.Cancelar")
    opcion=int(input("Opcion: "))
    if opcion==1:
        lista=muros_ladrillo
        nombre_lista="muros de ladrillo"
    elif opcion==2:
        lista=muros_fachada
        nombre_lista="muros de fachada"
    elif opcion==3:
        lista=ventanas_ladrillo
        nombre_lista="ventanas de ladrillo"
    elif opcion==4:
        lista=ventanas_fachada
        nombre_lista="ventanas de pintura"
    elif opcion==5:
        lista=metros_baranda
        nombre_lista="Barandas"
    elif opcion==0:
        print("Cancelado")
        return
    else: 
        print("Opcion invalida")
        return
    
    if not lista:
        print("No hay datos registrados aun para eliminar")
        return
    print(f"Elementos Actuales en {nombre_lista}")
    for i, muro in enumerate(lista, start=1):
        print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
    nombre_eliminar=input("Ingrese el nombre exacto del elemento a eliminar: ").strip()
    encontrado=None
    for muro in lista:
        if nombre_eliminar.lower()==muro["nombre"].lower():
            encontrado=muro
            break
    if encontrado:
        lista.remove(encontrado)
        print(f"Se elimino correctamente de {nombre_lista} el elemento '{nombre_eliminar}' ")
    else:
        print("No se encontro elemento que coincida con ese nombre ")
    if lista:
        print(f"{nombre_lista} lista actualizada")
        for i, muro in enumerate(lista,start=1):
            print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
    else:
        print(f"La lista de {nombre_lista} se encuentra vacio.")
###Igual que en el anterior se le da la opcion al usuario por si comete algun error, solo se le dara 
###la opcion al usuario de cambiar las cosas que el mismo ingreso.
def modificar_elemento(muros_ladrillo,muros_fachada,ventanas_ladrillo,ventanas_fachada,metros_baranda):
    print("Que desea modificar? ")
    print("Seleccione una opcion: ")
    print("1.Muros de ladrillo")
    print("2.Muros de pintura")
    print("3.Barandas")
    print("0.Cancelar")
    opcion=int(input("Opcion: "))
    if opcion==1:
        lista=muros_ladrillo
        nombre_lista="muros de ladrillo"
    elif opcion==2:
        lista=muros_fachada
        nombre_lista="muros de fachada"
    elif opcion==3:
        lista=metros_baranda
        nombre_lista="Barandas"
    elif opcion==0:
        print("Cancelado")
        return
    else: 
        print("Opcion invalida")
        return
    if not lista:
        print("No hay elementos para modificar")
        return
    for i, muro in enumerate(lista,start=1):
        print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
        print(f"Que elemento de {nombre_lista} desea modificar")
        print("1.Nombre")
        print("2.Largo")
        print("3.Altura")
        elem=int(input("Opcion: "))
        if elem==1:
            nombre_mod=input("Ingrese el nombre que desea modificar: ").strip()
            if nombre_mod.lower()==muro["nombre"].lower():
                nombre_nuevo=input("Ingrese el nuevo nombre: ")
                muro["nombre"]=nombre_nuevo
                print("Modificacion con exito")
                if "altura" in muro and "area" in muro and not "Perimetro N (1 Ventana)" in muro: 
                    for i, muro in enumerate(lista,start=1):
                        print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
                elif "Perimetro N (1 Ventana)" in muro:
                    for i, ven in enumerate(lista,start=1):
                        print(f"{i}.,{ven['nombre']}:,Largo(m): {ven['largo']},Altura(m): {ven['altura']}:,Area (m2)(1 ventana): {ven['area (1 ventana)']},Perimetro N(m)(1 Ventana): {ven['Perimetro N (1 Ventana)']},Perimetro O(m)(1 Ventana): {ven['Perimetro O (1 Ventana)']},Area total(m2): {ven['area total']},Perimetro N total(m): {ven['Perimetro N total']},Perimetro O total(m): {ven['Perimetro O total']}")
                elif "seccion" in muro:
                    for i,bar in enumerate(lista, start=1):
                        print(f"{i}.,{bar['nombre']},Largo(m){bar['largo']},Secciones: {bar['seccion']},Pisos: {bar['pisos']},Metro lineal(m): {bar['m_lineal']}")     
            else:
                print("Ningun nombre coincide con el ingresado")
        elif elem==2:
            nombre_mod=input("Ingrese el nombre que desea modificar: ").strip()
            largo_nuevo=float(input("Ingrese el nuevo largo: "))
            if nombre_mod.lower()==muro["nombre"].lower():
                muro["largo"]=largo_nuevo
                if "altura" in muro:
                    muro["area"]=muro["largo"]*muro["altura"]
                    for i, muro in enumerate(lista,start=1):
                        print(f"Lista actualizada de {nombre_lista}")
                        print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
            else:
                print("Ningun nombre coincide con el ingresado")
        elif elem==3:
            nombre_mod=input("Ingrese el nombre que desea modificar: ").strip()
            altura_nuevo=float(input("Ingrese la nueva altura: "))
            if nombre_mod.lower()==muro["nombre"].lower():
                muro["altura"]=altura_nuevo
                if "largo" in muro:
                    muro["area"]=muro["largo"]*muro["altura"]
                    for i, muro in enumerate(lista,start=1):
                        print(f"Lista actualizada de {nombre_lista}")
                        print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
            else:
                print("Ningun nombre coincide con el ingresado")
        else:
            print("Opcion invalida")
            return

                                  
if __name__ == "__main__":
    main()