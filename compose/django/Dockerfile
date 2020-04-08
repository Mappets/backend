FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # pdftotext dependencies
  && apk add poppler-utils poppler-dev \
  # translations dependencies
  && apk add gettext \
  # matplotlib dependecies
  && apk add g++

RUN pip install cython numpy

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements/requirements.txt
RUN pip install -r /requirements/requirements.txt

WORKDIR /web
ADD . /web
RUN python manage.py makemigrations
RUN python manage.py migrate

# ENTRYPOINT ["/entrypoint"]
