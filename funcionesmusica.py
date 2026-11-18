import json
import os

def mostrar_menu():
    print("="*30)
    print("1. agregar cancion")
    print("="*30)
    print("2. eliminar cancion")
    print("="*30)
    print("3. mostrar playlist")
    print("="*30)
    print("4. buscar cancion")
    print("="*30)
    print("5. salir")
    print("="*30)


def agregar_cancion(cancion, playlist):
    playlist.append(cancion)
    print(f"La canción '{cancion}' ha sido agregada a la playlist.")
    with open("playlist.txt", "w") as archivo:
        for cancion in playlist:
            archivo.write(cancion + "\n")

def eliminar_cancion(cancion, playlist):
    if cancion in playlist:
        playlist.remove(cancion)
        print(f"La canción '{cancion}' ha sido eliminada de la playlist.")
        with open("playlist.txt", "w") as archivo:
            for cancion in playlist:
                archivo.write(cancion + "\n")
    else:
        print(f"La canción '{cancion}' no se encuentra en la playlist.")

def mostrar_playlist(playlist):
    if playlist:
        print("Playlist:")
        with open("playlist.txt", "r") as archivo:
                contenido = archivo.read()
                print(contenido)
    else:
        print("La playlist está vacía.")


def buscar_cancion(cancion,playlist):
    if cancion in playlist:
        print(f"La canción '{cancion}' se encuentra en la playlist.")
    else:
        print(f"La canción '{cancion}' no se encuentra en la playlist.")

def guardar_playlist(playlist):
    ruta_archivo = "playlist.json"
    with open("playlist.json", "w") as archivo:
        json.dump(playlist, archivo) 
    return playlist

def cargar_playlist():
    ruta_archivo = "playlist.json"
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r") as archivo:
            playlist = json.load(archivo)
    else:
        playlist = []
    return playlist

def main():
    playlist = cargar_playlist()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cancion = input("Ingrese el nombre de la canción a agregar: ")
            agregar_cancion(cancion, playlist)
            guardar_playlist(playlist)

        elif opcion == "2":
            cancion = input("Ingrese el nombre de la canción a eliminar: ")
            eliminar_cancion(cancion, playlist)
            guardar_playlist(playlist)

        elif opcion == "3":
            mostrar_playlist(playlist)

        elif opcion == "4":
            cancion = input("Ingrese el nombre de la canción a buscar: ")
            buscar_cancion(cancion, playlist)

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


    
