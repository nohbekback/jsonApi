from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Definir modelos de Login y Profile
class Login(BaseModel):
    username: str
    password: str

class Profile(BaseModel):
    username: str
    name: str
    email: str
    alias: str
    phone: int
    address: str

# Establecer datos de autenticación y perfil
login_data = {"username": "brendac123", "password": "1234"}
profile_data = {"username": "brendac123", "name": "Brenda Cuevas", "logemail": "brendac@gmail.com", "alias": "brendac", "phone": "123-456-7890",
                "address": "123 Main Street, City, State, 12345"}

# Inicializar la aplicación FastAPI
app = FastAPI()

# Definir rutas
@app.post("/login")
def user_login(login: Login):
    if login.username == login_data["username"] and login.password == login_data["password"]:
        return {"message": "Inicio de sesión exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

@app.get("/profile")
def get_profile():
    return profile_data