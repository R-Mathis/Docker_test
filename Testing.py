from fastapi import FastAPI

app=FastAPI()
@app.get("/")
def main():
    return{"Hello' world"}

@app.get("/{medicament}")
def medicaments(medicament:str):
    return{"le nom du medicament est": medicament}