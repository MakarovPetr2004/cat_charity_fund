from datetime import datetime
from typing import Optional

from pydantic import BaseModel, conint, Field


class DonationSchema(BaseModel):
    comment: Optional[str]
    full_amount: Optional[conint(gt=0)]


class DonationCreate(DonationSchema):
    full_amount: conint(gt=0)


class DonationDB(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationSuperUserDB(DonationDB):
    user_id: int
    invested_amount: Optional[int] = 0
    close_date: Optional[datetime]
    fully_invested: Optional[bool] = False


