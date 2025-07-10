from fastAPI import APIRouter

router = APIRouter(prefix="/inventario", tags = ["El inventario"])

inventario_db = [{"comida": "carne fresca"}, {"comida": "pollo"}, {"comida": "higado"}]

@router.get("/inventario", tags = ["inventario"])
async def leer_inventario():
        return {
        "success": True, 
            "data": inventario_db,
            "message": "Este es el inventario actual"
    }