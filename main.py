from contextlib import asynccontextmanager
from fastapi import FastAPI, Path
import uvicorn

from core.models.db_helper import db_helper
from core.models.base import Base
from items_views import router_items
from users.views import router_users
from api_v1 import router as router_v1
from core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_items)
app.include_router(router_users)
app.include_router(router_v1, prefix=settings.api_v1_prefix)

@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
