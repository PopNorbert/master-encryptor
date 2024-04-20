from CaesarEncryptor import CaesarEncryptor
x = "AbjasdbfhdjnjSFg"
enc = CaesarEncryptor(x, 5)
print(x)
x = enc.encrypt()
print(x)
x = enc.decrypt()
print(x)