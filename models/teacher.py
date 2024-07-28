from pydantic import BaseModel

class Teacher(BaseModel):
    id: int
    name: str
    subject: str

class UpdateTeacher(BaseModel):
    name: str = None
    subject: str = None
