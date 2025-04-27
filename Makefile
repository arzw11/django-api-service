DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml
DB_CONTAINER = example-db
ENV = --env-file .env

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} ${ENV} down