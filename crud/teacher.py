from mongo_connect import db, parse_dict
from models.teacher import Teacher
from pymongo.errors import DuplicateKeyError

# Set unique index on the "id" field in the "teachers" collection
db.teachers.create_index("id", unique=True)

# Helper function to handle duplicate key errors
def handle_duplicate_key_error():
    return {"error": "Teacher with this ID already exists"}

# Helper function to handle not found errors
def handle_not_found_error():
    return {"error": "Teacher not found"}

# Create a new teacher
async def create_teacher(teacher: Teacher):
    try:
        await db.teachers.insert_one(teacher.dict())
        return {"id": teacher.id}
    except DuplicateKeyError:
        return handle_duplicate_key_error()

# Find a teacher by ID
async def find_teacher(teacher_id: int):
    teacher = await db.teachers.find_one({"id": teacher_id})
    return parse_dict(teacher) if teacher else handle_not_found_error()

# Update an existing teacher's data
async def update_teacher(teacher_id: int, teacher_data: dict):
    # Remove _id to avoid modifying the primary key
    sanitized_data = {k: v for k, v in teacher_data.items() if k != "_id"}
    result = await db.teachers.update_one({"id": teacher_id}, {"$set": sanitized_data})
    if result.matched_count == 0:
        return handle_not_found_error()
    return {"success": "Teacher updated"}

# Get all teachers from the database
async def get_all_teachers():
    teachers = await db.teachers.find().to_list(None)
    return [parse_dict(teacher) for teacher in teachers]

# Delete a teacher by ID
async def delete_teacher(teacher_id: int):
    result = await db.teachers.delete_one({"id": teacher_id})
    if result.deleted_count == 0:
        return handle_not_found_error()
    return {"success": "Teacher deleted"}
