from database import db, parse_dict
from models.teacher import Teacher
from pymongo.errors import DuplicateKeyError

db.teachers.create_index("id", unique=True)

async def create_teacher(teacher: Teacher):
    try:
        result = await db.teachers.insert_one(teacher.dict())
        return {"id": teacher.id}
    except DuplicateKeyError:
        return {"error": "Teacher with this id already exists"}

async def get_teacher(teacher_id: int):
    teacher = await db.teachers.find_one({"id": teacher_id})
    return parse_dict(teacher)

async def update_teacher(teacher_id: int, teacher_data: dict):
    teacher_data = {k: v for k, v in teacher_data.items() if k != "_id"}
    result = await db.teachers.update_one({"id": teacher_id}, {"$set": teacher_data})
    if result.matched_count == 0:
        return {"error": "Teacher not found"}
    return {"success": "Teacher updated"}

async def get_all_teachers():
    teachers = await db.teachers.find().to_list(None)
    return [parse_dict(teacher) for teacher in teachers]

async def delete_teacher(teacher_id: int):
    result = await db.teachers.delete_one({"id": teacher_id})
    if result.deleted_count == 0:
        return {"error": "Teacher not found"}
    return {"success": "Teacher deleted"}
