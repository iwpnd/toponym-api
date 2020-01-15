from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from toponym_api.api.api_v1.api import router as api_router
from toponym_api.core.config import ALLOWED_HOSTS, API_V1_STR, PROJECT_NAME
from mangum import Mangum

app = FastAPI(title=PROJECT_NAME, docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=API_V1_STR)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url, title=app.title + " - Swagger UI"
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(openapi_url=app.openapi_url, title=app.title + " - ReDoc")


@app.get("/ping")
def pong():
    return {"ping": "pong!"}


handler = Mangum(app)
