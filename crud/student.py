from mongo_connect import db, parse_dict
from models.student import Student
from pymongo.errors import DuplicateKeyError

# Create a unique index on the "roll_no" field for the "students" collection
db.students.create_index("roll_no", unique=True)

# Helper function for handling duplicate key errors
def handle_duplicate_key_error():
    return {"error": "Student with this roll number already exists"}

# Helper function for handling not found errors
def handle_not_found_error():
    return {"error": "Student not found"}

# Function to create a new student
async def create_student(student: Student):
    try:
        await db.students.insert_one(student.dict())
        return {"roll_no": student.roll_no}
    except DuplicateKeyError:
        return handle_duplicate_key_error()

# Function to retrieve a student by roll number
async def get_student(roll_no: int):
    student = await db.students.find_one({"roll_no": roll_no})
    return parse_dict(student) if student else handle_not_found_error()

# Function to update an existing student's data
async def update_student(roll_no: int, student_data: dict):
    # Exclude "_id" from the update to prevent changing the primary key
    sanitized_data = {k: v for k, v in student_data.items() if k != "_id"}
    result = await db.students.update_one({"roll_no": roll_no}, {"$set": sanitized_data})
    if result.matched_count == 0:
        return handle_not_found_error()
    return {"success": "Student updated"}

# Function to retrieve all students
async def get_all_students():
    students = await db.students.find().to_list(None)
    return [parse_dict(student) for student in students]

# Function to delete a student by roll number
async def delete_student(roll_no: int):
    result = await db.students.delete_one({"roll_no": roll_no})
    if result.deleted_count == 0:
        return handle_not_found_error()
    return {"success": "Student deleted"}
