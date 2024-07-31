from mongo_connect import db
from crud.student import get_student, update_student
from crud.teacher import find_teacher

# Function to handle errors with a consistent response format
def create_error_response(message: str):
    return {"error": message}

# Function to assign a student to a teacher
async def student_to_teacher(student_roll_no: int, teacher_id: int):
    # Retrieve the student details by roll number
    student = await get_student(student_roll_no)
    if not student:
        return create_error_response("Student not found")

    # Retrieve the teacher details by teacher ID
    teacher = await find_teacher(teacher_id)
    if not teacher:
        return create_error_response("Teacher not found")

    # Assign the teacher to the student
    student["teacher_id"] = teacher_id
    update_response = await update_student(student_roll_no, student)

    # Check for errors during the update process
    if "error" in update_response:
        return create_error_response(update_response["error"])
    
    # Return success message upon successful assignment
    return {"success": "Student is assigned to teacher"}
