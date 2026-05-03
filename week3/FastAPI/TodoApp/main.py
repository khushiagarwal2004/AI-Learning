from fastapi import FastAPI
import week3.FastAPI.TodoApp.models as models
from week3.FastAPI.TodoApp.database import engine
from week3.FastAPI.TodoApp.routers import todos
from week3.FastAPI.TodoApp.routers import admin, auth

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

# for having todos as well as auth api in single main file
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
