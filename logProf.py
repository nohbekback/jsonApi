#importar el modulo
import json

# Diccionario Python
login = {
    "username": "brendac123",
    "password": "1234"
},
user = {
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
            "cuenta":"empresarial",
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


# Convertir el diccionario a formato JSON con la funcion dumps
login_JSON = json.dumps(login, indent=4)
profile_JSON = json.dumps(user, indent=4)

print(login_JSON)
print(profile_JSON) 

