from app.model import UserSchema, UserLoginSchema

from config import database
import uuid


class UserRepo():

	@staticmethod
	async def retrieve():
		_user = []
		collection = database.get_collection('user').find()
		async for user in collection:
			_user.append(user)
		return _user

	@staticmethod
	async def insert(user: UserSchema):
		id = str(uuid.uuid4())
		_user = {
			"_id": id,
			"name": user.fullname,
			"email": user.email,
			"password": user.password
		}
		await database.get_collection('user').insert_one(_user)

	@staticmethod
	async def update(id: str, user: UserSchema):
		_user = await database.get_collection('user').find_one({"_id": id})
		_user["name"] = user.fullname
		_user["email"] = user.email
		await database.get_collection('user').update_one({"_id":id}, {"$set": _user})

	@staticmethod
	async def retrieve_id(id: str):
		return await database.get_collection('user').find_one({"_id": id})


	@staticmethod
	async def delete(id: str):
		return await database.delete_collection('user').delete_one({"_id": id})