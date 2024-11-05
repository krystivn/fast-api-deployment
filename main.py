import uvicorn
from fastapi import FastAPI
from config import db
from controller import router

async def lifespan(app: FastAPI):
    await db.create_all()

    yield

    await db.close()

def init_app():
    app = FastAPI(lifespan=lifespan)

    @app.get("/")
    def home():
        return "Welcome Home"

    app.include_router(router)

    return app

app = init_app()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=2137)