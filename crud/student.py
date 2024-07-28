from database import db, parse_dict
from models.student import Student
from pymongo.errors import DuplicateKeyError

db.students.create_index("roll_no", unique=True)

async def create_student(student: Student):
    try:
        result = await db.students.insert_one(student.dict())
        return {"roll_no": student.roll_no}
    except DuplicateKeyError:
        return {"error": "Student with this roll_no already exists"}

async def get_student(roll_no: int):
    student = await db.students.find_one({"roll_no": roll_no})
    return parse_dict(student)

async def update_student(roll_no: int, student_data: dict):
    student_data = {k: v for k, v in student_data.items() if k != "_id"}
    result = await db.students.update_one({"roll_no": roll_no}, {"$set": student_data})
    if result.matched_count == 0:
        return {"error": "Student not found"}
    return {"success": "Student updated"}

async def get_all_students():
    students = await db.students.find().to_list(None)
    return [parse_dict(student) for student in students]

async def delete_student(roll_no: int):
    result = await db.students.delete_one({"roll_no": roll_no})
    if result.deleted_count == 0:
        return {"error": "Student not found"}
    return {"success": "Student deleted"}
