import unittest
from io import StringIO
import sys
from lista_operaciones import ListaOperaciones

class TestListaOperaciones(unittest.TestCase):

    def setUp(self):
        self.lista_op = ListaOperaciones()

    def test_agregar_elemento(self):
        # Probar agregar un elemento nuevo
        self.lista_op.agregar_elemento(5)
        self.assertIn(5, self.lista_op.obtener_lista())

        # Capturar salida para verificar el mensaje
        captured_output = StringIO()
        sys.stdout = captured_output

        # Probar agregar un elemento existente
        self.lista_op.agregar_elemento(5)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "El elemento ya está en la lista")

    def test_eliminar_elemento(self):
        # Probar eliminar un elemento existente
        self.lista_op.agregar_elemento(10)
        self.lista_op.eliminar_elemento(10)
        self.assertNotIn(10, self.lista_op.obtener_lista())

        # Capturar salida para verificar el mensaje
        captured_output = StringIO()
        sys.stdout = captured_output

        # Probar eliminar un elemento no existente
        self.lista_op.eliminar_elemento(10)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "El elemento no está en la lista")

    def test_obtener_lista(self):
        self.assertEqual(self.lista_op.obtener_lista(), [])
        self.lista_op.agregar_elemento(3)
        self.assertEqual(self.lista_op.obtener_lista(), [3])

if __name__ == '__main__':
    unittest.main()
