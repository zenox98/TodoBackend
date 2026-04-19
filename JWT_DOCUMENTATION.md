# JWT Authentication Documentation

This document outlines the implementation, workflow, and security mechanisms of JSON Web Token (JWT) authentication in the Todo application backend.

## 1. Implementation Overview

The backend uses **Django REST Framework (DRF)** combined with the **`djangorestframework-simplejwt`** library to provide a stateless authentication system.

### Core Components:
- **Library**: `rest_framework_simplejwt`
- **Algorithm**: HS256 (HMAC with SHA-256)
- **Signing Key**: Uses the project's `SECRET_KEY` from `settings.py`.

---

## 2. Authentication Workflow

1. **Obtain Token**: The user sends a `POST` request to `/api/token/` with their `username` and `password`.
2. **Verification**: The backend verifies credentials. If valid, it returns:
   - `access`: Short-lived token for API authorization.
   - `refresh`: Longer-lived token to generate new access tokens.
3. **Authorization**: For every protected request (e.g., `/api/todo/`), the frontend must include the access token in the HTTP header:
   `Authorization: Bearer <access_token>`
4. **Token Refresh**: When the access token expires, the frontend sends the refresh token to `/api/token/refresh/` to receive a new access token without requiring a password.

---

## 3. Token Lifecycles & Configuration

Defined in `todo_backend/settings.py`:

| Token Type | Lifetime | Purpose |
| :--- | :--- | :--- |
| **Access Token** | 30 Minutes | Used for authorizing every API request. |
| **Refresh Token** | 1 Day | Used to obtain a new access token once the current one expires. |

---

## 4. Token Storage & State

### Frontend (Client-Side)
The backend does not manage frontend storage. It is the client's responsibility to store tokens securely. Common practices include:
- **LocalStorage/SessionStorage**: Accessible via JavaScript (vulnerable to XSS).
- **Secure/HttpOnly Cookies**: Most secure against XSS (requires additional backend configuration).

### Backend (Stateless vs. Stateful)
- **Access Tokens**: These are **entirely stateless**. The backend does not store them. It only verifies their signature using the `SECRET_KEY`.
- **Refresh Tokens**: These are partially stateful due to the **Blacklist** feature.

---

## 5. Security & Blacklisting

The implementation includes the **Token Blacklist** feature (`BLACKLIST_AFTER_ROTATION: True`).

### Where are blacklisted tokens stored?
When a refresh token is used to get a new access token, or if a user logs out (if implemented), the old refresh token is moved to the **Backend Database**.

- **Database Table**: `token_blacklist_blacklistedtoken`
- **Logic**: Once a token's unique identifier (JTI) is recorded in this table, the backend will reject any future attempts to use that specific token, even if it hasn't expired yet. This prevents "replay attacks" if a refresh token is stolen.

---

## 6. API Endpoints Reference

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/token/` | `POST` | Exchange credentials for Access & Refresh tokens. |
| `/api/token/refresh/` | `POST` | Exchange a Refresh token for a new Access token. |
| `/api/users/register/` | `POST` | Register a new user and receive tokens immediately. |

---

## 7. Security Best Practices
1. **Never** share the `SECRET_KEY`.
2. **Always** use HTTPS in production to prevent tokens from being intercepted in transit.
3. Ensure the frontend handles token expiration gracefully by implementing automatic refresh logic.
