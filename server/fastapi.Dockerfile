FROM python:3.12.1-bullseye as fastapi

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install uv
COPY ../pyproject.toml .
RUN uv pip sync