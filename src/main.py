from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from users.router import router as user_routers
from auth.router import router as auth_routers
from tasks.router import router as task_routers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
    Load the routers into the FastAPI instance
"""
app.include_router(auth_routers)
app.include_router(user_routers)
app.include_router(task_routers)

