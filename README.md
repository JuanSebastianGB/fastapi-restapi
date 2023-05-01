## FastAPI-RESTAPI

FastAPI-RESTAPI is a RESTful API built with the FastAPI framework. The API provides endpoints for creating, reading, updating, and deleting data from a database. The API is built using asynchronous programming, which allows for high-performance and scalable operations.

The repository contains the following files and directories:

### Docker Compose files

The repository includes two Docker Compose files:

1.  `docker-compose.yml`: This is the main Docker Compose file that is used for running the application in production mode. It contains the necessary configuration for running the API using a production-ready WSGI server (gunicorn), and a MYSQL database.
2.  `docker-compose.dev.yml`: This Docker Compose file is used for running the application in development mode. It includes the necessary configuration for running the API using the development server provided by FastAPI, and a MYSQL database.

### Directories

1.  `app`: This directory contains the main application code for the API. It includes the following subdirectories:

    - `config`: This directory contains the code for connecting to the database and defining the database models.

2.  `models`: This directory contains the models of the application.
3.  `routes`: This directory contains the routes of the applciation.

### Files

1.  `main.py`: This file contains the main application entry point for running the API.
2.  `config.py`: This file contains the configuration settings for the application.
3.  `requirements.txt`: This file contains the Python dependencies required by the application.

4.  `README.md`: This file contains information about the repository and how to use the API.
5.  `LICENSE`: This file contains the license information for the repository.

## Running the API

To run the API, you will need to have Docker and Docker Compose installed on your machine. Once you have Docker and Docker Compose installed, follow these steps:

1.  Clone the repository:

    bashCopy code

    `git clone https://github.com/JuanSebastianGB/fastapi-restapi.git`

2.  Change into the repository directory:

    bashCopy code

    `cd fastapi-restapi`

3.  Build the Docker images:

    Copy code

    `docker-compose build`

4.  Run the Docker containers in production mode:

    Copy code

    `docker-compose up`

    The API will be available at `http://localhost/api`.

5.  To run the API in development mode, use the following command instead:

    Copy code

    `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up`

    The API will be available at `http://localhost:8000/api`.

That's it! You should now be able to use the API. If you have any questions or run into any issues, please refer to the README.md file or open an issue on the GitHub repository.
