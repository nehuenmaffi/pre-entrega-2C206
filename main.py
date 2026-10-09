productos = [
    {
        "nombre": "Pelota",
        "categoria": "Futbol",
        "precio": 1200
    },
    {
        "nombre": "Casco",
        "categoria": "Motociclismo",
        "precio": 1500
    },
    {
        "nombre": "Palos",
        "categoria": "Hockey",
        "precio": 950
    }
]

while True:
    print("="*40)
    print("Sistema de gestion de productos")
    print("="*40)
    print("""
    1. Agregar productos
    2. Mostrar productos
    3. Buscar producto
    4. Eliminar producto
    5. Salir
     """)

    opcion = input("Elegí una opción del 1 al 5: ").strip()
    
    if opcion == "1":
        print("--- Agregar producto ---")
        nombre = input("Ingrese el nombre del producto: ").strip()
        while nombre == "":
            print("El nombre del producto no puede estar vacío.")
            nombre = input("Ingrese el nombre del producto: ").strip()

        categoria = input("Ingrese la categoria a la que pertenece el producto: ").strip()
        while categoria == "":
            print("La categoría del producto no puede estar vacía.")
            categoria = input("Ingrese la categoria a la que pertenece el producto: ").strip()

        precio_str = input("Ingrese el precio del producto (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("El precio debe ser un número entero.")
            precio_str = input("Ingrese el precio del producto (sin centavos): ").strip()

        precio = int(precio_str)

        datos = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }

        productos.append(datos)
        print("Producto agregado con éxito.")
    
    elif opcion == "2":
        print("--- Productos ingresados ---")
        if len(productos) == 0:
            print("No hay productos ingresados.")
        else:
            for i in range(len(productos)):
                print(f"ID: {i+1}\n- Nombre: {productos[i]['nombre']}\n- Categoría: {productos[i]['categoria']}\n- Precio: ${productos[i]['precio']}")
                print("-" * 20)
                
    elif opcion == "3":
        print("--- Buscar producto ---")
        if len(productos) == 0:
            print("No hay productos ingresados.")
        else:
            busqueda = input("Ingresá el producto que querés buscar: ").strip().lower()

            while busqueda == "":
                print("Tenés que ingresar un nombre de producto para buscar.")
                busqueda = input("Ingresá el producto que querés buscar: ").strip().lower()

            encontrado = 0
            for i in range(len(productos)):
                if busqueda in productos[i]['nombre'].lower():
                    print(f"ID: {i+1}\n- Nombre: {productos[i]['nombre']}\n- Categoría: {productos[i]['categoria']}\n- Precio: ${productos[i]['precio']}")
                    print("-" * 20)
                    encontrado += 1

            if encontrado == 0:
                print("No se encontró ningún producto con ese nombre.")

    elif opcion == "4":
        print("--- Eliminar producto ---")
        if len(productos) == 0:
            print("No hay productos ingresados.")
        else:
            for i in range(len(productos)):
                print(f"ID: {i+1} - {productos[i]['nombre']} | Categoría: {productos[i]['categoria']} | Precio: ${productos[i]['precio']}")
            
            id_eliminar = input("Ingresá el ID del producto que querés eliminar: ").strip()

            while not id_eliminar.isdigit() or int(id_eliminar) < 1 or int(id_eliminar) > len(productos):
                print("ID inválido. Tenés que ingresar un número de ID válido.")
                id_eliminar = input("Ingresá el ID del producto que querés eliminar: ").strip()

            posicion = int(id_eliminar) - 1
            eliminado = productos.pop(posicion)
            print(f"El producto eliminado: {eliminado['nombre']}")
            
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida. Por favor, elegí una opción del 1 al 5.")

    