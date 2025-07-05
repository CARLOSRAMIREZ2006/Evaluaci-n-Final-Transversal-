productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
 }

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}

def menu():
    while True:
        print("***MENÚ PRINCIPAL***")
        print("1. Stock marca.")
        print("2. Busqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")

        opcion = input("Ingrese Opción: ")

        if opcion == '1':
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        elif opcion == '2':
            while True:
                try:
                    precio_minimo = int(input("Ingrese precio mínimo: "))
                    precio_maximo = int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            buscar_precio(precio_minimo, precio_maximo)

        elif opcion == '3':
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese precio nuevo: "))
                except ValueError:
                    print("Debe ingresar un precio válido.")
                    continue
                if actualizar_precio(modelo, nuevo_precio): 
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
                continuar = input("Desea actualizar otro precio (s/n)?: ")
                if continuar != "si":
                    break

        elif opcion == '4':
            print("Programa Finalizado")
            break

        else:
            print("Debe selecionar una opcion valida!!")

def stock_marca(marca):
    total = 0 
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total += stock.get(modelo, [0, 0])[1]
    print(f"El stock es: {total}")

def buscar_precio(precio_minimo, precio_maximo):
    resultados = []
    for modelo, (precio, cantidad) in stock.items():
        if precio_minimo <= precio <= precio_maximo and cantidad > 0:
            if modelo in productos:
                marca = productos[modelo][0]
                resultados.append(f"{marca}---{modelo}")
    if resultados:
        resultados.sort()
        print("Los notebooks entre los precios consultas son: ", resultados)
    else:
        print("No hay notebook en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True 
    return False

menu()
