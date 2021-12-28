from fastapi import FastAPI

from app.database import create_admin_user
from app.database import create_db_and_tables
from app.database import drop_db_and_tables

app = FastAPI()

@app.on_event("startup")
def startup():
    drop_db_and_tables()
    create_db_and_tables()
    create_admin_user()

@app.get('/')
def root():
    return {'Hola': 'Mundo'}
    
if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=80)
