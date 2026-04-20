# Django Todo API

A RESTful backend API for a Todo application built with Django and Django REST Framework. It supports user registration, JWT-based authentication, and full CRUD operations for individual users' todo items.

## Features

*   **User Registration and Profile Management:** Create new user accounts and retrieve user profile information.
*   **Secure Authentication:** Uses JSON Web Tokens (JWT) for secure, stateless authentication.
*   **CRUD Operations:** Create, Read, Update, and Delete Todo items.
*   **Resource Isolation:** Users can only access and modify their own Todo items.
*   **Production Ready:** Configured for deployment on Render using PostgreSQL, Gunicorn, and WhiteNoise for static files.

## Tech Stack

*   **Framework:** Django 6.0
*   **API Toolkit:** Django REST Framework (DRF)
*   **Authentication:** djangorestframework-simplejwt
*   **Database:** PostgreSQL (Production) / SQLite (Local fallback)
*   **WSGI Server:** Gunicorn
*   **Static File Serving:** WhiteNoise

## Local Development Setup

Follow these steps to set up the project on your local machine.

### Prerequisites

*   Python 3.x
*   pip (Python package installer)
*   venv (Virtual environment)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd todo_backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables:**
    By default, the project uses SQLite for local development. If you want to test with a local PostgreSQL database, set the `DATABASE_URL` environment variable.
    ```bash
    export DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
    ```

5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints Reference

All API endpoints are prefixed with `/api/`.

### Authentication

*   **`POST /api/token/`**
    *   **Description:** Obtain JWT access and refresh tokens.
    *   **Payload:** `{ "username": "your_username", "password": "your_password" }`
*   **`POST /api/token/refresh/`**
    *   **Description:** Refresh an expired access token using a refresh token.
    *   **Payload:** `{ "refresh": "your_refresh_token" }`

### Users

*   **`POST /api/users/register/`**
    *   **Description:** Register a new user. Returns user details along with initial JWT access and refresh tokens.
    *   **Payload:** User registration details (e.g., username, password, email).
*   **`GET /api/users/me/`**
    *   **Description:** Get the authenticated user's profile.
    *   **Headers:** `Authorization: Bearer <access_token>`

### Todos

*   **`GET /api/todo/`**
    *   **Description:** List all todos for the authenticated user.
    *   **Headers:** `Authorization: Bearer <access_token>`
*   **`POST /api/todo/`**
    *   **Description:** Create a new todo item.
    *   **Headers:** `Authorization: Bearer <access_token>`
    *   **Payload:** `{ "title": "Task title", "description": "Task description", "completed": false }`
*   **`GET /api/todo/<id>/`**
    *   **Description:** Retrieve a specific todo item by ID.
    *   **Headers:** `Authorization: Bearer <access_token>`
*   **`PUT / PATCH /api/todo/<id>/`**
    *   **Description:** Update a specific todo item.
    *   **Headers:** `Authorization: Bearer <access_token>`
    *   **Payload:** Updated todo fields.
*   **`DELETE /api/todo/<id>/`**
    *   **Description:** Delete a specific todo item.
    *   **Headers:** `Authorization: Bearer <access_token>`

## Deployment (Render)

This project is configured for seamless deployment on Render.

### Web Service Configuration

When creating or updating the Web Service in the Render Dashboard, use the following settings:

*   **Build Command:** `./build.sh`
*   **Start Command:** `gunicorn todo_backend.wsgi:application`

### Environment Variables

Ensure the following environment variables are set in your Render Web Service settings:

*   `DATABASE_URL`: The Internal Database URL of your Render PostgreSQL instance (e.g., `postgresql://user:password@hostname/dbname`).
*   `SECRET_KEY`: A secure, randomly generated string for Django's cryptographic signing. Do not use the default local key in production.