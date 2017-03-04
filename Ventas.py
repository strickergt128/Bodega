pr = []
compras = []
def producto2():
    e = input ("Ingrese Cantidad a Comprar: ")
    l = "Producto: Leche Precio: 35.00 Cantidad: "
    if e > 20:
        print "Cantidad Mayor a la existente"
        Menu()
    else:
        compras.append(l + e)
        Menu()
def Producto():
    print "Ingrese Pruducto"
    x = raw_input ("Producto: ")
    y = raw_input ("Precio: ")
    z = raw_input ("Cantidad: ")
    pr.append("Producto: " + x + " Precio: " + y + " Cantidad: " + z)
    Menu()
def Menu():
    a = 20
    b = 14
    c = 45
    d = 58
    print "1.Ingresar Producto"
    print "2.Producto: Leche Precio: 35.00 Cantidad: 20"
    print "3.Producto: Computadoras Precio: 8000.00 Cantidad: 14"
    print "4.Producto: Estufas Precio: 1500.00 Cantidad: 45"
    print "5.Producto: Cereal Precio: 40.00 Cantidad: 58"
    print pr
    print "6.Ver productos comprados"
    x = input ("Ingrese numero de funcion o pruducto a Comprar: ")
    if x == 1:
        Producto()
    if x == 2:
        producto2()
    if x==6:
        print compras
def Usuario():
    z = raw_input('Ingrese Usuario: ')
    i = raw_input('Ingrese Contrasena: ')
    x = "Dilan"
    y = "SD"
    if z==x and i==y:
        Menu()
    else:
        print "Usuario Incorrecto"
        Usuario()
Usuario()
