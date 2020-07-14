FROM python:3.6

COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app

COPY ./app/requirements /app/requirements

RUN pip install --no-cache-dir -r requirements/dev.txt

COPY ./app /app



ENTRYPOINT ["/entrypoint.sh"]
