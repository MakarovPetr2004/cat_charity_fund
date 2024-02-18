from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Кошачий благотворительный фонд'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'secret'
    first_superuser_email: Optional[EmailStr] = 'admin@admin.com'
    first_superuser_password: Optional[str] = 'admin'

    class Config:
        env_file = '.env'


settings = Settings()
