#importar el modulo
import json


# Diccionario Python
login = {
    "username": "brendac123",
    "password": "1234"
},
profile = {
    "name": "Brenda Cuevas",
    "email": "brendac@gmail.com",
    "phone": "123-456-7890",
    "address": "123 Main Street, City, State, 12345"
}

# Convertir el diccionario a formato JSON con la funcion dumps
login_JSON = json.dumps(login, indent=4)
profile_JSON = json.dumps(profile, indent=4)

print(login_JSON)
print(profile_JSON) 

