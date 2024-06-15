# To-Do List API with FastAPI

## Description
This project is a To-Do List API developed using FastAPI, intended as a training exercise to familiarize with the framework. The project follows the [Module-Functionality](https://medium.com/@amirm.lavasani/how-to-structure-your-fastapi-projects-0219a6600a8f) structure.

The project is built in Python and utilizes the following libraries:
- [FastAPI](https://fastapi.tiangolo.com/)
- [UVICORN](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## Requirements
To run this project, you need to have the following installed:
1. [Python](https://www.python.org/)
2. [PIP](https://pip.pypa.io/en/stable/installation/)
3. [FastAPI](https://fastapi.tiangolo.com/)
4. [UVICORN](https://www.uvicorn.org/)
5. [SQLAlchemy](https://docs.sqlalchemy.org/en/20/intro.html#installation)

You can install the required Python libraries using:
```shell
pip install fastapi uvicorn sqlalchemy
```

## How to Use
1. Clone the project repository.
2. Navigate to the project root directory.
3. Run the following command to start the server:
    ```shell
    uvicorn main:app --reload
    ```
4. Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) or [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
