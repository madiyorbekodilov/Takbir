from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from models import *
from dtos import *

async def create_user(user: UserCreate, db):
    db_user = db.query(User).filter(User.tg_id == user.tg_id).first()
    if db_user is not None:
        raise HTTPException(status_code=402, detail="User already exists")

    user1 = User(
        tg_id=user.tg_id,
        full_name=user.full_name,
        total_count=0,
        share_link=""
    )
    db.add(user1)
    db.commit()
    db.refresh(user1)
    return UserResult(
        full_name=user1.full_name,
        total_count=user1.total_count,
        share_link=user1.share_link
    )


async def update_user(user: UserUpdate, db):
    db_user = db.query(User).filter(User.id == user.id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if user.full_name is not None:
        db_user.full_name = user.full_name
    if user.total_count is not None:
        db_user.total_count = user.total_count

    db.commit()
    db.refresh(db_user)
    return UserResult(
        full_name=db_user.full_name,
        total_count=db_user.total_count,
        share_link=db_user.share_link
    )


async def create_link(link: LinkCreate, db):
    link_one = Link(
        name=link.name,
        url=link.url
    )
    db.add(link_one)
    db.commit()
    db.refresh(link_one)
    return True

async def delete_link(link_id:int, db):
    link = db.query(Link).filter(Link.id == link_id).first()
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")

    db.delete(link)
    db.commit()
    db.refresh(link)
    return True

async def get_links(db):
    links = db.query(Link).all()
    links2 = list()
    for link in links:
        link_link = LinkResult(
            name=link.name,
            url=link.url
        )
        links2.append(link_link)

    return links2

async def create_daraja(daraja: DarajaCreate, db):
    db_daraja = db.query(Daraja).filter(Daraja.daraja == daraja.daraja).first()
    if db_daraja is not None:
        raise HTTPException(status_code=402, detail="Daraja already exists")
    new_daraja = Daraja(
        name=daraja.name,
        daraja=daraja.daraja,
        started_at=daraja.started_at,
        limit=daraja.limit
    )

    db.add(new_daraja)
    db.commit()
    db.refresh(new_daraja)
    return DarajaResult(
        name=new_daraja.name,
        daraja=new_daraja.daraja,
        started_at=new_daraja.started_at,
        limit=new_daraja.limit
    )

async def update_daraja(daraja: DarajaUpdate, db):
    db_daraja = db.query(Daraja).filter(Daraja.id == daraja.id).first()
    if db_daraja is None:
        raise HTTPException(status_code=404, detail="Daraja not found")

    if daraja.name is not None:
        db_daraja.name = daraja.name
    if daraja.started_at is not None:
        db_daraja.started_at = daraja.started_at
    if daraja.limit is not None:
        db_daraja.limit = daraja.limit

    db.commit()
    db.refresh(db_daraja)
    return DarajaResult(
        name=daraja.name,
        daraja=db_daraja.daraja,
        started_at=daraja.started_at,
        limit=daraja.limit
    )

async def delete_daraja(daraja_id:int, db):
    db_daraja = db.query(Daraja).filter(Daraja.id == daraja_id).first()
    if db_daraja is None:
        raise HTTPException(status_code=404, detail="Daraja not found")

    db.delete(db_daraja)
    db.commit()
    db.refresh(db_daraja)
    return True

async def get_all_daraja(db):
    db_daraja = db.query(Daraja).all()
    daraja_all = list()
    for daraja in db_daraja:
        da_raja = DarajaResult(
            name=daraja.name,
            daraja=daraja.daraja,
            started_at=daraja.started_at,
            limit=daraja.limit
        )
        daraja_all.append(da_raja)

    return daraja_all
async def get_daraja(daraja_id: int,db):
    db_daraja = db.query(Daraja).filter(Daraja.id == daraja_id).first()
    if db_daraja is None:
        raise HTTPException(status_code=404, detail="Daraja not found")
    return DarajaResult(
        name=db_daraja.name,
        daraja=db_daraja.daraja,
        started_at=db_daraja.started_at,
        limit=db_daraja.limit
    )

