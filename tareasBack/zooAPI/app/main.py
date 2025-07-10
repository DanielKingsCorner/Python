from fastapi import FastAPI
from .routers import animales, inventario, empleados


app = FastAPI(
    title = "ZooAPI",
    version = "0.0.1",
)




@app.get("/", tags=["index"])
async def  index():
    return {"success": True, 
            "data":[
                "/animales",
                "/inventario",
                "/empleados"
            ],
            "message": "Aquí tienes tus Endpoint"
    }

app.include_router(animales.router)
app.include_router(inventario.router)
app.include_router(empleados.router)





