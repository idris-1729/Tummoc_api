from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import asyncio

from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("password")
mongo_details = f"mongodb+srv://mdidrissameer:{password}@idris.lixk7ae.mongodb.net/?retryWrites=true&w=majority&appName=idris"
client = AsyncIOMotorClient(mongo_details)
db = client.get_database("school")

async def check_connection():
    try:
        # Perform a simple operation to check if the connection is working
        await db.command("ping")
        print("MongoDB connection successful!")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

async def init():
    await check_connection()

def parse_dict(doc) -> dict:
    if doc is None:
        return {}
    return {str(key): str(value) if isinstance(value, ObjectId) else value for key, value in doc.items()}


if __name__ == "__main__":
    asyncio.run(init())
