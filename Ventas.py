productos = {
                'No1': '2.', 'Producto1': 'Leche', 'Precio1': 35, 'Cantidad1': 20,
                'No2': '3.', 'Producto2': 'Computadoras', 'Precio2': 800, 'Cantidad2': 14,
                'No3': '4.', 'Producto3': 'Estufas', 'Precio3': 150, 'Cantidad3': 45,
                'No4': '5.', 'Producto4': 'Cereal', 'Precio4': 40, 'Cantidad4': 58
            }   
pr = {}
compras = {}
def producto2():
    e = int(input("Ingrese Cantidad a Comprar: "))
    if e > productos['Cantidad1']:
        print ("Cantidad Mayor a la existente")
        Menu()
    else:
        compras['Cantidad'] = e
        compras['Producto'] = "Leche"
        compras['Precio'] = 35
        productos['Cantidad1'] = productos['Cantidad1'] - e
        Menu()
def producto3():
    e = int(input("Ingrese Cantidad a Comprar: "))
    if e > productos['Cantidad2']:
        print ("Cantidad Mayor a la existente")
        Menu()
    else:
        compras['Cantidad2'] = e
        compras['Producto2'] = "Leche"
        compras['Precio2'] = 35
        productos['Cantidad2'] = productos['Cantidad2'] - e
        Menu()
def producto4():
    e = int(input("Ingrese Cantidad a Comprar: "))
    if e > productos['Cantidad3']:
        print ("Cantidad Mayor a la existente")
        Menu()
    else:
        compras['Cantidad3'] = e
        compras['Producto3'] = "Leche"
        compras['Precio3'] = 35
        productos['Cantidad3'] = productos['Cantidad3'] - e
        Menu()
def producto5():
    e = int(input("Ingrese Cantidad a Comprar: "))
    if e > productos['Cantidad4']:
        print ("Cantidad Mayor a la existente")
        Menu()
    else:
        compras['Cantidad4'] = e
        compras['Producto4'] = "Leche"
        compras['Precio4'] = 35
        productos['Cantidad4'] = productos['Cantidad4'] - e
        Menu()
def Producto():
    print ("Ingrese Pruducto")
    x = input ("Producto: ")
    y = int(input("Precio: "))
    z = int(input("Cantidad: "))
    pr['No'] = "6."
    pr['Producto'] = x
    pr['Precio'] = y
    pr['Cantidad'] = z
    Menu()
def Menu():
    print ("1.Ingresar Producto")
    print (productos['No1'],"Producto: ", productos['Producto1'], "Precio: ", productos['Precio1'], "Cantidad: ", productos['Cantidad1'])
    print (productos['No2'],"Producto: ", productos['Producto2'], "Precio: ", productos['Precio2'], "Cantidad: ", productos['Cantidad2'])
    print (productos['No3'],"Producto: ", productos['Producto3'], "Precio: ", productos['Precio3'], "Cantidad: ", productos['Cantidad3'])
    print (productos['No4'],"Producto: ", productos['Producto4'], "Precio: ", productos['Precio4'], "Cantidad: ", productos['Cantidad4'])
    print (pr)
    print ("6.Ver productos comprados")
    x = int(input("Ingrese numero de funcion o pruducto a Comprar: "))
    if x == 1:
        Producto()
    if x == 2:
        producto2()
    if x == 3:
        producto3()
    if x == 4:
        producto4()
    if x == 5:
        producto5()
    if x==6:
        print (compras)
        Menu()
def Usuario():
    z = input('Ingrese Usuario: ')
    i = input('Ingrese Contrasena: ')
    x = "Dilan"
    y = "SD"
    if z==x and i==y:
        Menu()
    else:
        print ("Usuario Incorrecto")
        Usuario()
Usuario()
