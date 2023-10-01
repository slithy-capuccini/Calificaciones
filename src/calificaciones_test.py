import calificaciones
import calificaciones_ui
if __name__=="__main__":
    #a
    print(f"Esto es a")
    print(calificaciones.nota_media([9.1,7.2]))
    print(calificaciones.nota_media([4.0,6.0]))
    print(calificaciones.nota_media([4.0,3.0]))
    print(calificaciones.nota_media([None,3.0]))
    print(calificaciones.nota_media([9.0,None]))
    #b
    print(f"Esto es b")
    print(calificaciones.nota_cuatrimestre((9.1,7.2),8.1))
    print(calificaciones.nota_cuatrimestre((4.0,6.0),5.0))
    print(calificaciones.nota_cuatrimestre((4.0,3.0),None))
    print(calificaciones.nota_cuatrimestre((None,3.0),None))
    print(calificaciones.nota_cuatrimestre((9.0,None),4.5))
    #c
    print(f"Esto es c")
    print(calificaciones.nota_continua((9.6, 9.9,10.0, 9.8),(9.7,9.5)))
    print(calificaciones.nota_continua((4.4, 4.9, 5.1, 4.7),(4.6,4.8)))
    print(calificaciones.nota_continua((4.0, 6.0, 4.0, 3.0),(5.0, None)))
    print(calificaciones.nota_continua((9.0, None, 4.0, 3.0),(4.5, None)))
    #d
    print(f"Esto es d")
    calificaciones_ui.solicita_notas()
