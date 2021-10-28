# Build Docker image

```shell
docker build -t orca .
```

# Usage with Docker

```shell
docker run --rm -p 5000:5000 -v "$PWD:$PWD" -w "$PWD" orca --file input-0.json
```

# Requests

## Stats

```shell
curl http://127.0.0.1:5000/stats
```

```json
{
  "vm_count": 2,
  "request_count": 4,
  "average_request_time": 0.000411454
}
```

## Attack

```shell
curl http://127.0.0.1:5000/attack?vm_id=vm-a211de
```

```json
[
  "vm-c7bac01a07"
]
```

# Limitations

* No fancy output of an error (like missing vm_id in a query) and status
* Only a few tests (`parse` and `analyze`) because there is nothing to test:
    * input serialization is done by `pydantic`
    * only single input query for attack with `dict.get` operation
    * middleware simple as two code lines
    * args parsing is done by `typer`

# Features

* All data in memory
* Data for the `attack` API already prepared for usage, i.e. there is no raw
  json in of policies in memory, so there is no overhead for the finding the
  answer, answers already in memory as a dict (look at `analyzer.Routes`):

```python
{
    "vm-a211de": ["vm-c7bac01a07"],
    "vm-c7bac01a07": [],
}
```

# Overview

File is parsed on the startup only after that the server.

Data for APIs stored inside app in `app.state` attribute and live only in
memory.

Http API views are defined in `router` module.

Stats collected by `middleware.MeasureProcessTimeMiddleware`.

For cli `typer` is used and live in `cli` module.
