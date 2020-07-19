# Birras Meetups

- Swagger/API docs at _/docs_ and _/redoc_

## Development
- Build dev: `docker-compose build`
- Run dev: `docker-compose up`
- Run tests: `docker-compose run --no-deps api pytest`

## Production
- Build prd: `docker build . -f docker/app/Dockerfile --no-cache -t meetups`
- Run prd: `docker run -d -p 5000:5000 --name meetups meetups`

## Required Environment Variables
- API_KEY
- POSTGRES_HOST
- POSTGRES_PORT
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB
- DEV_MODE
- RAPID_API_URL
- RAPID_API_KEY
- RAPID_API_HOST
- RAPID_API_COORD