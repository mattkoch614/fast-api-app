# FastAPI Social Media API

A RESTful API built with FastAPI for a social media application. This project is based on the [Mastering REST APIs with FastAPI](https://www.coursera.org/learn/packt-mastering-rest-apis-with-fastapi-1xeea) course from Coursera.

## Overview

This project demonstrates building a production-ready REST API using FastAPI, following best practices for code organization, testing, and deployment. The API currently supports basic social media functionality including posts and comments.

## Features

- **RESTful API Design**: Clean and intuitive API endpoints
- **Modular Architecture**: Organized code structure using APIRouter
- **Pydantic Models**: Type-safe data validation and serialization
- **Async Support**: Built on FastAPI's async capabilities

## Project Structure

```
fast-api-app/
├── fhirapi/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── models/
│   │   └── post.py          # Pydantic models for posts
│   └── routers/
│       └── post.py          # Post-related API endpoints
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fast-api-app
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI development server:

```bash
uvicorn fhirapi.main:app --reload
```

The API will be available at `http://localhost:8000`

- API Documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API Documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### Posts

- `POST /post` - Create a new post
- `GET /post` - Get all posts

## Development

For development dependencies, install:

```bash
pip install -r requirements-dev.txt
```

## Course Reference

This project follows the curriculum from the [Mastering REST APIs with FastAPI](https://www.coursera.org/learn/packt-mastering-rest-apis-with-fastapi-1xeea) course, which covers:

- Building RESTful APIs with FastAPI
- User authentication and authorization
- Async database integration
- Logging and error tracking
- Testing with pytest
- Background tasks
- File uploads
- Deployment to production platforms

## License

This project is for educational purposes as part of the Coursera course.
