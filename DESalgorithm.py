import os
import io
import base64
import Image
import pyDes
from array import array
#Algorithm of DES cipher, with 8 bits key, for images, presented by Nicolas RIcardo Enciso

def convertToByteArray(originalImage):
    with open(originalImage, "rb") as f:
        return bytearray(f.read())

def menu():
    print(">>>>>>   BIENVENIDO    <<<<<<")
    print("> Ingrese el nombre de la imagen a cifrar (debe estar en el mismo lugar del presente software")
    image = raw_input()
    print("> Ingrese el formato de la imagen (jpg, png, gif) ")
    imageFormat = raw_input()
    print("> Ingrese el nombre para la imagen descifrada de salida")
    desimage = raw_input()
    originalImage = str(image)+str('.')+str(imageFormat)
    byteImage = convertToByteArray(originalImage)
    print("> Ingrese la llave, debe ser de 8 caracteres")
    key = raw_input()
    if len(key) < 8:
        print("> SU clave debe ser de 8 caracteres")
        print("> Ingrese la llave, debe ser de 8 caracteres")
        key = raw_input()
    des = pyDes.des(str(key),padmode=pyDes.PAD_PKCS5)
    cipherImage = des.encrypt(str(byteImage))
    cipherImage = base64.b64encode(cipherImage)
    print("> Texto en base 64 cifrado: ")
    print(cipherImage)
    print("> Inicio de descifrado...")
    descipherImage = base64.b64decode(cipherImage)
    descipherImage = des.decrypt(str(descipherImage))
    image = Image.open(io.BytesIO(descipherImage))
    image.save(str(desimage)+'.'+str(imageFormat))
    print("> Su imagen ha sido descifrada")

menu()
    
        
    



