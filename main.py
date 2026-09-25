from fastapi import FastAPI
from routers import contact

app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

app.include_router(contact.router)