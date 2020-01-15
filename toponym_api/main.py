from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from toponym_api.api.api_v1.api import router as api_router
from toponym_api.core.config import ALLOWED_HOSTS, API_V1_STR, PROJECT_NAME
from mangum import Mangum

app = FastAPI(
    docs_url=f"{API_V1_STR}/docs",
    openapi_url=f"{API_V1_STR}/openapi.json",
    title=PROJECT_NAME,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=API_V1_STR)


@app.get("/ping")
def pong():
    return {"ping": "pong!"}


handler = Mangum(app, api_gateway_base_path="/Prod")
