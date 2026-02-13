from pydantic import BaseModel

import platform


print(f'{platform.system()}, {platform.release()}')


# class User(BaseModel):
#     id: int
#     username: str
#     email: str
#     is_active: bool = True
#
#
# user_data = {"id": 1,"username": "zara","email": "zara_1.gmail.com"}
#
# user= User(**user_data)
# print(user)
# print(user.is_active)

