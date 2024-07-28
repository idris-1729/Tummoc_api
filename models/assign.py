from pydantic import BaseModel

class Assign(BaseModel):
    student_id: int
    teacher_id: int
