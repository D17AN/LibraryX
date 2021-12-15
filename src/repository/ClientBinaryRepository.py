from src.repository.ClientRepository import ClientRepository
from src.domain.Client import Client
from src.domain.ClientValidator import ClientValidator
import pickle
from copy import deepcopy
import os

class ClientBinaryRepository(ClientRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__entity_validator = ClientValidator()


    def read_file(self):
        try:
            data = []
            file_name = self.__file_name
            if '_MEIPASS2' in os.environ:
                file_name = os.path.join(os.environ['_MEIPASS2'], file_name)

            with open(file_name, "rb") as f:
                data = pickle.load(f)

            for el in data: # we verify if each of object of the pickle file is valide
                self.__entity_validator.validate(el)

            for el in data:# we add each object in the repository if data was correct
                aux_el = deepcopy(el)
                self.add_client(aux_el)

            return True
        except IOError:
             pass
        except EOFError:
            return None


    def save_file(self):
        try:
            file_name = self.__file_name
            if '_MEIPASS2' in os.environ:
                file_name = os.path.join(os.environ['_MEIPASS2'], file_name)

            with open(file_name, "wb") as f:
                pickle.dump(self.clients_list, f)
        except IOError:
            raise IOError("File not found!")




