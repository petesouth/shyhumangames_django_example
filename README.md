
# Shy Human Games Django Example

This repository contains an example Django project developed by Shy Human Games.

## Introduction

This Django project serves as an example implementation for a supplier management system. It includes models, views, serializers, and migrations for managing supplier data.

## Installation

To run this project locally, follow these steps:

1. **Clone this repository to your local machine:**

   ```bash
   git clone https://github.com/shyhumangames/shyhumangames_django_example.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd shyhumangames_django_example
   ```

3. **Create a virtual environment and activate it (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your environment variables by creating a .env file in the root directory of the project. Here's an example .env file:**

   ```makefile
   DB_NAME=suppliers
   DB_USER=admin
   DB_PASSWORD=password123!
   DB_HOST=0.0.0.0
   DB_PORT=5432
   ALLOWED_HOSTS=127.0.0.1,localhost,192.168.12.131
   ```

6. **Start the PostgreSQL database using Docker Compose:**

   ```bash
   docker-compose up -d
   ```

7. **Run the database migrations to create the necessary tables:**

   ```bash
   python manage.py migrate
   ```

8. **Load initial data into the database from init_db.sql:**

   ```bash
   docker exec -i shyhumangames_django_example_db psql -U admin -d suppliers < scripts/init_db.sql
   ```

9. **Finally, start the Django development server:**

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## Usage

Once the server is running, you can access the API endpoints using a web browser or a tool like curl or Postman. Here are the available endpoints:

- `/v2/suppliers`: This endpoint provides access to supplier data. You can use query parameters to filter and paginate the results.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch to work on your feature or bug fix.
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your forked repository.
6. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License.

