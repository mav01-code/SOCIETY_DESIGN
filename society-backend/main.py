from fastapi import FastAPI
from database.db import engine
from database.models import Base
from residents.routes import router as residents_router
from gatepass.routes import router as gatepass_router
from entry.routes import router as entry_router
from users.routes import router as users_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(residents_router, prefix="/residents")
app.include_router(gatepass_router, prefix="/gatepass")
app.include_router(entry_router, prefix="/entry")
app.include_router(users_router, prefix = "/users")