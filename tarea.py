tareas = []

while True:
    print("\n--- Lista de Tareas ---")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Eliminar Tarea")
    print("4. Marcar como completada")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        tarea = input("Nueva Tarea: ")
        tareas.append([tarea, False])  # False = pendiente
        print("Agregada 📋")

    elif opcion == "2":
        for i, t in enumerate(tareas, 1):
            estado = "✅" if t[1] else "⏳"
            print(f"{i}. {t[0]} {estado}")

    elif opcion == "3":
        idx = int(input("# a eliminar: "))
        tareas.pop(idx - 1)
        print("Tarea eliminada 🗑️")

    elif opcion == "4":
        idx = int(input("# de tarea completada: "))
        tareas[idx - 1][1] = True
        print("Tarea marcada como completada ✅")

    elif opcion == "5":
        print("Saliendo del programa 👋")
        break