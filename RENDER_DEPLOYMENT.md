# Render Deployment Details

This document contains the configuration details for the services created and deployed on the Render cloud platform.

## 1. Web Service (Django Application)

*   **Name:** `TodoBackend`
*   **Deployment Method:** GitHub Repository
*   **Environment:** Python 3
*   **Build Command:** `./build.sh` (Installs dependencies via pip, collects static files, and runs database migrations)
*   **Start Command:** `gunicorn todo_backend.wsgi:application` (Runs the application using the Gunicorn WSGI server)

### Environment Variables Required
*   `DATABASE_URL`: Set to the Internal Database URL of the PostgreSQL service (see below).
*   `SECRET_KEY`: A secure, randomly generated string used for Django's cryptographic signing.

## 2. Database Service (PostgreSQL)

*   **Name:** `demoTODO`
*   **Hostname:** `dpg-d7icb3beo5us73dfdipg-a`
*   **Port:** `5432`
*   **Database Name:** `demotodo_oi3l`
*   **Username:** `terminal`
*   **Password:** `W90u1GXnC5bXmBkIPuGuwEyIg7Nk87aS`

### Connection Strings
*   **Internal Database URL:** `postgresql://terminal:W90u1GXnC5bXmBkIPuGuwEyIg7Nk87aS@dpg-d7icb3beo5us73dfdipg-a/demotodo_oi3l`
    *(Use this URL for the `DATABASE_URL` environment variable in the Web Service, as they are in the same region. It is faster and doesn't consume external bandwidth.)*
*   **External Database URL:** `postgresql://terminal:W90u1GXnC5bXmBkIPuGuwEyIg7Nk87aS@dpg-d7icb3beo5us73dfdipg-a.singapore-postgres.render.com/demotodo_oi3l`
    *(Use this URL if you need to connect to the database from your local machine, e.g., using pgAdmin, DBeaver, or psql.)*
