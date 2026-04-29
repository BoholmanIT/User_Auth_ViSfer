import os
import sys
from fastapi import FastAPI
from contextlib import asynccontextmanager
sys.path.insert(1, os.path.join(sys.path[0], '..'))



@asynccontextmanager
async def lifespan(app: FastAPI):
    


