from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.models import User
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.schemas.donation import (
    DonationDB, DonationCreate, DonationSuperUserDB
)


router = APIRouter()


@router.post(
    '/',
    response_model=DonationDB,
    dependencies=[Depends(current_user)],
)
async def create_new_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Сделать пожертвование."""

    new_donation = await donation_crud.create(donation, session)
    return new_donation


@router.get(
    '/',
    response_model=list[DonationSuperUserDB],
    dependencies=[Depends(current_superuser)]
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Получает список всех пожертвований.
    """

    all_donations = await donation_crud.get_multi(session)

    return all_donations


@router.get(
    '/my',
    response_model=list[DonationDB],
    dependencies=[Depends(current_user)]
)
async def get_my_donations(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """Получить список моих пожертвований."""

    donations = await donation_crud.get_by_user(
        session=session, user=user
    )

    return donations
