import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer
import router

app = FastAPI()

# posts = [
# 	{
# 		"id": 1,
# 		"title": "parrot",
# 		"content": "bird"
# 	},
# 	{
# 		"id": 2,
# 		"title": "monkey",
# 		"content": "animal"
# 	},
# 	{
# 		"id": 3,
# 		"title": "pig",
# 		"content": "animal"
# 	},
# ]

# users = [

# ]

# test
@app.get("/", tags=["test"])
def greet():
	return {"hello": "world"}



app.include_router(router.router)

# Get posts
# @app.get("/posts", tags=["posts"])
# def get_posts():
# 	return {"data" : posts}

# # Get single post
# @app.get("/posts{id}", tags=["posts"])
# def get_post(id: int):
# 	if id > len(posts) or id <= 0:
# 		return {
# 			"error": "this id not in a list"
# 		}
# 	for post in posts:
# 		if post["id"] == id:

# 			return {
# 				"data" : post
# 			}

# # post
# @app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
# def add_post(post: PostSchema):
# 	post.id = len(posts) + 1
# 	posts.append(post.dict())
# 	return {
# 		"info": "post added"
# 	}

# @app.post("/user/signup", tags=["user"])
# def user_signup(user: UserSchema = Body(default=None)):
# 	users.append(user)
# 	return signJWT(user.email)

# def check_user(data: UserLoginSchema):
# 	for user in users:
# 		if user.email == data.email and user.password == data.password:
# 			return True
# 		return False

# @app.post("/user/login", tags=["user"])
# def user_login(user: UserLoginSchema = Body(default=None)):
# 	if check_user(user):
# 		return signJWT(user.email)
# 	else:
# 		return {
# 			"error": "Invalid login details"
# 		}










