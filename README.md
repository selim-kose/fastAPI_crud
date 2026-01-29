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

## Project Structure

```text
fastapi_crud/
├── .github/
│   ├── workflows/
|      ├── docker.yml
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── user_service.py
│   └── user_router.py
├── tests/
│   ├── conftest.py
│   └── test_user_service.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

```md
- `routers`: HTTP layer
- `services`: Business logic
- `models`: SQLAlchemy ORM
- `schemas`: Pydantic validation
- `database`: MySQL Setup
```

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

- Service-layer tests using pytest
- SQLite in-memory database for isolation and speed
- Fixtures via conftest.py

Run unittest with coverage

```commandline
pytest --cov=app
```

### Endpoints

FastAPI provides automatic OpenAPI docs.

- Swagger UI: <http://localhost:8000/docs>
- ReDoc: <http://localhost:8000/redoc>

![Swagger Screenshot](https://github.com/user-attachments/assets/987df987-09e1-4f71-9323-92dbfe856207)

POST endpoint exampel:

![Postman Screenshot](https://github.com/user-attachments/assets/10f5c279-9fbc-489f-9fc9-591d5d16e18d)

## User model

- id = Integer, Primary_key
- name = String
- email = String, Unique
- age = Integer
- date_created = DateTime

## CI/CD

GitHub Actions pipeline:

- Run tests
- Build Docker image
- Push to Docker Hub

### Kubernetes

## Run on Minikube

```commandline
git clone https://github.com/selim-kose/fast_api_k8.git

minikube start

cd local_deployment

kubectl apply -f .
kubect delete -f .
```

## Run on AWS EKS

```commandline
git clone https://github.com/selim-kose/fast_api_k8.git

eksctl create cluster --name fastapi --nodes-min=3 --node-type=t3.medium
eksctl utils associate-iam-oidc-provider --region=eu-north-1 --cluster=fastapi --approve

eksctl create iamserviceaccount --name ebs-csi-controller-sa --namespace kube-system --cluster fastapi --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy --approve  --role-only  --role-name AmazonEKS_EBS_CSI_DriverRole

eksctl create addon --name aws-ebs-csi-driver --cluster fastapi --service-account-role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/AmazonEKS_EBS_CSI_DriverRole --force

aws eks update-kubeconfig --region eu-north-1 --name fastapi

cd aws_deployment

kubectl apply -f .
kubect delete -f .
```

- Log in to AWS console -> EC2 -> Load balancer
- Klick on the load balancer
- Find URL to cluster entrypoint under "DNS name"

<img src="https://github.com/user-attachments/assets/3ee0193f-0cb2-4dd1-8987-a034264aecc1" style="width: 80%;">

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
