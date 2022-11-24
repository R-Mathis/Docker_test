from fastapi import FastAPI
import uvicorn
import os

print("Hello world")


app=FastAPI()
@app.get("/")
def main():
    return{"Hello' world"}

@app.get("/{medicament}")
def medicaments(medicament:str):
    return{"le nom du medicament est": medicament}

if __name__=="__main__":
    app_port = int(os.getenv('APP_PORT', 9000))
    uvicorn.run(app, host="0.0.0.0", port=app_port)