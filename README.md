# python-flask-sample

A sample RESTful Python/Flask server that uses Pipenv for dependency management.

## Table of Contents

- [OpenAPI](#open-api-specifications)
- [Dependencies](#dependencies)
- [Setup Instructions](#setup-instructions)
- [Testing](#testing)

## Open API Specifications

To view the endpoint specs for this server, please refer to the [OpenAPI yaml](openapi.yaml). To render neatly,
launch the server and go to [/openapi](http://localhost:5000/openapi)

## Dependencies

- [Python 3](https://www.python.org/downloads/) installed on your machine
- [Visual Studio Code](https://code.visualstudio.com/) or any other code editor of your choice

## Setup Instructions

### PostgreSQL

1. Clone the `docker-postgres-sample` repository to your local machine:

    ```bash
    $ git clone https://github.com/devinobrien-css/docker-postgres-sample.git
    ...
    ```

2. Follow the instructions provided in that repository's README to launch the instance.

> Note: this repo is dependent on running a local Postgres instance. An example can used by following the ReadMe [from this repo](https://github.com/devinobrien-css/docker-postgres-sample) as stated above.

### Build and Run the Project

1. Open the project in Visual Studio Code.

2. Run the following command to establish a virtual environment:

```bash
    pipenv shell
```

3. Restore pip packages for the server by running the following:

```bash
    pipenv install
```

4. Start the server by running the folowing:

```bash
    python main.py
```

> The project should now be accessible through [localhost:5077](http://localhost:5077). Open in browser to verify the healthcheck endpoint is hit!

## Testing

A [postman collection](postman-testing.json) has been included for convenient testing
