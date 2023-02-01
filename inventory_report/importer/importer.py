import abc


class Importer(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def import_data(path):
        pass
