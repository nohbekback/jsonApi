#Importar el módulo
import json

# Cadena de caracteres en el formato JSON
datos_JSON = """
{
    "login": {
        "username": "brendac123",
        "password": "1234"
        },
    "profile": {
        "name": "Brenda Cuevas",
        "email": "brendac@gmail.com",
        "phone": "123-456-7890",
        "address": "123 Main Street, City, State, 12345"
        }
    }
"""

# Convertir cadena de caracteres JSON a un diccionario con la funcion loads
datos_diccionario = json.loads(datos_JSON)
print (datos_diccionario)
