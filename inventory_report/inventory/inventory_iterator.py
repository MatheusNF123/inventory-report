from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, lista):
        self.lista = lista
        self.index = 0

    def __next__(self):
        try:
            result = self.lista[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return result
