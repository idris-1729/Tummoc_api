from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import asyncio

from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("password")
mongo_url = f"mongodb+srv://mdidrissameer:{password}@idris.lixk7ae.mongodb.net/?retryWrites=true&w=majority&appName=idris"

# Initialize MongoDB client and database
client = AsyncIOMotorClient(mongo_url)
db = client["school"]

async def check_connection():
    """Ping the MongoDB server to ensure the connection is successful."""
    try:
        await db.command("ping")
        print("MongoDB connection successful!")
    except Exception as error:
        print(f"MongoDB connection failed: {error}")

async def init():
    """Initialize the database connection check."""
    await check_connection()

def parse_dict(document):
    """
    Convert MongoDB document to dictionary, converting ObjectId to string.

    Args:
        document (dict): MongoDB document.

    Returns:
        dict: Converted document with ObjectId as string.
    """
    if document is None:
        return {}
    return {key: str(value) if isinstance(value, ObjectId) else value for key, value in document.items()}

if __name__ == "__main__":
    # Run the init function to verify the MongoDB connection
    asyncio.run(init())
