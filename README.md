# Backend_AI_Engineering_Assignment_2
# Student API - Flask + PostgreSQL + Docker

## Project Overview

This project is a Student Management REST API built using Flask.

The purpose of this assignment was to replace temporary in-memory storage with a real PostgreSQL database running inside Docker while maintaining the existing application architecture.

The project demonstrates:

- Flask REST API development
- Layered backend architecture
- Repository pattern
- PostgreSQL database integration
- SQLAlchemy ORM
- Docker containerization
- Docker Compose
- Persistent database storage using Docker volumes


# Technologies Used

- Python 3.12
- Flask
- SQLAlchemy
- PostgreSQL 16
- Docker
- Docker Compose
- Postman


# Project Architecture

The application follows a layered architecture:

```
Client (Postman)
        |
        ↓
Routes Layer
        |
        ↓
Service Layer
        |
        ↓
Repository Layer
        |
        ↓
PostgreSQL Database
```


## Routes Layer

The routes layer handles HTTP requests and responses.

Location:

```
routes/student_routes.py
```


## Service Layer

The service layer contains application logic and communicates with the repository layer.

Location:

```
services/students_service.py
```


## Repository Layer

The repository layer handles data storage operations.

Initially, the project used an in-memory repository for storing data temporarily.

The in-memory repository was replaced with a PostgreSQL repository.

The service layer and routes were kept unchanged during this switch, proving that the storage layer can be changed without modifying the application logic.

Location:

```
repositories/postgres_repository.py
```


# Project Structure

```
beai_ass2/

│
├── app/
│   └── main.py
│
├── routes/
│   └── student_routes.py
│
├── services/
│   └── students_service.py
│
├── repositories/
│   ├── student_repository.py
│   └── postgres_repository.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── init.sql
├── README.md
└── .env.example
```


# Database Setup

PostgreSQL runs inside a Docker container.

Database:

```
assignment_db
```

Table:

```
students
```

Student table structure:

| Column | Data Type |
|---|---|
| id | Integer |
| name | String |
| age | Integer |


# Environment Configuration

The database connection string is stored using environment variables.

The `.env` file contains private configuration values and is not committed to GitHub.

A sample configuration file is provided:

```
.env.example
```

Example:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=assignment_db
DATABASE_URL=postgresql://postgres:password@db:5432/assignment_db
```

The `.env` file is ignored using `.gitignore`.


# Docker Setup

The complete application stack is managed using Docker Compose.

The stack contains two services:

## Flask Application

Container name:

```
flask_app
```


## PostgreSQL Database

Container name:

```
postgres_db
```


PostgreSQL uses a Docker volume:

```
postgres_data
```

The volume stores database files permanently, allowing data to survive container restarts.


# Running the Project

## Step 1: Clone Repository

```
git clone <repository-url>
```

Move into the project directory:

```
cd beai_ass2
```


## Step 2: Create Environment File

Create:

```
.env
```

using the values from:

```
.env.example
```


## Step 3: Build and Start the Application

Run:

```bash
docker compose up --build
```

This command starts the complete stack:

- Flask API
- PostgreSQL database


The API will run on:

```
http://localhost:5000
```


PostgreSQL will run on:

```
localhost:5432
```


# API Endpoints


## Create Student

Method:

```
POST
```

Endpoint:

```
/students
```

Example request:

```json
{
    "name": "Ali",
    "age": 22
}
```


Example response:

```json
{
    "id": 1,
    "name": "Ali",
    "age": 22
}
```


---

## Get All Students

Method:

```
GET
```

Endpoint:

```
/students
```


Example response:

```json
[
    {
        "id": 1,
        "name": "Ali",
        "age": 22
    }
]
```


---

## Delete Student

Method:

```
DELETE
```

Endpoint:

```
/students/<id>
```


Example:

```
/students/1
```


# Data Persistence Verification

Persistence was tested to confirm that data is stored permanently in PostgreSQL and not temporarily in application memory.

The verification process:

### 1. Create Data

Student records were created using Postman.


### 2. Verify Data in PostgreSQL

Connected to the PostgreSQL container:

```bash
docker exec -it postgres_db psql -U postgres -d assignment_db
```

Checked records:

```sql
SELECT * FROM students;
```


### 3. Restart Application and Database

Stopped containers:

```bash
docker compose down
```

Started the stack again:

```bash
docker compose up
```


### 4. Verify Data After Restart

Connected to PostgreSQL again and executed:

```sql
SELECT * FROM students;
```

The previously created records were still available.

This confirmed:

- PostgreSQL volume persistence works
- Data survives container restart
- Storage is permanent instead of temporary memory storage


# Assignment Requirements Completed

✅ PostgreSQL running in Docker  
✅ PostgreSQL volume configured for persistent storage  
✅ Complete stack starts using `docker compose up`  
✅ Database connection stored using `.env`  
✅ `.env` ignored using `.gitignore`  
✅ `.env.example` committed for configuration reference  
✅ PostgreSQL repository implemented  
✅ In-memory repository replaced with PostgreSQL repository  
✅ Service layer unchanged after storage switch  
✅ Routes unchanged after storage switch  
✅ Persistence tested across application and container restart  


# Author

Muhammad Wasay
