from fastapi import APIRouter
from repository import UserRepo


import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer
import router

router = APIRouter()


@router.get("/user/", dependencies=[Depends(jwtBearer())])
async def user():
	_userlist = await UserRepo.retrieve()
	return _userlist

@router.post("/user/create", dependencies=[Depends(jwtBearer())])
async def create(user: UserSchema = Body(default=None)):
	await UserRepo.insert(user)
	return signJWT(user.email)

@router.get("/user/{id}", dependencies=[Depends(jwtBearer())])
async def get_user(id: str):
	_user = await UserRepo.retrieve_id(id)
	return _user

@router.post("/user/update", dependencies=[Depends(jwtBearer())])
async def update(user: UserSchema):
	await UserRepo.update(user)
	return user

@router.delete("/user/{id}", dependencies=[Depends(jwtBearer())])
async def delete(id: str):
	await UserRepo.delete(id)
	return {
		"info": "user deleted"
	}

"""
@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
	users.append(user)
	return signJWT(user.email)

def check_user(data: UserLoginSchema):
	for user in users:
		if user.email == data.email and user.password == data.password:
			return True
		return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
	if check_user(user):
		return signJWT(user.email)
	else:
		return {
			"error": "Invalid login details"
		}
"""

