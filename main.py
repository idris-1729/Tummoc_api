import os
from fastapi import FastAPI
from routes import assign, student, teacher

app = FastAPI()

# Include routers for each route file
app.include_router(assign.router, prefix="/assignments", tags=["Assignments"])
app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(teacher.router, prefix="/teachers", tags=["Teachers"])


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=int(os.environ.get("PORT", 8000)),
        log_level="info"
    )