from Encryptor import Encryptor

class CaesarEncryptor(Encryptor):
    def __init__(self, plain, key):
        super().__init__(plain, key)

    def encrypt(self):
        cypher = ""
        for char in self.plain:
            if char.isalpha():
                shifted = ord(char) + self.key
                if char.isupper() and chr(shifted)>'Z':
                    shifted-=26
                elif char.islower() and chr(shifted)>'z':
                    shifted-=26
                cypher += chr(shifted)
            else:
                cypher+=char
        return cypher

    def decrypt(self):
        return self.plain
