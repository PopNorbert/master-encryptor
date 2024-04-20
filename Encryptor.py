from abc import ABC, abstractmethod
class Encryptor(ABC):
    def __init__(self, plaintext: str, key):
        self.plain = plaintext
        self.key = key
    
    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass
        