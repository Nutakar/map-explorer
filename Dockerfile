# syntax=docker/dockerfile:1

FROM python:3.8-alpine

ADD server1.py .

# WORKDIR /server1

COPY requirements.txt requirements.txt
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . .

CMD [ "python3", "server1.py"]