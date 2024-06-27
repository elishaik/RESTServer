import uvicorn
from fastapi import FastAPI
from routers import example as example_router

app = FastAPI()

app.include_router(example_router.router)

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()