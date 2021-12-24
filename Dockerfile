# Base build
FROM python:3.10-alpine AS base

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip \
    && apk add --no-cache --update musl-dev gcc libffi-dev \
    && pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Development build
FROM base AS development

# Production build
FROM base AS production

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
