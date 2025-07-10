from fastAPI import APIRouter

router = APIRouter(prefix="/empleados", tags = ["Los Empleados"])

empleados_db = [{"trabajador": "Daniel"}, {"trabajador": "Sergio"}]

@router.get("/empleados", tags = ["empleados"])
async def leer_empleados():
         return {
        "success": True, 
            "data": empleados_db,
            "message": "Estos son los empleados contratados"
    }