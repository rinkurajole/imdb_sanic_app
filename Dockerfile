FROM python:3.6.9-alpine
ENV PYTHONUNBUFFERED 1
ENV IN_DOCKER 1

COPY requirements.txt /requirements.txt

RUN apk add --no-cache --virtual .build-deps build-base \
    && pip3 install pip --upgrade \
    && pip3 install -r /requirements.txt \
    && apk del .build-deps

EXPOSE 8080

WORKDIR ../IMDB

ADD . /IMDB

CMD python -m imdb