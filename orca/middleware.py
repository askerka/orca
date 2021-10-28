import time
from typing import TypedDict

from starlette.types import ASGIApp, Receive, Scope, Send


class Statistics(TypedDict):
    time: int
    count: int


class MeasureProcessTimeMiddleware:
    def __init__(self, app: ASGIApp, stats: Statistics) -> None:
        self.app = app
        self.stats = stats

    async def __call__(
            self,
            scope: Scope,
            receive: Receive,
            send: Send,
    ) -> None:
        t = time.time_ns()
        self.stats['count'] += 1

        await self.app(scope, receive, send)

        self.stats['time'] += time.time_ns() - t
