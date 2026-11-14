def agregar_cancion(cancion, lista):
    lista.append(cancion)
    print(f"La canción '{cancion}' ha sido agregada a la playlist.")
    with open("playlist.txt", "w") as archivo:
        for cancion in lista:
            archivo.write(cancion + "\n")

def eliminar_cancion(cancion, lista):
    if cancion in lista:
        lista.remove(cancion)
        print(f"La canción '{cancion}' ha sido eliminada de la playlist.")
        with open("playlist.txt", "w") as archivo:
            for cancion in lista:
                archivo.write(cancion + "\n")
    else:
        print(f"La canción '{cancion}' no se encuentra en la playlist.")

def mostrar_playlist(lista):
    if lista:
        print("Playlist:")
        with open("playlist.txt", "r") as archivo:
                contenido = archivo.read()
                print(contenido)
    else:
        print("La playlist está vacía.")


def buscar_cancion(cancion, lista):
    if cancion in lista:
        print(f"La canción '{cancion}' se encuentra en la playlist.")
    else:
        print(f"La canción '{cancion}' no se encuentra en la playlist.")

