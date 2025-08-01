# Función para registrar una nueva película en una categoría
def registrar_pelicula():
    categoria = input("Ingrese la categoría: ").strip()
    titulo = input("Ingrese el título de la película: ").strip().title()

    # Si la categoría no existe, se crea una nueva entrada
    if categoria not in categorias:
        categorias[categoria] = {}

    # Verifica si la película ya fue registrada en esa categoría
    if titulo in categorias[categoria]:
        print("ERROR: La película ya fue registrada en esta categoría.")
    else:
        categorias[categoria][titulo] = 0  # Se inicia con 0 votos
        print(f"✅ Película '{titulo}' registrada en la categoría '{categoria}'.")

# Función para registrar un voto a una película
def registrar_voto():
    titulo = input("Ingrese el título de la película que desea votar: ").strip().title()
    coincidencias = []

    # Buscar en qué categorías está registrada la película
    for cat in categorias:
        if titulo in categorias[cat]:
            coincidencias.append(cat)

    # Si no se encontró la película en ninguna categoría
    if not coincidencias:
        print("ERROR: Película no encontrada en ninguna categoría.")
        return

    # Si solo hay una coincidencia, se registra el voto directamente
    if len(coincidencias) == 1:
        cat = coincidencias[0]
        categorias[cat][titulo] += 1
        print(f"✅ Voto registrado para '{titulo}' en la categoría '{cat}'.")
    else:
        # Si hay varias coincidencias, el usuario elige la categoría
        print("La película se encuentra en varias categorías:")
        for i, cat in enumerate(coincidencias, 1):
            print(f"{i}. {cat}")

        try:
            seleccion = int(input("Seleccione el número de la categoría para votar: "))
            if 1 <= seleccion <= len(coincidencias):
                cat_elegida = coincidencias[seleccion - 1]
                categorias[cat_elegida][titulo] += 1
                print(f"✅ Voto registrado para '{titulo}' en la categoría '{cat_elegida}'.")
            else:
                print("❌ Opción fuera de rango.")
        except ValueError:
            print("❌ Entrada inválida. Por favor ingrese un número.")

# Función para mostrar los resultados actuales (películas y sus votos)
def mostrar_resultados():
    print("\nRESULTADOS ACTUALES:")
    for cat, pelis in categorias.items():
        print(f"\nCategoría: {cat}")
        for titulo, votos in pelis.items():
            print(f" - {titulo}: {votos} voto(s)")

# Función para mostrar los ganadores de cada categoría
def mostrar_ganadores():
    print("\n🏆 Ganadores por categoría:")
    for cat, pelis in categorias.items():
        if pelis:
            ganadora = max(pelis, key=pelis.get)  # Película con más votos
            print(f" - {cat}: '{ganadora}'")

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n=== Sistema de Premios Oscarin ===")
    print("1. Registrar película")
    print("2. Registrar voto")
    print("3. Mostrar resultados")
    print("4. Mostrar ganadores por categoría")
    print("5. Salir")

# Bucle principal del programa
while True:
    try:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            registrar_pelicula()
        elif opcion == 2:
            registrar_voto()
        elif opcion == 3:
            mostrar_resultados()
        elif opcion == 4:
            mostrar_ganadores()
        elif opcion == 5:
            print("GRACIAS POR USAR EL PROGRAMA")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
    except ValueError:
        print("❌ ERROR DETECTADO: Entrada inválida.")


