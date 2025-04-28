DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml
DB_CONTAINER = example-db
ENV = --env-file .env
MANAGE_PY = python manage.py

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} ${ENV} down

.PHONY: runserver
runserver:
	${MANAGE_PY} runserver