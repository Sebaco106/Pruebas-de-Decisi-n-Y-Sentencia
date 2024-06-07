class GestorTareas:
    def __init__(self):
        self.tareas = {}

    def agregar_tarea(self, tarea_id, descripcion):
        if tarea_id in self.tareas:
            return "Tarea ya existe"
        self.tareas[tarea_id] = {'descripcion': descripcion, 'completada': False}
        return "Tarea agregada"

    def marcar_completada(self, tarea_id):
        if tarea_id not in self.tareas:
            return "Tarea no encontrada"
        self.tareas[tarea_id]['completada'] = True
        return "Tarea completada"

    def obtener_resumen(self):
        total = len(self.tareas)
        completadas = sum(1 for tarea in self.tareas.values() if tarea['completada'])
        return f"Total: {total}, Completadas: {completadas}"
