# TaskApp

This documentation provides an overview of the available API endpoints and their functionalities.

## Authentication System

### User Registration

**Endpoint:** `/api/signup/`

- Method: `POST`
- Description: Registers a new user account.
- Request Body:
  - `username` (string): User's username.
  - `password` (string): User's password.
  - `email` (string): User's email address.
- Response:
  - `201 Created`: User registration successful.
  - `400 Bad Request`: Invalid request parameters.

### User Login

**Endpoint:** `/api/login/`

- Method: `POST`
- Description: Logs in a user and generates access and refresh tokens.
- Request Body:
  - `username` (string): User's username.
  - `password` (string): User's password.
- Response:
  - `200 OK`: Login successful. Returns access and refresh tokens as cookies.
  - `401 Unauthorized`: Invalid credentials.

### User Logout

**Endpoint:** `/api/logout/`

- Method: `POST`
- Description: Logs out the authenticated user and invalidates the tokens.
- Response:
  - `200 OK`: Logout successful.
  - `401 Unauthorized`: User not authenticated.

## User Facing End-points

### List Apps

**Endpoint:** `/api/apps/list/`

- Method: `GET`
- Description: Retrieves a list of apps.
- Authentication: Required.
- Response:
  - `200 OK`: Returns a list of apps.
  - `401 Unauthorized`: User not authenticated.

### Retrieve App Details

**Endpoint:** `/api/apps/detail/{app_id}/`

- Method: `GET`
- Description: Retrieves details of a specific app.
- Authentication: Required.
- Response:
  - `200 OK`: Returns the app details.
  - `404 Not Found`: App not found.
  - `401 Unauthorized`: User not authenticated.

### Complete User Task

**Endpoint:** `/api/apps/detail/{app_id}/`

- Method: `POST`
- Description: Marks a user task as completed and uploads a screenshot.
- Authentication: Required.
- Request Body:
  - `app_id` (integer): ID of the app for the task.
  - `screenshot` (file): Screenshot image file.
- Response:
  - `201 Created`: Task completion successful.
  - `400 Bad Request`: Invalid request parameters.
  - `401 Unauthorized`: User not authenticated.

### User Profile

**Endpoint:** `/api/profile/`

- Method: `GET`
- Description: Retrieves the profile of the authenticated user.
- Authentication: Required.
- Response:
  - `200 OK`: Returns the user profile.
  - `401 Unauthorized`: User not authenticated.

### Completed User Tasks

**Endpoint:** `/api/tasks/list/`

- Method: `GET`
- Description: Retrieves a list of completed user tasks.
- Authentication: Required.
- Response:
  - `200 OK`: Returns a list of completed user tasks.
  - `401 Unauthorized`: User not authenticated.

### Total Points

**Endpoint:** `/api/total-points/`

- Method: `GET`
- Description: Retrieves the total points earned by the authenticated user.
- Authentication: Required.
- Response:
  - `200 OK`: Returns the total points.
  - `401 Unauthorized`: User not authenticated.

## Admin Facing End-points

### Create App

**Endpoint:** `/api/apps/create/`

- Method: `POST`
- Description: Creates a new app.
- Authentication: Admin access required.
- Request Body:
  - `name` (string): App name.
  - `link` (string): App link.
  - `points` (integer): Points earned for downloading the app.
- Response:
  - `201 Created`: App creation successful.
  - `400 Bad Request`: Invalid request parameters.
  - `401 Unauthorized`: Admin access required.

### Update App Details

**Endpoint:** `/api/apps/update/{app_id}/`

- Method: `PUT`
- Description: Updates the details of a specific app.
- Authentication: Admin access required.
- Request Body:
  - `name` (string): App name.
  - `link` (string): App link.
  - `points` (integer): Points earned for downloading the app.
- Response:
  - `200 OK`: App update successful.
  - `400 Bad Request`: Invalid request parameters.
  - `404 Not Found`: App not found.
  - `401 Unauthorized`: Admin access required.

### Delete App

**Endpoint:** `/api/apps/update/{app_id}/`

- Method: `DELETE`
- Description: Deletes that specific app.
- Authentication: Admin access required.
- Response:
  - `200 OK`: App deleted successfully.
  - `404 Not Found`: App not found.
  - `401 Unauthorized`: Admin access required.

### Retrieve User Task Details

**Endpoint:** `/api/tasks/detail/{task_id}/`

- Method: `GET`
- Description: Retrieves details of a specific user task.
- Authentication: Admin access required.
- Response:
  - `200 OK`: Returns the user task details.
  - `404 Not Found`: Task not found.
  - `401 Unauthorized`: User not authenticated.

### Delete User Task

**Endpoint:** `/api/tasks/detail/{task_id}/`

- Method: `DELETE`
- Description: Deletes specific user task.
- Authentication: Admin access required.
- Response:
  - `200 OK`: Task deleted successfully.
  - `404 Not Found`: Task not found.
  - `401 Unauthorized`: User not authenticated.

## Manual Token Generation

### Manual Token for User

**Endpoint:** `/api/token/user/`

- Method: `POST`
- Description: Generates an access and refresh tokens as cookies.
- Request Body:
  - `username` (string): User's username.
  - `password` (string): User's password.
- Response:
  - `200 OK`: Returns access and refresh tokens as cookies for User.
  - `400 Unauthorized`: Invalid credentials.

### Manual Token for Admin

**Endpoint:** `/api/token/admin/`

- Method: `POST`
- Description: Generates an access and refresh tokens as cookies.
- Request Body:
  - `username` (string): Admin's username.
  - `password` (string): Admin's password.
- Response:
  - `200 OK`: Returns access and refresh tokens as cookies for Admin.
  - `400 Unauthorized`: Invalid credentials.

###  Refresh Token Generator

**Endpoint:** `/api/token/refresh/`

- Method: `POST`
- Description: Generates a new access token from refresh token.
- Request Body:
  - `refresh` (string): refresh token.
- Response:
  - `200 OK`: Returns access token.
  - `400 Unauthorized`: Invalid refresh token.
