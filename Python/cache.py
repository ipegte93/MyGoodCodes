import os
import pickle
import gzip


class CacheManager:
    def __init__(self):
        self.path = os.path.join(os.getcwd(), "cache")
        self.__check_folder()

    def __check_folder(self):
        if os.path.exists(self.path) == False:
            os.makedirs(self.path)

    def create(self, data, name: str):
        path = os.path.join(self.path, name)
        with gzip.open(path, 'wb') as f:
            pickle.dump(data, f)

    def read(self, name: str):
        path = os.path.join(self.path, name)
        with gzip.open(path, 'rb') as f:
            return pickle.load(f)

    def get_list(self):
        return os.listdir(self.path)
