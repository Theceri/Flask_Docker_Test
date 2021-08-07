# Flask_Docker_Test
Test deploy app on linux server using docker

## Setup a .env file with the following variables
```
FLASK_APP=main.py
FLASK_ENV=development
FLASK_DEBUG=1
SQLALCHEMY_DATABASE_URI=posgresql://postgres:postgres@localhost:5432/postgres
SQLALCHEMY_TRACK_MODIFICATIONS=False

```
