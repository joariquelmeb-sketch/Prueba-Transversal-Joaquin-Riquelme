planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}

inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15]
}



def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida (ingrese un número entero)")

def buscar_codigo(codigo, dicc_inscripciones):
    
    return codigo.upper() in [k.upper() for k in dicc_inscripciones.keys()]

def cupos_tipo(tipo, dicc_planes, dicc_inscripciones):
    tipo_buscado = tipo.lower()
    total_cupos = 0
    
    for cod_plan, datos in dicc_planes.items():
        if datos[1].lower() == tipo_buscado:
            for k_insc, v_insc in dicc_inscripciones.items():
                if k_insc.upper() == cod_plan.upper():
                    total_cupos += v_insc[1]
                    
    print(f"El total de cupos disponibles es: {total_cupos}")

def busqueda_precio(p_min, p_max, dicc_planes, dicc_inscripciones):
    if p_min < 0 or p_max < 0 or p_min > p_max:
        print("No hay planes en ese rango de precios.")
        return

    resultados = []
    for cod_plan, datos_insc in dicc_inscripciones.items():
        precio = datos_insc[0]
        cupos = datos_insc[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            nombre_plan = ""
            for k_plan, v_plan in dicc_planes.items():
                if k_plan.upper() == cod_plan.upper():
                    nombre_plan = v_plan[0]
                    break
            
            resultados.append(f"{nombre_plan}--{cod_plan}")
            
    if resultados:
      
        resultados.sort()
        print(f"Los planes encontrados son: {resultados}")
    else:
        print("No hay planes en ese rango de precios.")

def actualizar_precio(codigo, nuevo_precio, dicc_inscripciones):
    if not buscar_codigo(codigo, dicc_inscripciones):
        return False
        
    for k in dicc_inscripciones.keys():
        if k.upper() == codigo.upper():
            dicc_inscripciones[k][0] = nuevo_precio
            return True
    return False

def eliminar_plan(codigo, dicc_planes, dicc_inscripciones):
    if not buscar_codigo(codigo, dicc_inscripciones):
        return False
        
    for k in list(dicc_inscripciones.keys()):
        if k.upper() == codigo.upper():
            del dicc_inscripciones[k]
            
    for k in list(dicc_planes.keys()):
        if k.upper() == codigo.upper():
            del dicc_planes[k]
            
    return True

def validar_codigo(codigo, dicc_planes):
    if not codigo or codigo.isspace():
        return False
    return not buscar_codigo(codigo, dicc_planes)

def validar_nombre(nombre):
    return bool(nombre and not nombre.isspace())

def validar_tipo(tipo):
    return tipo in ['mensual', 'trimestral', 'anual']

def validar_duracion(duracion):
    try:
        val = int(duracion)
        return val > 0
    except ValueError:
        return False

def validar_piscina(opcion):
    return opcion.lower() in ['s', 'n']

def validar_clases(opcion):
    return opcion.lower() in ['s', 'n']

def validar_horario(horario):
    return bool(horario and not horario.isspace())

def validar_precio(precio):
    try:
        val = int(precio)
        return val > 0
    except ValueError:
        return False

def validar_cupos(cupos):
    try:
        val = int(cupos)
        return val >= 0
    except ValueError:
        return False

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, dicc_planes, dicc_inscripciones):
    if buscar_codigo(codigo, dicc_inscripciones):
        return False
    
  
    piscina_bool = True if acceso_piscina.lower() == 's' else False
    clases_bool = True if incluye_clases.lower() == 's' else False
    
    cod_key = codigo.upper()
    dicc_planes[cod_key] = [nombre, tipo, int(duracion), piscina_bool, clases_bool, horario]
    dicc_inscripciones[cod_key] = [int(precio), int(cupos)]
    return True

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")

def main():
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            tipo = input("Ingrese tipo de plan a consultar: ")
            cupos_tipo(tipo, planes, inscripciones)
            
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, planes, inscripciones)
            
        elif opcion == 3:
            while True:
                codigo = input("Ingrese código del plan: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio <= 0:
                        print("El precio debe ser un número entero mayor que cero.")
                        continue
                except ValueError:
                    print("Debe ingresar un valor entero válido.")
                    continue
                
                if actualizar_precio(codigo, nuevo_precio, inscripciones):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                    
                resp = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                if resp != 's':
                    break
                    
        elif opcion == 4:
            cod = input("Ingrese código del plan: ")
            nom = input("Ingrese nombre del plan: ")
            tip = input("Ingrese tipo (mensual/trimestral/anual): ")
            dur = input("Ingrese duración (meses): ")
            pis = input("¿Incluye acceso a piscina? (s/n): ")
            cla = input("¿Incluye clases grupales? (s/n): ")
            hor = input("Ingrese horario: ")
            pre = input("Ingrese precio: ")
            cup = input("Ingrese cupos: ")
            
            if not validar_codigo(cod, planes):
                print("Error: Código inválido o ya existente.")
            elif not validar_nombre(nom):
                print("Error: El nombre no puede estar vacío.")
            elif not validar_tipo(tip):
                print("Error: Tipo debe ser 'mensual', 'trimestral' o 'anual'.")
            elif not validar_duracion(dur):
                print("Error: La duración debe ser un entero mayor que cero.")
            elif not validar_piscina(pis):
                print("Error: Respuesta de piscina inválida (s/n).")
            elif not validar_clases(cla):
                print("Error: Respuesta de clases inválida (s/n).")
            elif not validar_horario(hor):
                print("Error: El horario no puede estar vacío.")
            elif not validar_precio(pre):
                print("Error: El precio debe ser un entero mayor que cero.")
            elif not validar_cupos(cup):
                print("Error: Los cupos deben ser un entero mayor o igual a cero.")
            else:
                if agregar_plan(cod, nom, tip, dur, pis, cla, hor, pre, cup, planes, inscripciones):
                    print("Plan agregado")
                else:
                    print("El código ya existe")
                    
        elif opcion == 5:
            codigo = input("Ingrese código del plan a eliminar: ")
            if eliminar_plan(codigo, planes, inscripciones):
                print("Plan eliminado")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()
