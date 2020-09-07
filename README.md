# Django API Project
A django template

## Instaltion

### Install the project via python virtualenv

Create and launch a virtualenv
```sh
python3 -m venv .env
source .env/bin/active
```

Install the project requirements (within the virtualenv) and migrate to create the database.

```sh
pip install -r requirements.txt
python manage.py migrate
```

### Install the project via docker-compose

Start docker-compose

```sh
docker-compose up
```

Migrations are running on starting doker-compose no need to re run


## Endpoints

GET `/api/scrapers/`

HTTP Status Code `200`
```sh
curl --request GET http://localhost:8000/api/scrapers/
```
Response example
HTTP Status Code `200`
```json
{
  "scrapers": [
    {
      "id": 2,
      "created_at": "2020-06-30T22:16:41.375386+00:00",
      "currency": "bitcoin",
      "frequency": 60,
      "value": 9150.05,
      "value_updated_at": "2020-06-30T22:21:58.108506+00:00"
    },
    {
      "id": 3,
      "created_at": "2020-06-30T22:21:08.028843+00:00",
      "currency": "tether",
      "frequency": 100,
      "value": 0.999931,
      "value_updated_at": "2020-06-30T22:22:10.522852+00:00"
    }
  ]
}
```

POST `/api/scrapers/`

HTTP Status Code `200`
```sh
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"currency": "Dogecoin", "frequency": 25}' \
     http://localhost:8000/api/scrapers/
```

Response example
```json
{
  "id": 5,
  "created_at": "2020-07-01T22:07:47.797137+00:00",
  "currency": "Dogecoin",
  "frequency": 25
}
```

In case of any validation error

HTTP Status Code `400`

Response example
```json
{
    "error": {
        "currency": [
            {
                "message": "This field is required.",
                "code": "required"
            }
        ],
        "frequency": [
            {
                "message": "This field is required.",
                "code": "required"
            }
        ]
    }
}
```

PUT `/api/scrapers/`

HTTP Status Code `200`
```sh
curl --header "Content-Type: application/json" \
     --request PUT \
     --data '{"id": 4, "frequency": 35}' \
     http://localhost:8000/api/scrapers/
```

Response example
```json
{
    "msg": "Scraper updated"
}
```

In case of any validation error

HTTP Status Code `400`

Response example
```json
{
    "error": {
        "frequency": [
            {
                "message": "This field is required.",
                "code": "required"
            }
        ],
        "id": [
            {
                "message": "This field is required.",
                "code": "required"
            }
        ],
        "value": [
            {
                "message": "Enter a whole number.",
                "code": "invalid"
            }
        ]
    }
}
```

DELETE `/api/scrapers`

HTTP Status Code `200`
```sh
curl --header "Content-Type: application/json" \
     --request DELETE \
     --data '{"id": 4}' \
     http://localhost:8000/api/scrapers/
```

Response example
```json
{
    "msg": "Scraper deleted"
}
```

In case of any validation error

HTTP Status Code `400`

Response example
```json
{
    "error": {
        "id": [
            {
                "message": "The scraper was not found.",
                "code": "not_found"
            }
        ]
    }
}
```

## Tests
To run the tests for the project run the follow script
```sh
python manage.py test api
```

And test are automated thanks to [github actions](https://github.com/features/actions) ♥️

[Here](https://github.com/eriksape/django_api/actions) are automated test runned in this project