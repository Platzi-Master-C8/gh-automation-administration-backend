import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_database
from app.routers import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(permissions_router)

@app.on_event("startup")
def startup():
    init_database()

@app.get("/")
def root():
    return {"Hola": "Mundo"}
    
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=80)
