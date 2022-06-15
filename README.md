# smart-health-api
API Rest Smart Health using Python, FastAPI and PostgreSQL

# Documentation
## Production
https://smart-health-api-production.up.railway.app/
## Development
https://smart-health-api-development.up.railway.app/docs

## Project Setup
```shell
pip install -r requirements.txt
```

### Configuration
Create `.env` file in root:
```text
STAGE=dev or prd

DB_HOST_PRD=your database host for production
DB_PASS_PRD=your database pass for production
DB_USER_PRD=your database user for production
DB_NAME_PRD=your database name for production

DB_HOST_DEV=your database host for production
DB_PASS_DEV=your database pass for production
DB_USER_DEV=your database user for production
DB_NAME_DEV=your database name for production

```

### Run and Hot-Reload for Development
```shell
uvicorn main:app --reload
```
