##Calculadora de cantidades
##Elaborado por: Juan Sebastian Leal 
def main():
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
        print("MENU")
        print("Seleccione una opcion:")
        print("1. Calculo de area de ladrillo.")
        print("2. Calculo de area en graniplast u otro acabado.")
        print("3. Calculo de ventanas.")
        print("4. Calculo de metros lineales en barandas")
        print("5. Mostrar resumen: ")
        print("6. Modificar o eliminar algun elemento: ")
        print("7. Mostrar resumen descontando areas de ventanas: ")
        print("8.Importar a Excel")
        print("0. Salir")
        try: 
            opcion=int(input("Seleccione una opcion: "))
        except ValueError:
            print ("Por favor ingrese un numero valido")
            continue
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
            resumen_area_ladrillo(muros_ladrillo)
            resumen_fachada(muros_fachada)
            resumen_ventana(ventanas_ladrillo,ventanas_fachada)
            resumen_baranda(metros_baranda)
        elif opcion==7:
            t1=resumen_area_ladrillo(muros_ladrillo)
            t2=resumen_fachada(muros_fachada)
            t3,_=resumen_ventana(ventanas_ladrillo,ventanas_fachada)
            _,t4=resumen_ventana(ventanas_ladrillo,ventanas_fachada)
            if total_ladrillo and total_fachada:
                total_ladrillo=t1-t3
                total_fachada=t2-t4
                print(f"El area total de ladrillo descontando ventanas={total_ladrillo}m2")
                print(f"El area total de fachada en pintura descontando ventanas={total_fachada}m2")
            else: 
                print("No se puede hacer calculos sin datos")

        elif opcion==0:
            print("Saliendo...")
            print("Adios")
            break
        else:
            print("Opcion invalida, intente de nuevo")
def area_ladrillo():
    print("CALCULO DE AREA DE LADRILLO")
    muros=[]
    while True:
        nombre=input("Nombre de la fachada o identificacion: (Area ladrillo Fachada Norte 1):")
        print("Digite las dimensiones: ")
        
        altura_pisos=0
        largo=float(input("Largo (m): "))
        altura_pisos=input("Desea calcular la altura por numero de pisos (s/n)").lower()
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
        area=largo * altura
        muros.append({
            "nombre":nombre,
            "largo":largo,
            "altura":altura,
            "area":area,
        })
        print(f"Area calculada: {area:.2f} m²")
        continuar=input("Desea agregar otro muro(s/n)").lower()
        if continuar != "s":
            break
    print("Resumen de areas")
    total=0
    for i, muro in enumerate(muros, start=1):
        print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
        total=total+muro["area"]
    print(f"Area total= {total:.2f} m2")
    input("Presione enter para volver al menu")
    return muros
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
        
def area_fachada():
    fachada=[]
    print("CALCULO AREA DE FACHADA PINTURA")
    while True:
        try: 
            nombre=input("Digite el nombre de la fachada (Ej: Fachada Norte 1): ")
            print("Digite las dimensiones: ")
            largo=float(input("Largo(m): "))
            altura_pisos=input("Desea calcular la altura por numero de pisos(s/n) ").lower()
            if altura_pisos=="s":
                altura=altura_pisos*2.5
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
        continuar=input("Desea agregar otro muro(s/n)").lower()
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
        return
    print("Resumen de area fachada en pintura")
    total=0
    for i, muro in enumerate(muros_fachada, start=1):
        print(f"{i}.{muro['nombre']}:,Largo: {muro['largo']} m:,Altura: {muro['altura']} m:,Area: {muro['area']} m2")
        total=total+muro["area"]
    print(f"Area total= {total:.2f} m2")
    input("Presione enter para volver al menu")
    return total

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
            print(f"Area de una ventana: {area}")
            print(f"Metro lineal de una ventana en N: {perimetro_n}")
            print(f"Metro lineal de una ventana en O: {perimetro_o}")
            print("Digite el numero de pisos y ventanas por piso en la fachada: ")
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
            
def metro_baranda():
    baranda=[]
    while True:
        nombre=input("Digite el nombre de la baranda: ")
        largo=float(input("Cual es el largo de la baranda (m): "))
        seccion=float(input("Cuantas secciones tiene la baranda: "))
        continuar=input("Quiere añadir otro tipo de baranda (s/n): ")
        metro=largo*seccion
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


    
    
    
    

if __name__ == "__main__":
    main()