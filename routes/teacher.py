from fastapi import APIRouter, HTTPException
from models.teacher import Teacher, UpdateTeacher
from crud.teacher import create_teacher, get_teacher, get_all_teachers, update_teacher, delete_teacher

router = APIRouter()

@router.post("/", response_model=dict)
async def create_new_teacher(teacher: Teacher):
    response = await create_teacher(teacher)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response

@router.get("/{teacher_id}", response_model=dict)
async def read_teacher(teacher_id: int):
    teacher = await get_teacher(teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.put("/{teacher_id}", response_model=dict)
async def update_teacher_details(teacher_id: int, teacher: UpdateTeacher):
    response = await update_teacher(teacher_id, teacher.dict(exclude_unset=True))
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response

@router.get("/", response_model=list)
async def read_all_teachers():
    teachers = await get_all_teachers()
    return teachers

@router.delete("/{teacher_id}", response_model=dict)
async def delete_teacher_record(teacher_id: int):
    response = await delete_teacher(teacher_id)
    if "error" in response:
        raise HTTPException(status_code=404, detail=response["error"])
    return response
