from pydantic import BaseModel

class Student(BaseModel):
    roll_no: int
    name: str
    age: int
    teacher_id: int = None

class UpdateStudent(BaseModel):
    name: str = None
    age: int = None
    teacher_id: int = None
