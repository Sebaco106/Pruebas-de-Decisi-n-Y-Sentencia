import unittest
from gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea_nueva(self):
        resultado = self.gestor.agregar_tarea(1, "Tarea de prueba")
        self.assertEqual(resultado, "Tarea agregada")
        self.assertIn(1, self.gestor.tareas)
        self.assertFalse(self.gestor.tareas[1]['completada'])

    def test_agregar_tarea_existente(self):
        self.gestor.agregar_tarea(1, "Tarea de prueba")
        resultado = self.gestor.agregar_tarea(1, "Tarea duplicada")
        self.assertEqual(resultado, "Tarea ya existe")

    def test_marcar_tarea_completada_existente(self):
        self.gestor.agregar_tarea(1, "Tarea de prueba")
        resultado = self.gestor.marcar_completada(1)
        self.assertEqual(resultado, "Tarea completada")
        self.assertTrue(self.gestor.tareas[1]['completada'])

    def test_marcar_tarea_completada_no_existente(self):
        resultado = self.gestor.marcar_completada(2)
        self.assertEqual(resultado, "Tarea no encontrada")

    def test_obtener_resumen(self):
        self.gestor.agregar_tarea(1, "Tarea 1")
        self.gestor.agregar_tarea(2, "Tarea 2")
        self.gestor.marcar_completada(1)
        resumen = self.gestor.obtener_resumen()
        self.assertEqual(resumen, "Total: 2, Completadas: 1")

if __name__ == '__main__':
    unittest.main()
