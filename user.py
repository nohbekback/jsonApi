#este codigo lee archivo en formato json
import json

with open("user.json") as users:
    datos= json.load(users)

    print(datos)