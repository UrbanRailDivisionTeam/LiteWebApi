FROM ghcr.io/astral-sh/uv:python3.12-alpine

ADD . /LiteWebApi
WORKDIR /LiteWebApi
RUN uv sync --locked
CMD ["uv", "run", "server.py"]