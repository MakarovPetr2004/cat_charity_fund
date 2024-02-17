from datetime import datetime
from typing import Optional

from pydantic import BaseModel, conint, Field, validator


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]
    full_amount: Optional[conint(gt=0)]


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=1, max_length=100)
    description: str
    full_amount: conint(gt=0)


class CharityProjectUpdate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectCreate):
    id: int
    create_date: datetime
    invested_amount: int = 0
    close_date: Optional[datetime]
    fully_invested: bool = False

    class Config:
        orm_mode = True

