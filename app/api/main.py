from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import settings


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    """
    Get the Databound - splashPage API homepage.
    """

    return settings.templates.TemplateResponse("pages/index.html", {"request": request})
