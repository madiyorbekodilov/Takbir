from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from dtos import UserUpdate, LinkCreate, DarajaCreate, DarajaUpdate
from functions import create_user, update_user, create_link, delete_link, get_links, create_daraja, update_daraja, \
    delete_daraja, get_all_daraja, get_daraja, get_user_by_tg_id, get_user_by_id, create_friend, my_friend
from models import SessionLocal

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://alehson.uz/",
    "https://takbir-web-app.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/sinov")
async def root():
    return {"message": "Assalomu alekum Madiyorbek"}


@app.post("/create/user")
async def user_create(full_name: str, tg_id: int, db: Session = Depends(get_db)):
    response = await create_user(full_name, tg_id, db)
    return {"message": "user successfully created",
            "statusCode": 200,
            "data": response
            }


@app.put("/update/user")
async def user_update(user: UserUpdate, db: Session = Depends(get_db)):
    response = await update_user(user, db)
    return {"message": "user successfully updated",
            "statusCode": 200,
            "data": response
            }


@app.get("/get/user")
async def user_get(user_id: int, db: Session = Depends(get_db)):
    response = get_user_by_id(user_id, db)
    return {"message": "user successfully fetched",
            "statusCode": 200,
            "data": response
            }


@app.get("/get/tg_id/user")
async def get_tg_id(tg_id: int, db: Session = Depends(get_db)):
    response = await get_user_by_tg_id(tg_id, db)
    return {"message": "user successfully fetched by telegram id",
            "statusCode": 200,
            "data": response
            }


@app.post("/create/link")
async def link_create(link: LinkCreate, db: Session = Depends(get_db)):
    response = await create_link(link, db)
    return {"message": "link successfully created",
            "statusCode": 200,
            "data": response
            }


@app.delete("/delete/link")
async def link_delete(link_id: int, db: Session = Depends(get_db)):
    response = await delete_link(link_id, db)
    return {"message": "link successfully deleted",
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


@app.post("/create/daraja")
async def daraja_create(user: DarajaCreate, db: Session = Depends(get_db)):
    response = await create_daraja(user, db)
    return {"message": "Daraja successfully created",
            "statusCode": 200,
            "data": response
            }


@app.put("/update/daraja")
async def daraja_update(user: DarajaUpdate, db: Session = Depends(get_db)):
    response = await update_daraja(user, db)
    return {"message": "Daraja successfully updated",
            "statusCode": 200,
            "data": response
            }


@app.delete("/delete/daraja")
async def daraja_delete(daraja_id: int, db: Session = Depends(get_db)):
    response = await delete_daraja(daraja_id, db)
    return {"message": "Daraja successfully deleted",
            "statusCode": 200,
            "data": response
            }


@app.get("/get/all/daraja")
async def get_total_daraja(db: Session = Depends(get_db)):
    response = await get_all_daraja(db)
    return {"message": "Fetched all daraja",
            "statusCode": 200,
            "data": response
            }


@app.get("/get/daraja")
async def take_daraja(daraja_id: int, db: Session = Depends(get_db)):
    response = await get_daraja(daraja_id, db)
    return {"message": "Fetched daraja successfully",
            "statusCode": 200,
            "data": response
            }


@app.post("/create/friend")
async def friend_create(user_id: int, friend_tg_id: int, db: Session = Depends(get_db)):
    response = await create_friend(user_id, friend_tg_id, db)
    return {"message": "Successfully created friend",
            "statusCode": 200,
            "data": response
            }


@app.get("/get-all/friends")
async def all_friends(my_tg_id: int, db: Session = Depends(get_db)):
    response = await my_friend(my_tg_id, db)
    return {"message": "Fetched friends successfully",
            "statusCode": 200,
            "data": response
            }
