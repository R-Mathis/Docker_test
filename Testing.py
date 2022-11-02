from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get("/")
def main():
    return{"Hello' world"}
class Medoc(BaseModel):
    Medoc_id:int
    Medoc_name:str
    Medoc_price:int

@app.get("/{medicament}")
def medicaments(medicament:str):
    return{"le nom du medicament est": medicament}

@app.put("/{medicament}/enregistrement/")
def creation_fiche(medicament:str,medoc:Medoc):
    medoc.Medoc_name=medicament
    return{"Medoc_id":medoc.Medoc_id,"Medoc_name":medicament,"Medoc_price":medoc.Medoc_price}