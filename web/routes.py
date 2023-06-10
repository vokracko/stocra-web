from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI(openapi_url=None)


@app.get("/")
async def index() -> FileResponse:
    return FileResponse("web/static/index.html")


@app.get("/openapi.yaml")
async def openapi() -> FileResponse:
    return FileResponse("web/static/openapi.yaml")


@app.get("/favicon.png")
async def openapi() -> FileResponse:
    return FileResponse("web/static/favicon.png")


@app.get("/docs")
async def docs() -> HTMLResponse:
    return get_swagger_ui_html(
        title="Stocra.com",
        openapi_url="/openapi.yaml",
    )
