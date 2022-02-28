FROM python:3.9.9

RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd -g 799 nyu && useradd -r -u 999 -g nyu nyu

COPY . /app

WORKDIR /app

RUN pip install Flask

USER nyu

COPY --chown=nyu:nyu . .

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]