FROM python:3.8.18-slim

ENV DAGSTER_HOME=/opt/dagster/home/

RUN mkdir -p /opt/dagster/home /opt/dagster/dags

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /opt/dagster/dags

EXPOSE 3000

ENTRYPOINT ["dagit", "-h", "0.0.0.0", "-p", "3000"]
