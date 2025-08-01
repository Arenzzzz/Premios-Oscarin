# Hecho por:
    # - Moshé Arenz Peláez Virula - 1556425
    # - Carlos Andrés Cholotío Mendoza - 1517925

# Diccionario principal de registros con categoría predefinas para el uso del programa
categorias = {
    'Mejor Guión':{'Superman':2, 'Batman':2, 'Spiderman':2},
    'Mejor Animación':{'Totoro':0, 'Los Pitufos':0},
    'Mejor Comedia':{'Los Chiflados':1, 'Scary Movie':4}
}

# Función para registrar una nueva película en una categoría
def registrar_pelicula():
    print("\nREGISTRO DE CATEGORÍA Y PELÍCULA")
    categoria = input("Ingrese la categoría: ").strip().title()
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
    # Valida que hayan categorías y películas registradas
    if len(categorias) != 0:
        print("\nREGISTRO DE VOTO")
        for i, catg in enumerate(categorias, 1):
            print(f'{i}.-{catg}')
        
        while True:
            try:
                cat = int(input("Categoría: "))
                    
            except ValueError:
                print("ERROR: Ingresa la opción en números")
                
            else:
                if 0 < cat <= len(categorias):
                    break
                print("OPCIÓN INVÁLIDA")
            
        for i, catg in enumerate(categorias, 1):
            if cat == i:
                cat = catg
        
        print(f'\nCategoría: {cat}')
        for i, peli in enumerate(categorias[cat], 1):
            print(f'{i}.-{peli}')
            
        while True:
            try:
                pelicula = int(input("Película: "))
                    
            except ValueError:
                print("ERROR: Ingresa la opción en números")
                
            else:
                if 0 < pelicula <= len(categorias[cat]):
                    break
                print("OPCIÓN INVÁLIDA")
        
        for i, peli in enumerate(categorias[cat], 1):
            if pelicula == i:
                pelicula = peli
                categorias[cat][pelicula] += 1
        
        
        print(f"✅ Voto registrado para '{pelicula}' en la categoría '{cat}'.")
    
    else:
        print("\nNo hay películas registradas, añádalas.")
        
# Función para mostrar los resultados actuales (películas y sus votos)
def mostrar_resultados():
    # Valida que hayan categorías y películas registradas
    if len(categorias) != 0:
        print("\nRESULTADOS ACTUALES:")
        for cat, pelis in categorias.items():
            print(f"\nCategoría: {cat}")
            for titulo, votos in pelis.items():
                print(f" - {titulo}: {votos} voto(s)")
    
    else:
        print("\nNo hay películas registradas, añádalas.")

# Función para mostrar los ganadores de cada categoría
def mostrar_ganadores():
    # Valida que hayan categorías y películas registradas
    if len(categorias) != 0:
        
        print("\n🏆 Ganadores por categoría:")

        # Iteración al diccionario principal de registros
        for cat, pelis in categorias.items():
            mayores = []    # Lista para guardar las películas y verificar si tiene votos iguales (empates) o no
            validacion_voto = False # Varibale para verificar si las películas cuentan con votos o no
            
            # Iteración al diccionario de películas por cada categoría
            for pel, voto in pelis.items():

                # Encuentra el valor máximo de votos de cada película
                mayor = max(pelis, key=pelis.get)
                valor_mayor = pelis.get(mayor)
                
                # Verifica que cada película tenga votos
                if voto != 0:
                    validacion_voto = True
                
                # Analiza la cantidad de votos y las aguarda en la lista para luego verificar el conteo
                if voto == valor_mayor:
                    mayores.append({pel:voto})
            
            # Realiza las tareas a las películas que cuentan con votos
            if validacion_voto == True:

                # Validación para las películas que tienen más votos
                if len(mayores) == 1:
                    print(f" - {cat}: '{mayor}'") # Película con más votos
                
                # Validación a las películas que tengan el mismo número de votos e imprime sus estados
                elif len(mayores) > 1:
                    print(f' - {cat}: Empate')
                    for i in mayores:
                        for x, y in i.items():
                            print(f'\t{x}: {y}')
            
            # Imprime las categorías que no tienen votos (0)
            else:
                print(f" - {cat}: No tiene votos")
            
    
    else:
        print("\nNo hay películas registradas, añádalas.")

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
            print("\nGRACIAS POR USAR EL PROGRAMA")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")
    except ValueError:
        print("❌ ERROR DETECTADO: Entrada inválida.")
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
            print("\nGRACIAS POR USAR EL PROGRAMA")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")
    except ValueError:
        print("❌ ERROR DETECTADO: Entrada inválida.")