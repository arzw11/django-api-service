## Django Project X

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Run with Docker Compose

1. Build and run the container using Docker Compose:
    
    Run the containers in the background:

    ```sh
    docker-compose -f docker_compose/app.yaml --env-file .env -f docker_compose/storages.yaml --env-file .env up --build -d
    ```    

2. Stop and remove containers:

    To stop and remove all running containers, execute:

    ```sh
    docker-compose -f docker_compose/app.yaml --env-file .env -f docker_compose/storages.yaml --env-file .env up --build -d
    ```    