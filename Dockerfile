FROM python:3.9.7-alpine3.14 as build-env

WORKDIR /app

COPY . .

RUN apk update && apk add gcc musl-dev libffi-dev && \
    python -m pip install --upgrade pip && \
    python -m venv venv && source venv/bin/activate && \
    python -m pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev


FROM python:3.9.7-alpine3.14

WORKDIR /app

COPY --from=build-env /app/venv /app/venv
COPY --from=build-env /app/orca /app/orca
COPY --from=build-env /app/main.py /app/main.py

ENTRYPOINT ["/app/venv/bin/python", "/app/main.py"]
