from fastapi import HTTPException, Depends

from sqlalchemy import func
from sqlalchemy.testing.pickleable import User

from api.user.model import Users
from api.user.utils import check_phone
from utils.base.session import AsyncDatabase
from utils.base.BaseRepository import BaseRepository


class UserService(BaseRepository):
    model = Users

    async def get(self, by: str, value: str | int):
        match by:
            case 'email':
                query = func.lower(Users.email) == value.lower()
            case 'username':
                query = func.lower(Users.username) == value.lower()
            case 'phone':
                query = func.lower(Users.phone) == value.lower()
            case _:
                raise HTTPException(404, detail=f'{by} not valid')

        result = await self.filter(query)

        return result.first()

    async def get_user_by_phone(self, phone: str) -> User:
        phone_number = await check_phone(phone)
        return await self.get(by='phone', value=phone_number)

    async def get_user_by_email(self, email: str) -> User:
        return await self.get(by='email', value=email)

    async def get_user_by_username(self, username: str) -> User:
        return await self.get(by='username', value=username)


async def get_user_service(session=Depends(AsyncDatabase.get_session)):
    return UserService(session)


user_service: UserService = Depends(get_user_service)