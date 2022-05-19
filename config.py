import motor.motor_asyncio

MONGODB_URL = 'mongodb://localhost:27017/FastAPI_db'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# connection to db
database = client.FastAPI_db