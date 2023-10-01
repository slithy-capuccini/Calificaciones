import calificaciones
def solicita_notas():
    nombre=input("Introduzca su nombre: ")
    notas_teoria=[input(f"Introduce su nota del examen teórico número {i}: ") for i in range(4)]
    notas_teoria=calificaciones.convert_to_float(notas_teoria)
    notas_practica=[input(f"Introduce su nota del examen teórico número {i}: ") for i in range(2)]
    notas_practica=calificaciones.convert_to_float(notas_practica)
    mostrar_notas(nombre,notas_teoria,notas_practica)
def mostrar_notas(name,tupla_t,tupla_p):
    print(f"Hola {name}")
    print("Tus notas del primer cuatrimestre son:")
    teoria1=calificaciones.nota_media(tupla_t[:2])
    practica1=tupla_p[0]
    cuatri1=calificaciones.nota_cuatrimestre(tupla_t[:2],tupla_p[0])
    print(f"teoria {teoria1}, practica {practica1}, cuatrimestre {cuatri1}")
    print("Tus notas del primer cuatrimestre son:")
    teoria2=calificaciones.nota_media(tupla_t[2:])
    practica2=tupla_p[1]
    cuatri2=calificaciones.nota_cuatrimestre(tupla_t[2:],tupla_p[1])
    print(f"teoria {teoria2}, practica {practica2}, cuatrimestre {cuatri2}")
    nota_final=calificaciones.nota_media([cuatri1,cuatri2])
    print(f"Tu nota final de la asignatura es {nota_final}")