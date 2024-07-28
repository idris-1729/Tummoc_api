from fastapi import APIRouter, HTTPException
from models.student import Student, UpdateStudent
from crud.student import create_student, get_all_students,get_student, update_student, delete_student

router = APIRouter()

@router.post("/", response_model=dict)
async def create_new_student(student: Student):
    response = await create_student(student)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response

@router.get("/{roll_no}", response_model=dict)
async def read_student(roll_no: int):
    student = await get_student(roll_no)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{roll_no}", response_model=dict)
async def update_student_details(roll_no: int, student: UpdateStudent):
    response = await update_student(roll_no, student.dict(exclude_unset=True))
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response

@router.get("/", response_model=list)
async def read_all_students():
    students = await get_all_students()
    return students

@router.delete("/{roll_no}", response_model=dict)
async def delete_student_record(roll_no: int):
    response = await delete_student(roll_no)
    if "error" in response:
        raise HTTPException(status_code=404, detail=response["error"])
    return response
