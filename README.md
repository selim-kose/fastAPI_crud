# FastAPI MySQL CRUD Service

A production-ready FastAPI backend using SQLAlchemy, MySQL, Docker, Kubernetes, and pytest.

This project is part of the course Cloud Native Development - 2025 at YH Akademin and is the final assignment where we include what we have learnd during the course.

The project is an simple API for managin users. The API does only CRUD operationsn, nothing fancy.

## Tech stack

- **Backend:** FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Testing:** Pytest
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube / EKS)
- **CI/CD:** GitHub Actions

## Architecture Overview

![Architecture Diagram](https://github.com/user-attachments/assets/208364e7-67b2-4527-9905-539cbcf6adae)

## Instructions

### Enviroment variables example

Create a .env file in the root folder and change values to match your DB credentials and connection details.

```env
DB_USERNAME=username
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=users
```

### Run locally on docker with docker-compose

```commandline
git clone https://github.com/selim-kose/fastAPI_crud.git

docker-compose up -d --build
docker-compose down
```

### Run locally CLI

```commandline
git clone https://github.com/selim-kose/fastAPI_crud.git

python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

docker run -d --name mysql\
   -v mysql_data:/var/lib/mysql\
   -e MYSQL_ROOT_USERNAME=root\
   -e MYSQL_ROOT_PASSWORD=password\
   -e MYSQL_USER=user\
   -e MYSQL_PASSWORD=password\
   -e MYSQL_DATABASE=users\
   -p 3306:3306\
   -d mysql/mysql-server:latest\

touch .env

uvicorn app.main:app --reload
```

### Tests

Service-layer tests using pytest

Run unittest with coverage

```commandline
pytest --cov=app
```

### Endpoints

FastAPI provides automatic OpenAPI docs.

- Swagger UI: <http://localhost:8000/docs>
- ReDoc: <http://localhost:8000/redoc>

![Swagger Screenshot](https://github.com/user-attachments/assets/987df987-09e1-4f71-9323-92dbfe856207)

### User model

## CI/CD

GitHub Actions pipeline:

- Run tests
- Build Docker image
- Push to Docker Hub

### Kubernetes

## Run on AWS EKS

```mermaid
flowchart LR
    Client["Client<br/>(Browser / API Client)"]
    FastAPI["FastAPI Application<br/>(Uvicorn)"]
    MySQL["MySQL Database"]
    Volume["Persistent Volume"]

    Client -->|HTTP Requests| FastAPI
    FastAPI -->|SQLAlchemy| MySQL
    MySQL --> Volume
```
