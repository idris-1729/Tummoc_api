from fastapi import APIRouter, HTTPException
from models.assign import Assign
from crud.assign import assign_student_to_teacher

router = APIRouter()

@router.put("/", response_model=dict)
async def assign_student(assignment: Assign):
    response = await assign_student_to_teacher(assignment.student_id, assignment.teacher_id)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response
