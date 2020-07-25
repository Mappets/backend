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

RUN pip install cython

COPY ./requirements/base.txt /base.txt
COPY ./requirements/dev.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD . /django

# RUN addgroup -S django \
    # && adduser -S -G django django

# Requirements are installed here to ensure they will be cached.

COPY ./compose/dev/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/dev/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./compose/dev/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/dev/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/dev/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower


# RUN chown -R django:django /django
# USER root

WORKDIR /django


ENTRYPOINT ["/entrypoint"]
