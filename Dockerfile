FROM python:3.6

MAINTAINER PG Drange <pgdr@equinor.com>

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

EXPOSE 8000

CMD ["app.py"]
