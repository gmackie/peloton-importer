FROM python:3.9

WORKDIR /usr/src/app

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

ENV INFLUXDB_HOST=influx.gmac.io
ENV INFLUXDB_PORT=8086
ENV INFLUXDB_DATABASE=peloton

VOLUME [ "/data" ]

CMD ["python3", "importer"]