from fastapi import FastAPI
from app.routes import chat
from app.services.scheduler import start_scheduler
from app.services.robinhood import login_to_robinhood


app = FastAPI()
app.include_router(chat.router)
@app.get("/")
def read_root():
    return {"message": "Hello from Orderly!"}

from app.services.scheduler import start_scheduler

@app.on_event("startup")
async def startup_event():
    login_to_robinhood()
    start_scheduler()