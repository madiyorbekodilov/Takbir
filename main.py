from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from dtos import UserCreate, UserUpdate, LinkCreate
from functions import create_user, update_user, create_link, delete_link, get_links
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

@app.post("/create/link")
async def link_create(link: LinkCreate, db: Session = Depends(get_db)):
    response = await create_link(link, db)
    return {"message": "link sucsesfully created",
            "statusCode": 200,
            "data": response
            }

@app.delete("/delete/link")
async def link_delete(link_id: int, db: Session = Depends(get_db)):
    response = await delete_link(link_id, db)
    return {"message": "link sucsesfully deleted",
            "statusCode": 200,
            "data": response
            }

@app.get("/get/link")
async def get_link(db: Session = Depends(get_db)):
    response = await get_links(db)
    return {"message": "fetched all links ",
            "statusCode": 200,
            "data": response
            }
