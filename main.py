from fastapi import FastAPI
from database.db import engine
from database.models import Base
from residents.routes import router as residents_router
from gatepass.routes import router as gatepass_router
from entry.routes import router as entry_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(residents_router, prefix="/residents")
app.include_router(gatepass_router, prefix="/gatepass")
app.include_router(entry_router, prefix="/entry")
