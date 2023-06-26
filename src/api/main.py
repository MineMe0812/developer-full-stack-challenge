from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.config import settings

from routes import users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CLIENT_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
