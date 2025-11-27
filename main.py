from fastapi import FastAPI
from api.v1.routes.auth_routes import router as auth_router
from api.v1.routes.project_routes import router as project_router
from database.connection import init_db

app = FastAPI(
    title="Advanced Task Management API",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(auth_router)
app.include_router(project_router)

@app.get("/",tags=["Root"])
async def root():
    return {"message":"Advanced Task Management server is running"}