class ListaOperaciones:
    def __init__(self, lista=None):
        if lista is None:
            self.lista = []
        else:
            self.lista = lista

    def agregar_elemento(self, elemento):
        if elemento not in self.lista:
            self.lista.append(elemento)
        else:
            print("El elemento ya está en la lista")

    def eliminar_elemento(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
        else:
            print("El elemento no está en la lista")

    def obtener_lista(self):
        return self.lista
