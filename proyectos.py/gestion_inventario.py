class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "pendiente"
    
    def marcar_completada(self):
        self.estado = "completada"
    
    def __str__(self):
        return f'Título: {self.titulo} | Estado: {self.estado} | Descripción: {self.descripcion}'

def mostrar_menu():
    print("1. Agregar tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea")
    print("4. Actualizar estado de tarea")
    print("5. Eliminar tarea")
    print("6. Filtrar tareas por estado")
    print("7. Actualizar descripción de tarea")
    print("8. Salir")

tareas = []

while True:
    mostrar_menu()
    try:
        opcion = input("Elige una opción: ")

        if opcion == "8":
            print("¡Gracias por usar el sistema de gestión de tareas!")
            break

        if opcion == "1":
            titulo = input("Ingrese el título de la tarea: ").strip()
            if not titulo:
                print("Error: El título no puede estar vacío")
                continue
            
            descripcion = input("Ingrese la descripción de la tarea: ").strip()
            if not descripcion:
                print("Error: La descripción no puede estar vacía")
                continue
            if any(t.titulo.lower() == titulo.lower() for t in tareas):
                print("Error: Ya existe una tarea con ese título")
                continue
                
            tarea = Tarea(titulo, descripcion)
            tareas.append(tarea)
            print("Tarea agregada exitosamente")

        elif opcion == "2":
            if not tareas:
                print("No hay tareas registradas")
            else:
                print("\nLista de tareas:")
                for i, tarea in enumerate(tareas, 1):
                    print(f'{i}. {tarea}')

        elif opcion == "3":
            titulo = input("Ingrese el título de la tarea a buscar: ").strip()
            encontrada = False
            for tarea in tareas:
                if tarea.titulo.lower() == titulo.lower():
                    print("\nTarea encontrada:")
                    print(tarea)
                    encontrada = True
                    break
            if not encontrada:
                print("Tarea no encontrada")

        elif opcion == "4":
            titulo = input("Ingrese el título de la tarea a completar: ").strip()
            encontrada = False
            for tarea in tareas:
                if tarea.titulo.lower() == titulo.lower():
                    if tarea.estado == "completada":
                        print("La tarea ya está completada")
                    else:
                        tarea.marcar_completada()
                        print("Estado de la tarea actualizado a 'completada'")
                    encontrada = True
                    break
            if not encontrada:
                print("Tarea no encontrada")

        elif opcion == "5":
            titulo = input("Ingrese el título de la tarea a eliminar: ").strip()
            encontrada = False
            for tarea in tareas:
                if tarea.titulo.lower() == titulo.lower():
                    tareas.remove(tarea)
                    print("Tarea eliminada exitosamente")
                    encontrada = True
                    break
            if not encontrada:
                print("Tarea no encontrada")

        elif opcion == "6":
            estado = input("Ingrese el estado a filtrar (pendiente/completada): ").strip().lower()
            if estado not in ["pendiente", "completada"]:
                print("Estado no válido. Use 'pendiente' o 'completada'")
                continue
            
            tareas_filtradas = [t for t in tareas if t.estado == estado]
            if not tareas_filtradas:
                print(f"No hay tareas en estado '{estado}'")
            else:
                print(f"\nTareas en estado '{estado}':")
                for i, tarea in enumerate(tareas_filtradas, 1):
                    print(f"{i}. {tarea}")

        elif opcion == "7":
            titulo = input("Ingrese el título de la tarea a actualizar: ").strip()
            encontrada = False
            for tarea in tareas:
                if tarea.titulo.lower() == titulo.lower():
                    nueva_descripcion = input("Ingrese la nueva descripción: ").strip()
                    if not nueva_descripcion:
                        print("Error: La descripción no puede estar vacía")
                        break
                    tarea.descripcion = nueva_descripcion
                    print("Descripción actualizada exitosamente")
                    encontrada = True
                    break
            if not encontrada:
                print("Tarea no encontrada")

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8")

    except Exception as e:
        print(f"Error inesperado: {str(e)}")