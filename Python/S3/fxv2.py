listaPersonas=[]
dictPersonas={
    "nombe":'',
    "dni":'',
    "cursos":""
}
def statusPersona(age):
    year=2024    
    if year-age<18:
        return False
    else:
        return True

def agregarPersona():
    nombre= input("ingrese su nombre")
    dni= input("ingrese su dni")
    cursos= int(input("ingrese cantidad de cursos"))
    dictPersonas['nombre']=nombre
    dictPersonas['dni']=dni
    dictPersonas['cursos']=[]
    for _ in range(cursos):
        nameCurso=input("ingrese su curso")
        dictPersonas['cursos'].append(nameCurso)
    listaPersonas.append(dictPersonas)

edad=int(input("ingrese su fechad de nacimiento"))
status=statusPersona(edad)
while status:
    if status:
        print("Bienvenido a DATUX")
    else:
        print("persona menor de edad")

    msg="""
    1. Ingresar datos de nuevo alumno
    2. Mostrar alumnos
    """
    print(msg)
    opcion=int(input("ingrese su opcion"))
    if opcion == 1:
        agregarPersona()
    elif opcion ==2:
        for i in listaPersonas:
            print(f"la persona con nombre {i['nombre']} esta matriculado en {len(i['cursos'])} cursos")
    else :
        print("ingrese opcion correcta")