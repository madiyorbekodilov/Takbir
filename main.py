from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from dtos import UserCreate, UserUpdate
from functions import create_user, update_user
from models import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/create/user")
async def user_create(user: UserCreate, db: Session = Depends(get_db)):
    response = await create_user(user, db)
    return {"message": "user sucsesfully created",
            "statusCode": 200,
            "data": response
            }

@app.put("/update/user")
async def user_update(user: UserUpdate, db: Session = Depends(get_db)):
    response = await update_user(user, db)
    return {"message": "user sucsesfully updated",
            "statusCode": 200,
            "data": response
            }

