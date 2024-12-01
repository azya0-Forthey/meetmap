from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import placemark, user

app = FastAPI(
    title="MeetmapAPI",
    description="Meetmap API",
    version="0.0.1",
    responses={
        404: {"description": "Not found"},
    }
)

origins = [
    "http://79.137.204.11"
    "http://79.137.204.11:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(placemark.router)
app.include_router(user.router)
