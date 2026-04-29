import os
import sys
from fastapi import FastAPI
from contextlib import asynccontextmanager
import db.engine
import db.session
sys.path.insert(1, os.path.join(sys.path[0], '..'))



@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.engine = db.engine.create_async_engine()
    app.state.session_factory = db.session.Factory_AsyncSession(async_engine=app.state.engine)
    yield
    await app.state.engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message" : "Hello World"}