from api.v1.api import api_router
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 
from schema.healthcheck import HealthCheck
from schema.parameters import UploadForm

app = FastAPI(
    title="KNN Mobile Training",
    openapi_url="/api/v1/openapi.json",
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/upload", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

# HealthCheck
# @app.get("", response_model=HealthCheck, tags=["Healthcheck"])
# @app.get("/", response_model=HealthCheck, tags=["Healthcheck"], include_in_schema=False)
# async def healthcheck(request: Request):
#     return {"message": "OK"}

app.include_router(api_router, prefix="/api/v1")