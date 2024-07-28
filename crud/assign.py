from database import db
from crud.student import get_student, update_student
from crud.teacher import get_teacher

async def assign_student_to_teacher(student_roll_no: int, teacher_id: int):
    student = await get_student(student_roll_no)
    if not student:
        return {"error": "Student not found"}
    
    teacher = await get_teacher(teacher_id)
    if not teacher:
        return {"error": "Teacher not found"}
    
    student["teacher_id"] = teacher_id
    response = await update_student(student_roll_no, student)
    if "error" in response:
        return {"error": response["error"]}
    return {"success": "Student assigned to teacher"}
