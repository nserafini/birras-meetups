from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from meetups.core.config import settings


def create_app():
    app = FastAPI(title=settings.API_NAME, version=settings.API_VERSION,)
    return app


app = create_app()


@app.get("/", response_class=HTMLResponse)
def alive():
    return "<h1>Alive<h1>"
