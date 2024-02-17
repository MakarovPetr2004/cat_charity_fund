from typing import Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charityproject import charity_project_crud
from app.models import CharityProject, Donation, User


async def check_name_duplicate(
        room_name: str,
        session: AsyncSession,
) -> None:
    project_id = await charity_project_crud.get_room_id_by_name(
        room_name, session
    )

    if project_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Проект с таким именем уже существует!',
        )


async def check_project_exists(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        charity_project_id, session
    )

    if charity_project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найдена!'
        )
    return charity_project


async def check_project_edit(
        charity_project: CharityProject,
        full_amount: Optional[int] = None
) -> None:

    if not charity_project.fully_invested:
        raise HTTPException(
            status_code=422,
            detail='Закрытый проект нельзя редактировать!'
        )

    if not charity_project.invested_amount > full_amount:
        raise HTTPException(
            status_code=404,
            detail='Нельзя установить требуемую сумму меньше уже вложенной.'
        )


async def check_invested_amount_is_empty(
        charity_project: CharityProject,
) -> None:

    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=422,
            detail='Нельзя удалить проект, в который уже были инвестированы '
                   'средства!'
        )

