from pydantic import BaseModel
from fastAPI import APIRouter

router = APIRouter(prefix="/animales", tags = ["Los Animales"])

class Animal(BaseModel):
    nombre: str
    edad: int
    familia: str
    vivo: bool

animales_db = [{"nombre": "tigre"}, {"nombre": "gato"}, {"nombre": "lince"}]

@router.get("/animales", tags = ["animales"])
async def leer_animales():
    datos_validados = []

    for item in animales_db:
            try:
                 datos_validados.append(Animal(**item))
            except ValueError:
                 pass

    datos_validados = [Animal(**item) for item in animales_db]

    return {
        "success": True, 
            "data": animales_db,
            "message": "Estos son los animales que tenemos"
    }

@router.post("/{animal}")
async def crear_animal(animal: Animal):
    animales_db.append(animal.model_dump())
    return {
        "success": True, 
            "data": animales_db,
            "message": "Animal añadido correctamente"
    }
    