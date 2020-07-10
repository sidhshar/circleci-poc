# Complete Tutorial

Current Build Status: [![S3Infosoft](https://circleci.com/gh/sidhshar/circleci-poc.svg)](https://circleci.com/gh/sidhshar/circleci-poc)

## Setup

In a python virtual environment, run:

- `pip install -r requirements.txt`
- `python manage.py migrate blog`
- `python manage.py createsuperuser` (to create user that you'll use to log in)

### Run the application

```bash
python manage.py runserver
```

### Test

```bash
python manage.py test
```

### Docker
NB: The app instance will run off the a preset admin user as set in [init.sh](/init.sh).

To spin up the application using docker, ensure that Docker is installed. Then run:

```bash
docker-compose up
```

Or in detached mode:

```bash
docker-compose up -d
```

The application will be live at [0.0.0.0:8000](0.0.0.0:8000)
