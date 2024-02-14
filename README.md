
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

   -- Note* The Dockerfile calles migrate by default as it runs the server.

8. **Load initial data into the database from init_db.sql:**

   ```bash
   cd ./scripts
   source ./insertdata.sh
   ```

   *** If this is the first time you've run the app.  Create the init_db.sql by running
   - From projet root

   ```
   source ./venv/bin/activate
   cd scripts
   python3 ./generatesql.py
   ```

   This creates
   ./scripts/init_db.sql with 100,000 entires. Feel free to mod geneatesql.py and make it 1 million or whatever number


9. **Finally, start the Django development server:**

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
### Note* docker-compose.yml starts up this server auto.  Comment it out if you'd like to run the server from command line directly.

## Usage

Once the server is running, you can access the API endpoints using a web browser or a tool like curl or Postman. Here are the available endpoints:

- `/app/v2/suppliers`: This endpoint provides access to supplier data. You can use query parameters to filter and paginate the results.


## Remember to create the .env files from the .env.template files.

```
./.env
./react_ui_example/.env
```

### React_ui_example  Will demonstrate calling this API for endless scrolling of "Suppliers"
- The Sub project unser this project ./react_ui_example/
- It contains it's own readme file.
- Responsive Application written in react/redux/bootstrap  
- It's an example of calling the server api in this django and demonstrates an endless scroll example.

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



## Install mongo client  This needs to be there to run the docker-compose

To install the MongoDB client on an Ubuntu 22.10 server, you can use the MongoDB official repository, which provides the most up-to-date versions of MongoDB and its tools. This method ensures you get the MongoDB client compatible with Ubuntu 22.10. Here's how to do it:

Import the MongoDB public GPG key to ensure that the software package is authentic:

```
bash
Copy code
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
```
Add the MongoDB repository to your server. Since Ubuntu 22.10 might not have a direct repository, you can use the repository for the latest LTS version available at the time of your setup. For this example, we'll use a generic command; adjust it if there's a newer version available:

```
bash
Copy code
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
```

Update your local package database to include the newly added MongoDB repository:

```
bash
Copy code
sudo apt-get update
Install the MongoDB client. This step will only install the MongoDB client without the server 
```
components:

```
bash
Copy code
sudo apt-get install -y mongodb-org-shell
```

If you only need the MongoDB shell (mongo), this is the package you should install (mongodb-org-shell). It will allow you to connect to a MongoDB database running on another server without installing the entire MongoDB server package.

Please note that MongoDB versions and repository URLs can change. If MongoDB has released newer versions after this instruction was created, you might want to check the official MongoDB documentation for the most current repository setup and version numbers.


# Demonstation of a SQL version of a TTL key json store.

## KeyValueJsonStoreAPIView  app/v2/values/  api
-TTL_MINUTES in .env is how many minutes.  For example  TTL_MINUTES=5  means the TTL is 5 minutes.
- The Age-ing is done via a chron job setup in the docker file.  run_delete_expired_values.sh gets run on the cron.
- This goes Against the delete_expired_values.py script that runs every minute and deletes all entries
    that no longer should be in the database. 
- The script in ./ called test_key_value_api.py calls this api as a rest client to test out the various cases.  After the server is running, you can run this script to see what and how the API functions.  Good way to see how it works as well. 
