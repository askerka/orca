from typing import Final, Optional

from fastapi import APIRouter, Depends, status
from starlette.requests import Request

from .analyzer import Routes
from .middleware import Statistics

router = APIRouter()


def get_routes(request: Request) -> Routes:
    return request.app.state.routes


def get_stats(request: Request) -> Statistics:
    return request.app.state.stats


@router.get('/attack', status_code=status.HTTP_200_OK)
def attack(
        vm_id: str,
        routes: Routes = Depends(get_routes),
):
    return routes.get(vm_id, [])


SECOND: Final[float] = 10e9


@router.get('/stats', status_code=status.HTTP_200_OK)
def stats(
        routes: Routes = Depends(get_routes),
        st: Statistics = Depends(get_stats)
):
    return {
        'vm_count': len(routes),
        'request_count': st['count'],
        'average_request_time': round(
            (st['time'] / SECOND) / st['count'],
            9
        ),
    }
