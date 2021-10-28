import typer
import uvicorn

from .analyzer import analyze
from .app import create_app
from .parser import parse


def run(
        file: typer.FileText = typer.Option(...),
        port: int = 5000,
) -> None:
    doc = parse(file)
    routes = analyze(doc)

    app = create_app(routes)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info",
    )
