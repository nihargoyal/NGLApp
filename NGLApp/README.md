# Problem Set 1

1. Write a regex to extract all the numbers with orange color background from the below text in italics (Output should be a list).

Ans.

import re

text = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'

regex_pattern = r'(?<=<span style="background-color:orange">)(\d+)(?=<\/span>)'
numbers = re.findall(regex_pattern, text)

print(numbers)

########################################################################################################################################################################################################################################

# Problem Set 2

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


########################################################################################################################################################################################################################################

# Project Set 3

Ques. Write and share a small note about your choice of system to schedule
periodic tasks (such as downloading a list of ISINs every 24 hours). Why did
you choose it? Is it reliable enough; Or will it scale? If not, what are the
problems with it? And, what else would you recommend to fix this problem at
scale in production?

Ans. When it comes to choosing a system to schedule periodic tasks like downloading a list of ISINs every 24 hours, reliability and scalability are key considerations. One popular choice is a job scheduling system like Apache Airflow. It offers robust features, such as task dependencies, retries, and monitoring, ensuring reliable execution of periodic tasks.

However, if scaling becomes a concern in production, some challenges may arise. As the task load increases, the system's performance might be affected, leading to potential delays or failures. To address this, it's advisable to consider a few potential solutions:

1. Distributed task execution: Implement a distributed architecture using technologies like Apache Kafka or RabbitMQ to handle task distribution across multiple worker nodes, enabling better scalability and load balancing.

2. Horizontal scaling: Add more worker nodes to the system to distribute the task workload effectively and ensure timely execution.

3. Monitoring and auto-scaling: Implement a monitoring system to track resource utilization and automatically scale up or down based on predefined thresholds, ensuring optimal performance during peak and off-peak periods.

4. Job optimization: Analyze the task execution flow and optimize the task dependencies, reducing unnecessary dependencies and improving overall system efficiency.

It's crucial to evaluate the specific needs and requirements of the project to determine the most appropriate solution for scaling periodic task scheduling in production. Regular monitoring, performance testing, and continuous optimization will help ensure the system remains reliable and scalable as the workload increases.



Ques. In what circumstances would you use Flask instead of Django and vice
versa?

Ans. Flask and Django are both popular Python web frameworks, and the choice between them depends on the specific project requirements and development goals. Here are some circumstances where each framework may be preferred:

Use Flask when:
1. Lightweight and flexibility are important: Flask is a micro-framework that provides a minimalistic approach, allowing developers to have more control over the project structure and components.
2. Building small to medium-sized applications: Flask's simplicity and modular design make it well-suited for smaller projects where a lighter footprint and faster development process are desired.
3. API development: Flask's simplicity and focus on minimalism make it an excellent choice for building RESTful APIs quickly and efficiently.
4. Customization and extensibility are priorities: Flask provides more freedom to choose and integrate third-party libraries and components as per project-specific requirements.

Use Django when:
1. Rapid development of larger, complex applications is required: Django follows the "batteries included" principle, providing a robust and comprehensive set of features out-of-the-box, including an ORM, authentication system, and admin interface. This makes it well-suited for building complex web applications quickly.
2. Built-in features and conventions are valued: Django's integrated approach saves development time by offering pre-built solutions for common functionalities like user authentication, database management, and form handling.
3. Content management or data-driven applications: Django's powerful ORM and built-in admin interface make it a strong choice for content-heavy websites, CMS platforms, or applications that rely heavily on databases.
4. Security and scalability are top priorities: Django has a strong focus on security best practices and provides tools to prevent common security vulnerabilities. It also offers scalability options such as caching, database routing, and load balancing.

Ultimately, the choice between Flask and Django depends on the project's specific requirements, team expertise, and development priorities.