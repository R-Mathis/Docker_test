from fastapi import FastAPI
import uvicorn
import os
import google.auth
import sqlalchemy
from google.cloud.sql.connector import Connector ,IPTypes
from google.cloud import secretmanager
from dotenv import load_dotenv
import pg8000
print("Hello world")
##recuperation de toutes les variables de connexion##


load_dotenv(".env")
secret_id=os.getenv('secret_id')
db_user=os.getenv('db_user')
db_name=os.getenv('db_name')
region=os.getenv('region')
instance_name=os.getenv('instance_name')


credentials,PROJECT_ID=google.auth.default()
client = secretmanager.SecretManagerServiceClient(credentials=credentials)
name = f"projects/{PROJECT_ID}/secrets/{secret_id}/versions/latest"
db_password=client.access_secret_version(request={"name": name}).payload.data.decode('UTF-8')
print(db_password)
INSTANCE_CONNECT_NAME=f"{PROJECT_ID}:{region}:{instance_name}"
connector=Connector()
conn: pg8000.dbapi.Connection=connector.connect(INSTANCE_CONNECT_NAME,"pg8000",user=db_user,password=db_password,db=db_name,ip_type=IPTypes.PRIVATE)
cursor=conn.cursor()


## gestion de l'api##
app=FastAPI()
@app.get("/")
def main():
    return{"Hello' world"}



@app.get("/base")
def base():
    
    cursor.execute("CREATE TABLE IF NOT EXISTS Medoc (Nom_medoc VARCHAR(255) NOT NULL) ")
    conn.commit()

    return "table créée"

@app.get("/drop")
def drop():
    
    cursor.execute("DROP TABLE IF EXISTS Medoc")
    conn.commit()

    return "table effacée"
@app.get("/list")
def liste():
    cursor.execute("SELECT * FROM Medoc")
    results = cursor.fetchall()

    return  results
@app.get("/{medicament}")
def medicaments(medicament:str):
    #cursor.execute("INSERT INTO Nom_medoc values (?)", (medicament))
    cursor.execute("INSERT INTO Medoc (Nom_medoc) values ('"+medicament+"')")
    conn.commit()
    return{"le nom du medicament est": medicament}

if __name__=="__main__":
    app_port = int(os.getenv('APP_PORT', 8080))
    uvicorn.run(app, host="0.0.0.0", port=app_port)