from typing import cast

from asgiref.typing import ASGIApplication
from fastapi import FastAPI

from .analyzer import Routes
from .middleware import MeasureProcessTimeMiddleware, Statistics
from .router import router


def create_app(routes: Routes) -> ASGIApplication:
    app = FastAPI()

    app.include_router(router)

    stats: Statistics = {'count': -1, 'time': 0}
    app.add_middleware(MeasureProcessTimeMiddleware, stats=stats)

    app.state.stats = stats
    app.state.routes = routes

    return cast(ASGIApplication, app)
