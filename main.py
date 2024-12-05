from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import random

class TodoSchema(BaseModel):
    title: str

class StatusSchema(BaseModel):
    status: bool

todos = []

app = FastAPI()

@app.post("/post")
async def createTodo(todo: TodoSchema) -> str:
    final_todo = {
        "id": int(random.random()*10000000),
        "title": todo.title,
        "status": False
    }
    todos.append(final_todo)
    return "Created"

@app.get("/get")
async def getTodo():
    return todos

@app.put("/put/{id}")
async def editTodo(id: int, status: StatusSchema) -> str:
    for todo in todos:
        if todo.get('id') == id:
            todo['status'] = status.status
    return "Status Changed"

@app.delete("/delete/{id}")
async def deleteTodo(id: int) -> str:
    for todo in todos:
        if todo.get('id') == id:
            todos.remove(todo)
    return "Deleted"
    
