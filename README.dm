# Project Setup and Run Instructions

This document provides step-by-step instructions to set up and run the project on Windows, Linux, and using Docker.

## Prerequisites

- **Python 3.12.7**: Ensure Python is installed on your system.
- **pip**: The Python package manager.
- **Virtual Environment Tools**: Such as `venv` or `virtualenv`.
- **Database**: PostgreSQL or another supported database.
- **Docker**: For containerized setup.

## Setup Instructions

### 1. Create a `.env` File

In the root of your project, create a `.env` file and define the following environment variables:

ENV_TYPE=local
SERVICE_TOKEN=your_static_key_here


### 2. Configure Database Settings

Edit the database parameters in `app/src/app/settings.py` to match your database configuration.

### 3. Create a Virtual Environment

#### Windows

1. Open Command Prompt and navigate to your project directory.
2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   venv\Scripts\activate
   ```

#### Linux

1. Open Terminal and navigate to your project directory.
2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

### 4. Install Dependencies

With the virtual environment activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

Run the following command to apply database migrations:

```bash
alembic upgrade head
```

### 6. Run the Project Locally

Start the application using the following command:

```bash
uvicorn app.main:app --reload
```

### Accessing the API Documentation

Once the server is running, you can access the API documentation via Swagger UI at:

[http://127.0.0.1:8000/api/v1/docs](http://127.0.0.1:8000/api/v1/docs)

## Docker Setup

### Running with Docker

1. **Build the Docker Image**: 

   ```bash
   docker build -t fastapi_project .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -d -p 8000:8000 fastapi_project
   ```


## Notes

- Ensure that your database is running and accessible from the environment where you are running the application.
- Adjust the `.env` file as needed to match your specific configuration and environment requirements.