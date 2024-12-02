FROM python:3.13-bullseye as fastapi

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install uv

COPY ./pyproject.toml /src/pyproject.toml
COPY ./uv.lock /src/uv.lock

RUN uv sync --frozen