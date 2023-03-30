# **Run Dagster Dags in Docker**

A rudimentary template for a quick Dagster project setup in Docker. This is based on the image build process illustrated in the [Deploying Dagster to Docker](https://docs.dagster.io/deployment/guides/docker) section.

## **Setup**
```
git clone https://github.com/sarit-si/dagster-docker-template.git
cd dagster-docker-template
docker compose up -d
````

- (Optional) Create `home` folder. Else, docker compose will create it anyways.
- (Optional) To customise the Dagster instance, a [`dagster.yaml`](https://docs.dagster.io/deployment/dagster-instance) needs to be created. Place it in the `home` folder. This needs `docker compose down && docker compose up -d`. Without the `dagster.yaml`, dagster will write logs, events, storage, etc. to `/opt/dags/home` folder.
- The `home` and `dags` folders are volume mounted inside the container. (Note: `home` folder if not present, will automatically get created during docker compose)
- All assets, resources, etc. need to be placed inside the `dags` folder.
