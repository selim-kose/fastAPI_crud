# FastAPI MySQL CRUD Service

A production-ready FastAPI backend using SQLAlchemy, MySQL, Docker, Kubernetes, and pytest.

This project is part of the course Cloud Native Development - 2025 at YH Akademin and is the final assignment where we include what we have learnd during the course.

The project is an API for managin users. The API is simple and does only CRUD operations.

## Tech stack

- **Backend:** FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Testing:** Pytest
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube / EKS)
- **CI/CD:** GitHub Actions

## Architecture Overview

![Architecture Diagram](docs/images/architecture.png)

## Instructions

Run locally on docker with docker-compose

```commandline
git clone https://github.com/selim-kose/fastAPI_crud.git

docker-compose up -d --build
docker-compose down

```

### Enviroment variables example

Create a .env file in the root folder and change values to match your DB credentials and connection details.

```env
DB_USERNAME=username
DB_PASSWORD=password
DB_HOST=host.docker.internal
DB_PORT=3306
DB_NAME=users
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

### Kubernetes

## Run on AWS EKS
