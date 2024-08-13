from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    full_name: str
    tg_id: int


class UserUpdate(BaseModel):
    id: int
    full_name: Optional[str]
    total_count: Optional[int]


class UserResult(BaseModel):
    full_name: str
    total_count: int
    share_link: str


class LinkCreate(BaseModel):
    name: str
    url: str


class LinkResult(BaseModel):
    name: str
    url: str


class DarajaCreate(BaseModel):
    name: str
    daraja: int
    started_at: int
    limit: int


class DarajaUpdate(BaseModel):
    id: int
    name: str
    started_at: int
    limit: int


class DarajaResult(BaseModel):
    name: str
    daraja: int
    started_at: int
    limit: int


class FriendCreate(BaseModel):
    user_id: int
    friend_tg_id: int
