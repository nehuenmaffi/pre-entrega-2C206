productos = [] # [[], [], []]

while True:
    print("="*40)
    print("Sistema de gestion de productos")
    print("="*40)
    print("""
    1. Agregar productos
    2. Mostrar productos
    3. Mostrar producto
    4. Eliminar producto
    5. Salir
     """)

    opcion = input("Elegí una opción del 1 al 5:").strip()
    
    if opcion == "1":
        print("--- Agregar producto ---")
        # validacion de los datos agregados
        nombre = input("Ingrese el nombre del producto: ").strip()
        while nombre == "":
            print("El nombre del producto no puede estar vacío.")
            nombre = input("Ingrese el nombre del producto: ").strip()
        categoria = input("Ingrese la categoria a la que pertenece el producto: ").strip()
        while categoria == "":
                    print("La categoría del producto no puede estar vacía.")
                    categoria = input("Ingrese la categoria ala que pertenece el producto: ").strip()
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
        # [[], [], []]
        if len(productos) == 0:
            print("No hay productos ingresados.")
        else:
            for i, producto in range(len(productos)): # 3 -> i = 0, I = 1, i = 2
                print(f"Producto {i+1}:")
                print(f"Nombre: {producto['nombre']}")
                print(f"Categoría: {producto['categoria']}")
                print(f"Precio: ${producto['precio']}")
                print("-"*20)

    elif opcion == "3":

    elif opcion == "4":
    
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida. Por favor, elegí una opción del 1 al 5.")

    