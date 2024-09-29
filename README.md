# Inventory Management System

A simple Inventory Management System built with Django Rest Framework that supports CRUD operations on inventory items. The application includes JWT-based authentication for secure access, Redis caching for improved performance, and comprehensive logging and testing features.

## Features

- User registration and JWT authentication.
- CRUD operations for inventory items.
- Redis caching for frequently accessed items.
- Comprehensive logging for monitoring and debugging.
- Unit tests to ensure functionality.

## Technologies Used

- **Django**: Web framework for building the API.
- **Django Rest Framework (DRF)**: Toolkit for building Web APIs.
- **PostgreSQL**: Database for storing inventory items.
- **Redis**: Caching solution for performance improvement.
- **JWT**: Authentication for securing API endpoints.

## API Endpoints
Authentication
Token Obtain Pair:

POST /api/token/
Request Body: { "username": "your_username", "password": "your_password" }
Returns: Access and refresh tokens.
Token Refresh:

POST /api/token/refresh/
Request Body: { "refresh": "your_refresh_token" }
Returns: New access token.
Inventory Item Endpoints
Create Item:

POST /items/
Request Body: { "name": "item_name", "description": "item_description" }
Returns: Created item details.
Read Item:

GET /items/{item_id}/
Returns: Item details.
Update Item:

PUT /items/{item_id}/
Request Body: { "name": "updated_name", "description": "updated_description" }
Returns: Updated item details.
Delete Item:

DELETE /items/{item_id}/
Returns: Success message.
Testing
To run the unit tests, use the following command:

bash
Copy code
python manage.py test
