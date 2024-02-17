from sqlalchemy import Column, String

from app.models.base import CharityDonationBase


class CharityProject(CharityDonationBase):
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String, nullable=False)
