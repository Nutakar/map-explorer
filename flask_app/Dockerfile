# syntax=docker/dockerfile:1

FROM python:3.8-alpine

WORKDIR /map-explorer

COPY requirements.txt .
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps 

COPY . .

CMD [ "gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "wsgi:server" ]