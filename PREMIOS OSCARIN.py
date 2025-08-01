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

        