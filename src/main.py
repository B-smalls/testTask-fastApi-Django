from fastapi import FastAPI

app = FastAPI(
    title="Async Web API service"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}