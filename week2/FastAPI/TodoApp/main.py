from fastapi import FastAPI,Depends,HTTPException,Path
import models
from models import Todos
from database import engine,SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel,Field

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    # prior to yield satement and yield statement too, will excute before sending the response 
    try:
        yield db
    # after yield sttement will exceute after getting the response 
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

class TodoRequest(BaseModel):
    title:str=Field(min_length=3)
    description:str=Field(min_length=3,max_length=100)
    priority:int=Field(gt=0,lt=6)
    complete:bool



@app.get('/',status_code=status.HTTP_200_OK)
# Depends here is dependency injection that helps to exceute something which we want to execute prior to some code
# like here get_db i.e. opening our db session needs to be done first even before reading it
async def read_all(db:db_dependency): 
    # return all data from our db
    return db.query(Todos).all()

@app.get('/todo/{todo_id}',status_code=status.HTTP_200_OK)
async def read_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    # first is added to reduce complexity since id is primary then it must have single same id only 
    todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail="Todo not found")


@app.post('/todo',status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,todo_request:TodoRequest):
    todo_model=Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()

@app.put('/todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency,todo_request:TodoRequest,todo_id:int=Path(gt=0),):
    todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found')
    
    todo_model.title=todo_request.title
    todo_model.description=todo_request.description
    todo_model.priority=todo_request.priority
    todo_model.complete=todo_request.complete

    db.add(todo_model)
    db.commit()

@app.delete('/todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found')
    db.query(Todos).filter(Todos.id==todo_id).delete()
    db.commit()