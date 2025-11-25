from fastapi import FastAPI

app = FastAPI(
    title="Advanced Task Management API"
)

@app.get("/")
async def root():
    return {"Hello":"World"}