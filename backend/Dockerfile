FROM python:3.10.13-alpine3.19

EXPOSE 8000/tcp

RUN apk update && apk upgrade --no-cache && rm -rf /var/cache/apk/* \
    && addgroup -g 101 -S master \
    && adduser -u 101 -S -h /home/master -G master master \
    && chown master:master -R /home/master

RUN --mount=type=bind,source=/requirements.txt,target=/tmp/requirements.txt \
    pip3 install --upgrade pip && pip3 install --upgrade setuptools \
    && pip3 install -r /tmp/requirements.txt --no-cache-dir

WORKDIR /tl_backend

COPY . .

RUN export DEBUG_STATE=True && python manage.py collectstatic --no-input

USER master

CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000" ]