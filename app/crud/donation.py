from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):

    @staticmethod
    async def get_by_user(
            session: AsyncSession, user: User
    ):
        reservations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )

        return reservations.scalars().all()


donation_crud = CRUDDonation(Donation)
