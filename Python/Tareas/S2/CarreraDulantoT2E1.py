def saludar():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    correo = input("Ingrese su correo electrónico: ")
    print("¡Hola,", nombre + "!")

def operacionMatematica():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operador = input("Ingrese el operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: División por cero :c"
    else:
        resultado = "Operador inválido"
    print("El resultado es:", resultado)

def agregarAlumno(listaAlumnos):
    alumno = {}
    alumno['nombre'] = input("Ingrese el nombre del alumno: ")
    alumno['edad'] = int(input("Ingrese la edad del alumno: "))
    alumno['correo'] = input("Ingrese el correo electrónico del alumno: ")
    cursos = []
    while True:
        cursoNombre = input("Ingrese el nombre del curso ('fin' para terminar): ")
        if cursoNombre.lower() == 'fin':
            break
        notas = []
        while True:
            nota = float(input("Ingrese la nota del curso (ingrese -1 para terminar): "))
            if nota == -1:
                break
            notas.append(nota)
        cursos.append({'nombre_curso': cursoNombre, 'notas': notas})
    alumno['cursos'] = cursos
    listaAlumnos.append(alumno)

def calcularPromedioNotas(listaAlumnos):
    notasFinales = []
    for alumno in listaAlumnos:
        for curso in alumno['cursos']:
            promedioCurso = sum(curso['notas']) / len(curso['notas'])
            notasFinales.append(promedioCurso)
    return notasFinales

def mostrarAprobados(listaAlumnos, promedioAprobacion):
    print("Alumnos aprobados:")
    for alumno in listaAlumnos:
        promedioAlumno = sum(calcularPromedioNotas([alumno])) / len(alumno['cursos'])
        if promedioAlumno >= promedioAprobacion:
            print("- Nombre:", alumno['nombre'])
            print("  Promedio:", promedioAlumno)

def mostrarDesaprobados(listaAlumnos, promedioAprobacion):
    print("Alumnos desaprobados:")
    for alumno in listaAlumnos:
        promedioAlumno = sum(calcularPromedioNotas([alumno])) / len(alumno['cursos'])
        if promedioAlumno < promedioAprobacion:
            print("- Nombre:", alumno['nombre'])
            print("  Promedio:", promedioAlumno)

def generarListaMultiplos():
    numerosMultiplos = []
    for i in range(0, 10**10, 70):
        if i % 2 == 0 and i % 5 == 0 and i % 7 == 0:
            numerosMultiplos.append(i)
    print("Cantidad de números múltiplos de 2, 5 y 7:", len(numerosMultiplos))

def obtenerMayor():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return max(num1, num2)

listaAlumnos = []

while True:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Realizar una operación matemática")
    print("3. Agregar alumno")
    print("4. Calcular promedio de notas")
    print("5. Mostrar listado de alumnos aprobados")
    print("6. Mostrar listado de alumnos desaprobados")
    print("7. Generar lista de números múltiplos")
    print("8. Obtener el mayor de dos números")
    print("9. Salir")

    opcion = input("Ingrese el número de la opción que desea ejecutar: ")

    if opcion == '1':
        saludar()
    elif opcion == '2':
        operacionMatematica()
    elif opcion == '3':
        agregarAlumno(listaAlumnos)
    elif opcion == '4':
        promedio_notas = calcularPromedioNotas(listaAlumnos)
        print("Promedio de notas:", sum(promedio_notas) / len(promedio_notas))
    elif opcion == '5':
        mostrarAprobados(listaAlumnos, promedioAprobacion=10.5)  
    elif opcion == '6':
        mostrarDesaprobados(listaAlumnos, promedioAprobacion=10.5) 
    elif opcion == '7':
        generarListaMultiplos()
    elif opcion == '8':
        mayor = obtenerMayor()
        print("El mayor número es:", mayor)
    elif opcion == '9':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 9.")
