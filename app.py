from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI(title="Calculateur d'année de naissance", version="1.0.0")

# Configuration CORS pour permettre les requêtes depuis Shopify
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, spécifiez vos domaines Shopify
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgeRequest(BaseModel):
    age: int

class BirthYearResponse(BaseModel):
    birth_year: int

@app.get("/")
async def root():
    return {"message": "Calculateur d'année de naissance - Utilisez POST /birthyear avec votre âge"}

@app.post("/birthyear", response_model=BirthYearResponse)
async def calculate_birth_year(request: AgeRequest):
    """
    Calcule l'année de naissance à partir de l'âge fourni.
    
    Args:
        request: Objet contenant l'âge de la personne
        
    Returns:
        Objet contenant l'année de naissance calculée
    """
    # Validation de l'âge
    if request.age < 0:
        raise HTTPException(status_code=400, detail="L'âge ne peut pas être négatif")
    if request.age > 150:
        raise HTTPException(status_code=400, detail="L'âge semble invalide (plus de 150 ans)")
    
    # Calcul de l'année de naissance
    current_year = datetime.now().year
    birth_year = current_year - request.age
    
    return BirthYearResponse(birth_year=birth_year)

@app.get("/health")
async def health_check():
    """Endpoint de vérification de santé de l'API"""
    return {"status": "healthy", "service": "birth-year-calculator"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
