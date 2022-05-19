from typing import TypeVar, Optional
from pydantic import BaseModel, Field, EmailStr


T = TypeVar('T')

# class PostSchema(BaseModel):
# 	id : int = Field(default=None)
# 	title : str = Field(default=None)
# 	content : str = Field(default=None)
# 	class Config:
# 		schema_extra = {
# 			"post_demo": {
# 				"title": "some t about an",
# 				"content": "some c about an"
# 			}
# 		}

class UserSchema(BaseModel):
	fullname : str = Field(default=None)
	email : EmailStr = Field(default=None)
	password : str = Field(default=None)
	class Config:
		the_schema = {
			"user_demo":
			{
				"name": "Karl",
				"email": "help@mail.tu",
				"password":"123qwerty"
			}
		}

class UserLoginSchema(BaseModel):
	email : EmailStr = Field(default=None)
	password : str = Field(default=None)
	class Config:
		the_schema = {
			"user_demo": {
				"email": "help@mail.tu",
				"password":"123qwerty"
			}
		}