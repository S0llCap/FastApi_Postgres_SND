import os, sys
import asyncio
from fastapi import FastAPI

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from endpoints import events
from db.db_setup import get_pool

app = FastAPI(
    title = "Тестовое задание",
    version = "1.0.1",
    openapi_tags = events.tags_metadata
)
app.include_router(events.router)

pool = get_pool()

@app.get("/")
async def root():
    return "YAY! We're still alive ~~~{,,_,,}=^-^="

#db connections refresher
async def checkConnections():
    while True:
        await asyncio.sleep(300)
        print("AUTOMAINTAIN: Check DB connections pool")
        pool.check()

@app.on_event("startup")
def startup():
    asyncio.create_task(checkConnections())
