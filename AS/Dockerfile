FROM python:3.9.9

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

COPY . /app

WORKDIR /app

RUN pip install Flask

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
