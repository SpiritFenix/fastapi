from fastapi import FastAPI
from app.pages.router import router as router_pages


app = FastAPI()
app.include_router(router_pages)


@app.get("/")
async def root():
    return {"message": "Hello World"}


