inventario = {
    'producto1': {
        'nombre': 'Camiseta',
        'precio': 20.99,
        'cantidad': 50,
        'categoria': 'Ropa',
        'codigo': 'CAM001-AR'
    },
    'producto2': {
        'nombre': 'Zapatos deportivos',
        'precio': 59.99,
        'cantidad': 30,
        'categoria': 'Calzado',
        'codigo': 'ZAP002-PE'
    },
    'producto3': {
        'nombre': 'Libreta',
        'precio': 5.99,
        'cantidad': 100,
        'categoria': 'Papeleria',
        'codigo': 'LIB003-CH'
    },
}

tasas ={
    'ar':0.05,
    'pe':0.04,
    'ch':0.02
}

##
def obtener_opcion(maxOpcion):
    opcion=input("Ingrese su opcion: ")
    if opcion.isnumeric():
        if int(opcion)<=maxOpcion:
            return int(opcion)    
        else:
            print(f"ingrese una opcion valida, tiene desde la opcion 1 hasta {maxOpcion}")
            return False
    else:
        print("Debe ingresar una numero")
        return False
    

def calc_impuesto(inventario):
    pass

def getFlete(ix):
    """     for kwarg in inventario:
            #print(kwarg, "=>", inventario[kwarg])
            pass """
    for i,value in ix.items():
        print(i, "=>",value,"type",type(value))
        codigo=value['codigo']
        pais=codigo.split('-')[1]
        flete=0.0
        for i,value2 in tasas.items():
            if i.lower() == pais.lower():
                flete = value2
        value['flete']=flete
    print(ix)
        

def validarStock(stockactual,cantidad):
    if stockactual>=cantidad:
        return True
    else:
        return False


def ActualizarStock(inventario):
    msg="Menu de movimientos de productos"
    dicItems={}
    print(msg)  
    for i,(clave,value) in enumerate(inventario.items(),1):
        print(i,value['nombre'],value['cantidad'])
        dicItems[i]=value['nombre']+'-'+clave
    move=input("ingrese el producto a mover: ")
    cantidad=input("ingrese la cantidad a mover: ")
    t1=(move,int(cantidad))
    claveBuscar=dicItems[int(move)].split("-")[1]
    cantidadActual=inventario[claveBuscar]['cantidad']
    print(cantidadActual,type(cantidadActual))
    print(t1[1])
    if not validarStock(cantidadActual,t1[1]):
            print("no puedes mover articulos ya que tiene un stock menor a lo solicitado")
            return False
    inventario[claveBuscar]['cantidad']=cantidadActual-t1[1]
    print(inventario)

while True:
    msg="""
     Bienvenido a DatuxLogs
     1.Calcular el impuesto
     2.Obtener Flete
     3.Actualizar stock
     4.Salir
    """
    print(msg)
    opcion=obtener_opcion(4)
    if not opcion:
        print("incorrecto")
        continue
    match opcion:
        case 1:
            calc_impuesto()
        case 2:
            getFlete(inventario)
            print(inventario)
        case 3:
            ActualizarStock(inventario)
        case 4:
            print("Hasta luego")
            break
            """     if opcion ==1:
            calc_impuesto()
        elif opcion ==2:
            pass
        elif opcion ==3:
            pass
        elif opcion ==4:
            pass
        else:
            print("ingrese una opcion valida") """