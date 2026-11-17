
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Tienda DevOps")

class Compra(BaseModel):
    precio: float
    descuento: float

@app.get("/")
def inicio():
    return {"mensaje": "Tienda DevOps 1.0"}

@app.post("/compra")
def calcular_compra(compra: Compra):
    if compra.precio < 0:
        raise HTTPException(
            status_code=400,
            detail="Precio invalido"
        )
    
    if not 0 <= compra.descuento <= 100:
        raise HTTPException(
            status_code=400,
            detail="Descuento invalido"
        )
    
    subtotal = compra.precio * (
        1 - compra.descuento / 100
    )

    total = round(subtotal * 1.16, 2)
    return {
        "subtotal": round(subtotal, 2),
        "total": total
    }

@app.get("/version")
def obtener_version():
    return {"aplicación": "Tienda DevOps",
            "version": "1.0.0"}