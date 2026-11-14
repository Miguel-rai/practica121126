import funcionesmusica
playlist = []
while True:
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
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
       cancion = input("Ingrese el nombre de la canción a agregar: ")
       funcionesmusica.agregar_cancion(cancion,playlist)

    elif opcion == "2":
        cancion = input("Ingrese el nombre de la canción a eliminar: ")
        funcionesmusica.eliminar_cancion(cancion, playlist)

    elif opcion == "3":
        funcionesmusica.mostrar_playlist(playlist)

    elif opcion == "4":
        cancion = input("Ingrese el nombre de la canción a buscar: ")
        funcionesmusica.buscar_cancion(cancion, playlist)

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")