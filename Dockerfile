# Base build
FROM python:3.10-alpine AS base

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip \
    && apk add --no-cache --update --virtual .build-deps \
        gcc libffi-dev musl-dev \
    && apk add --no-cache --update postgresql-dev  \
    && pip install --no-cache-dir --upgrade -r /code/requirements.txt \
    && apk del .build-deps

# Development build
FROM base AS development

# Production build
FROM base AS production

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
