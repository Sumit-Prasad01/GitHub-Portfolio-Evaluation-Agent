from fastapi import FastAPI
from app.api.routes import router
import uvicorn

app = FastAPI(
    title="GitHub Portfolio Evaluation Agent",
    description="AI system to evaluate developer GitHub portfolios",
    version="1.0.0"
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("app.main:app", port = 5050, host = "127.0.0.1")