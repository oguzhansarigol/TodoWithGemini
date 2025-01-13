from alembic.util import status
from fastapi import FastAPI, Depends, Path, HTTPException,Request
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette import status
from .models import Base,Todo
from .database import engine, SessionLocal
from .routers.auth import router as auth_routher
from .routers.todo import  router as todo_routher
import os


app= FastAPI()

script_dir=os.path.dirname(__file__)
st_abs_file_path=os.path.join(script_dir,"static/")


app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/")
def read_root(request: Request):
    return  RedirectResponse(url="/todo/todo-page",status_code=status.HTTP_302_FOUND)


app.include_router(auth_routher)
app.include_router(todo_routher)
Base.metadata.create_all(bind=engine)

