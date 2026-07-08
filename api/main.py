from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="DocLens AI",
    description="RAG-based Technical Documentation Assistant",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "DocLens AI API is running."
    }