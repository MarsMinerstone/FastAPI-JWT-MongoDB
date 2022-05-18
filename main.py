import uvicorn
from fastapi import FastAPI
from app.model import PostSchema

app = FastAPI()

posts = [
	{
		"id": 1,
		"title": "parrot",
		"content": "bird"
	},
	{
		"id": 2,
		"title": "monkey",
		"content": "animal"
	},
	{
		"id": 3,
		"title": "pig",
		"content": "animal"
	},
]

users = []

# test
@app.get("/", tags=["test"])
def greet():
	return {"hello": "world"}

# Get posts
@app.get("/posts", tags=["posts"])
def get_posts():
	return {"data" : posts}

# Get single post
@app.get("/posts{id}", tags=["posts"])
def get_post(id: int):
	if id > len(posts) or id <= 0:
		return {
			"error": "this id not in a list"
		}
	for post in posts:
		if post["id"] == id:

			return {
				"data" : post
			}

# post
@app.post("/posts", tags=["posts"])
def add_post(post: PostSchema):
	post.id = len(posts) + 1
	posts.append(post.dict())
	return {
		"info": "post added"
	}












