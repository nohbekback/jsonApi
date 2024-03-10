#Importar el módulo
import json
from jsonschema import validate


# Definir un esquema JSON
schema = {
    "type": "object",
    "properties": {
        "cuenta": {"type": "string"},
        "organizacion": {"type": "string"}
    },
    "required": ["cuenta", "organizacion"]
}

# JSON a validar
data = {
    "cuenta": "empresarial",
    "organizacion": "nohbek"
}

# Validar el JSON contra el esquema
try:
    validate(instance=data, schema=schema)
    print("JSON válido")
except Exception as e:
    print("JSON inválido:", e)


# Cadena de caracteres en el formato JSON
datos_JSON = """
{
    "login": {
        "username": "brendac123",
        "password": "1234"
        },
    "user" :{
       "profile": {
           "general":{
                "name": "Brenda Cuevas",
                "email": "brendac@gmail.com",
                "alias": "brendac",
                "phone": "123-456-7890",
                "address": "123 Main Street, City, State, 12345"
            },
            "cuenta": "empresarial",
            "id": 1,
            "creditos":"0.3ETH"           
           },
        "configuracion":{
            "cuenta": "empresarial",
            "organizacion": "nohbek",
            "contacto": "Brenda Cuevas",
            "email": "brendac@gmail.com",
            "usuario": 1       
           },
        "facturacion": {
            "suscripcion": "advance",
            "soporte":"gratuito",
            "red": "ethnohbek",
            "registros": 1,
            "transacciones":1       
           }
        }
    }

"""

# Convertir cadena de caracteres JSON a un diccionario con la funcion loads
datos_diccionario = json.loads(datos_JSON)
print (datos_diccionario)
